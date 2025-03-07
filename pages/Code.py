import streamlit as st
# import google.generativeai as genai
# import os

# # Display logo (fixed)
# st.logo("Assets/dummy_logo.png")  # Replace with your logo path

# # Hide Streamlit branding
# hide_streamlit_style = """
#     <style>
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}
#     </style>
# """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# # Check login status (replace with your actual login logic)
# if "logged_in" not in st.session_state or not st.session_state.logged_in:
#     st.error("Please login to continue")
#     st.stop()

# # Display chat header
# st.header(":green[Code Execution Chat]")
# st.write("Chat and execute code.")
# st.write("-----")

# # Initialize chat history
# if "chat_messages" not in st.session_state:
#     st.session_state["chat_messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# # Display previous chat messages
# for msg in st.session_state["chat_messages"]:
#     st.chat_message(msg["role"]).write(msg["content"])

# # Handle user input
# if prompt := st.chat_input("Ask your question:"):
#     if "GOOGLE_API_KEY" not in st.secrets:
#         st.error("API key missing in secrets. Please add `GOOGLE_API_KEY` in `.streamlit/secrets.toml`.")
#         st.stop()

#     api_key = st.secrets["GOOGLE_API_KEY"]
#     genai.configure(api_key=api_key)

#     try:
#         # Initialize chat object if not already created
#         if "chat_object" not in st.session_state:
#             model = genai.GenerativeModel("gemini-1.5-pro")  # Using a valid Gemini model
#             st.session_state["chat_object"] = model.start_chat(history=[])

#         chat = st.session_state["chat_object"]
#         response = chat.send_message(prompt)

#         # Extract response text
#         response_text = response.text if response.text else "No response received."

#     except Exception as e:
#         st.error(f"An error occurred: {e}")
#         st.stop()

#     # Append user input and response to chat history
#     st.session_state["chat_messages"].append({"role": "user", "content": prompt})
#     st.session_state["chat_messages"].append({"role": "assistant", "content": response_text})

#     # Display assistant's response
#     st.chat_message("assistant").write(response_text)

#     st.rerun()


st.warning("Un-Authorized Access")