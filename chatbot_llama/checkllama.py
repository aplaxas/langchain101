import requests
import os
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from huggingface_hub import InferenceClient

# https://python.langchain.com/docs/integrations/llms/huggingface_hub

HUGGINGFACEHUB_API_TOKEN = "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"

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

print(HUGGINGFACEHUB_API_TOKEN)


question = "Who won the FIFA World Cup in the year 1994? "
template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

repo_id = "meta-llama/Llama-2-7b-chat-hf" 

llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
)
llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.run(question))
