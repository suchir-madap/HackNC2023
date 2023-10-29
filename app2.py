import streamlit as st
from ingestPDF import readUploadedPdf


import io
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)





