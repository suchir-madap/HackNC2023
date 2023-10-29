# from gtts import gTTS
# import streamlit as st
# import base64

# #PASS STRING TO TURN INTO AUDIO MP3
# def textToAudio(str):
#     audio = gTTS(str)
#     audio.save('output.mp3')

# #STYLIZE THE AUDIO PLAYBACK
# style_css = """
# audio::-webkit-media-controls-panel,
# audio::-webkit-media-controls-enclosure {
#     background-color:#BBBBBB;}

# audio::-webkit-media-controls-time-remaining-display,
# audio::-webkit-media-controls-current-time-display {
#     color: white;
#     text-shadow: none; 
# }
# audio::-webkit-media-controls-timeline {
#   background-color: #888888;
#   border-radius: 25px;
#   margin-left: 10px;
#   margin-right: 10px;
# }
# audio {
#     width: 100px;
#     height: 100px;
# }
# """
# st.markdown(
#     "<style>" + style_css + "</style>", unsafe_allow_html=True
# )

# #GENERATE AN AUDIO PLAYBACK FROM MP3
# def generateAudio():
#     audio_file = open('output.mp3', 'rb')
#     st.audio(audio_file)

# def autoplay_audio(file_path: str):
#     with open(file_path, "rb") as f:
#         data = f.read()
#         b64 = base64.b64encode(data).decode()
#         md = f"""
#             <audio controls autoplay="true">
#             <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
#             </audio>
#             """
#         st.markdown(
#             md,
#             unsafe_allow_html=True,
#         )