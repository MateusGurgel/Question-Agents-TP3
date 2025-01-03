from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wikipedia_query_search_tool = WikipediaQueryRun(
    api_wrapper=api_wrapper,
    name="Wikipedia Search Tool",
    description="This will bring the top_k 1 result from Wikipedia for the query.",
)