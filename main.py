import streamlit as st

from agents.teacher import Teacher
import json

input = st.chat_input("Diga um tópico para fazer perguntas")

if input:
    #questions = [{"Question": "question", "Answer": "answer"}]
    teacher = Teacher()
    questions = teacher.start_questioning(input)
    questions = json.loads(questions['output'])

    print(questions)

    for question in questions:
        with st.expander(question["Question"]):
            st.write(question["Answer"])