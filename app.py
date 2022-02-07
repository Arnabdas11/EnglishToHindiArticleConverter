import streamlit as st
from PIL import Image
from pytesseract import Output
import pytesseract
from transformers import pipeline
import Converter
import Scanner
import torch
pipe = pipeline(task='text2text-generation', model='facebook/m2m100_418M')


def translate(img,pipe):
    # Preprocessing the image
    img = Scanner.preprocessing(img)
    # Scanning and getting the dataframe
    text = Scanner.scanner(img)
    # Sentencing the text
    sentenced_text = Converter.sentencing(text)
    # Result
    result = Converter.converter(sentenced_text, pipe)
    return result

st.title("English to Hindi Language Converter")
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Choose a file", type='jpg')
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image)
    btn = st.button("Translate")

with col2:
    st.header("Translated Text")
    if btn:
        output = translate(uploaded_file)
        st.write(output)

