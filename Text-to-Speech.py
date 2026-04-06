import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpapershome.com/images/pages/ico_h/27882.jpg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text_align:center;color:lightblue'>Text to Speech</h1>",unsafe_allow_html=True)
lang = st.selectbox(
    "Choose Language",
    ["en","ur","fr","ar","es"],index=0
)
text= st.text_area("Enter Text to Convert")
if st.button('Convert') and text:
    translator=GoogleTranslator(source='en',target=lang).translate(text)
    #st.write(translator)

    tts=gTTS(translator,lang=lang)
    tts.save("output.mp3")
    
    audio1=open("output.mp3","rb")
    st.audio(audio1.read(),format="audio1/mp3")