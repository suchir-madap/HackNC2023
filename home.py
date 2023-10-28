import streamlit as st

class SessionState:
    def __init__(self):
        self.play = False 

session_state = SessionState()

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
st.subheader("Welcome to our AI Text Analyzer!")
st.write("This program is designed to help you answer any questions you have about your uploaded document. Please enter a question/prompt below and the computer will generate a response to answer your query!")
st.write("Please input your text here, I will analyze it: ")
txt = st.text_area('Enter your text: ')


txt = st.text_area('Enter your question: ')

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.button('Play')

with col2:
    st.button('Pause')
with col3:
    st.button('Clear')
