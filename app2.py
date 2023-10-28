import streamlit as st
from ingestPDF import readUploadedPdf


 import io
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)



 uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

 readUploadedPdf(uploaded_file)
