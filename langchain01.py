import os
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# @markdown https://platform.openai.com/account/api-keys
# @param {type:"string"}
OPENAI_API_KEY = "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"

# @markdown https://huggingface.co/settings/tokens
# @param {type:"string"}
HUGGINGFACEHUB_API_TOKEN = "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"

# @markdown https://serpapi.com/manage-api-key
# @param {type:"string"}
SERPAPI_API_KEY = "4d8dc6313b5a5bea6962281a3c3e5de4698a995e90e6870e4bcf1ae64afc5546"

PINECONE_API_KEY = "d4e2ee4e-2f42-47b9-bd6b-2b3b48ac393e"

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
os.environ["SERPAPI_API_KEY"] = SERPAPI_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.9)
sys = SystemMessage(
    content="You are an expert AI providing music recommendations.")
msg = HumanMessage(
    content='Recommend me 5 rock ballads songs from the 1980s. return JSON with singer and song')

aimsg = chat([sys, msg])
print(aimsg.content)
