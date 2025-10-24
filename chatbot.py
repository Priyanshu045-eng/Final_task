import streamlit as st
import requests


st.set_page_config(page_title="Gemini Chatbot")
st.title("Gemini Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role = msg["role"]
    with st.chat_message(role):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": user_input}
    ).json()
    bot_reply = response.get("response")

    with st.chat_message("AI"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "AI", "content": bot_reply})
