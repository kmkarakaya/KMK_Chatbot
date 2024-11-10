#from openai import OpenAI
from ollama import chat
# https://github.com/ollama/ollama-python/tree/main/examples
models = ['qwen2.5:7b-instruct-q3_K_L','llama3.1:8b-instruct-q3_K_M','gemma:2b', 'aya:8b', 'gemma2:latest','llama3.2:3b','qwen2.5:3b','qwen2.5:7b']
system_prompt = [{
    'role': 'system',
    'content': 'Sen sadece Türkçe konuşan bir asistansın. Tüm cevapları sadece Türkçe olarak ver.',
  }]

#from pyngrok import ngrok

#pip install pyngrok
#Run the following command to add your authtoken to the default ngrok.yml configuration file.
#ngrok config add-authtoken 1dmTtU.....
#then run the following command to connect to the port 8501
#ngrok http 8501
#now you can access the app from the link provided by ngrok


import streamlit as st

with st.sidebar:
    "KMK Chatbot"
    model_selected = st.selectbox("Select a model", models)
    

st.title("💬 KMK Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Ollama "+ model_selected)
st.write("This is a chatbot that uses the Ollama API to generate responses to user input. You can select another model from the sidebar.")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not model_selected:
        st.info("Please select a model to continue.")
        st.stop()

    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    #response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    response = chat(model_selected, messages= system_prompt+st.session_state.messages)
    msg = response['message']['content']
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
