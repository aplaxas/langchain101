import os
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

#@markdown https://platform.openai.com/account/api-keys
OPENAI_API_KEY = "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" #@param {type:"string"}

#@markdown https://huggingface.co/settings/tokens
HUGGINGFACEHUB_API_TOKEN = "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" #@param {type:"string"}

#@markdown https://serpapi.com/manage-api-key
SERPAPI_API_KEY = "4d8dc6313b5a5bea6962281a3c3e5de4698a995e90e6870e4bcf1ae64afc5546" #@param {type:"string"}

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
os.environ["SERPAPI_API_KEY"] = SERPAPI_API_KEY


def response(message, chat_hitory):   
  chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.9)
  sys = SystemMessage(content="You are an my best friend.")
  msg = HumanMessage(content=message)
  aimsg = chat([sys, msg])

  response = aimsg.content

  print(response)

  bot_message = aimsg.content
  chat_hitory.append((message, bot_message))

  return '', chat_hitory


with gr.Blocks() as demo:
  chatbot = gr.Chatbot(label="Chatbot")
  msg = gr.Textbox(label="Input", placeholder="Type your message here")
  clear = gr.Button(label="Clear chat history")
  msg.submit(response, [msg, chatbot], [msg, chatbot])
  clear.click(lambda: None, None, chatbot, queue=False)

demo.launch(debug=True, share=True)
  