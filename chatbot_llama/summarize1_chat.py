import os


from langchain.document_loaders import TextLoader
from langchain.chains.summarize import load_summarize_chain
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from huggingface_hub import InferenceClient

# https://python.langchain.com/docs/integrations/llms/huggingface_hub

HUGGINGFACEHUB_API_TOKEN = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

# print(HUGGINGFACEHUB_API_TOKEN)

input_filepath = "./data/calltext/dps748700319.txt"
with open(input_filepath, 'r', encoding='utf-8') as f:
    text = f.read()


template1 = """summarize problem or issues from Context with two sentences.
Context:```{text}```"""

template = """summarize problem or issues from Context .
### summary examples ###
Example 1:
Type: Software
Problem: The software is not working.
Solution: Reinstall the software.

Example 2:
Type: Hardware
Problem: The hardware is not working.
Solution: Replace the hardware.

### Context ###
Context:```{text}```"""

prompt = PromptTemplate(template=template, input_variables=["text"])

repo_id = "meta-llama/Llama-2-7b-chat-hf"
llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
)
llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.run(text))
