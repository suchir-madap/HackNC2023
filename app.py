from gtts import gTTS
import streamlit as st
import base64
from ingestPDF import readUploadedPdf
from langtest import chunking


class SessionState:
    def __init__(self):
        self.play = False 

session_state = SessionState()

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

#PASS STRING TO TURN INTO AUDIO MP3
def textToAudio(str):
    audio = gTTS(str)
    audio.save('output.mp3')

#STYLIZE THE AUDIO PLAYBACK
style_css = """
audio::-webkit-media-controls-panel,
audio::-webkit-media-controls-enclosure {
    background-color:#BBBBBB;}

audio::-webkit-media-controls-time-remaining-display,
audio::-webkit-media-controls-current-time-display {
    color: white;
    text-shadow: none; 
}
audio::-webkit-media-controls-timeline {
  background-color: #888888;
  border-radius: 25px;
  margin-left: 10px;
  margin-right: 10px;
}
audio {
    width: 100px;
    height: 100px;
}
"""
st.markdown(
    "<style>" + style_css + "</style>", unsafe_allow_html=True
)

#GENERATE AN AUDIO PLAYBACK FROM MP3
def generateAudio():
    audio_file = open('output.mp3', 'rb')
    st.audio(audio_file)

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

st.subheader("Welcome to our AI Text Analyzer!")
st.write("This program is designed to help you answer any questions you have about your uploaded document. Please enter a question/prompt below and the computer will generate a response to answer your query!")
st.write("Please input your text here, I will analyze it: ")
doc = st.text_area('Enter your text or upload your file below: ')
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

query = st.text_area('Enter your question: ')


passToLangChain = readUploadedPdf(uploaded_file)


from langtest import callAPI




# if answered != None:
#     st.subheader(answered)


col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button('Play'):
        answered = callAPI(passToLangChain, query)
        textToAudio(answered)
        autoplay_audio("output.mp3")
        st.experimental_rerun()
with col2:
    st.button('Pause')
with col3:
    if st.button('Reset'):
        st.experimental_rerun()