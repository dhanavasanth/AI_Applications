from openai import OpenAI
import streamlit as st
from Home import *
st.logo("Assets/dummy_logo.png")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Check login status
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("Please login to continue")
    st.stop()

# Configure Gemini API
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']  # Replace with your API key
if not OPENAI_API_KEY:
    st.error("Gemini API key is missing. Please provide it.")
    st.stop()

else:
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = st.chat_input("Enter your prompt:")
    if prompt is not None:
        with st.spinner("The assistant is thinking..."):
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            time.sleep(5)
            if response is not None:
                st.image(response.data[0].url,use_container_width=True,caption=prompt)
                