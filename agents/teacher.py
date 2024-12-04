from langchain.agents import AgentExecutor, create_react_agent
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from decouple import config

from langchain_core.prompts import PromptTemplate

from agents.tools.google_search import google_search_tool
from agents.tools.wikipedia_query import wikipedia_query_search_tool

class Teacher:
    def __init__(self, max_questions=10):
        self.max_questions = max_questions
        self.tools = [wikipedia_query_search_tool, google_search_tool]
        self.llm = ChatOpenAI(openai_api_key=config("OPENAI_API_KEY"))
        self.memory = ConversationBufferMemory()

        system_prompt = """
            You are a Havard teacher applying a oral test. 
            Make questions about the following topic. 
            Respond in the same language as the topic.
            You have access to the following tools:
            
            use the following format:
            
            [
            {{
                "Question": "the input question you must answer",
                "Answer": "the answer to the question"
            }},
            {{
                "Question": "the input question 2 you must answer",
                "Answer": "the answer 2 to the question"
            }}
            ]
            

            {tools}
            
            Use the following format:
            
            Topic: the input question you must answer
            
            Thought: you should always think about what to do
            
            Action: the action to take, should be one of [{tool_names}]
            
            Action Input: the input to the action
            
            Observation: the result of the action
            
            ... (this Thought/Action/Action Input/Observation can repeat N times)
            
            Thought: I now know the final answer
            
            Final Answer: A list with every question and answer; Answer in valid JSON list format.
            
            Begin!
            
            Topic: {input}
            
            Thought:{agent_scratchpad}    
        """

        self.prompt = PromptTemplate.from_template(system_prompt)


    def start_questioning(self, topic: str):
        agent = create_react_agent(self.llm, self.tools, self.prompt)
        agent_executor = AgentExecutor(agent=agent, tools=self.tools, handle_parsing_errors=True, max_steps=3)

        return agent_executor.invoke(
            {
                "input": topic
            }
        )