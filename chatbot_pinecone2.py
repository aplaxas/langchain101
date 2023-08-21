from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader, UnstructuredPDFLoader
from langchain.document_loaders import DirectoryLoader

# https://colab.research.google.com/drive/1MlrF0Mo8KHrxcrAeulCP3t9hroc073YN?usp=sharing#scrollTo=3__nT0D4Fkmg

loader = DirectoryLoader('./tesla', glob="*.pdf",
                         loader_cls=UnstructuredPDFLoader)

documents = loader.load()

print(len(documents))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

print(len(texts))

OPENAI_API_KEY = "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"
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

persist_directory = 'db'

vectordb = Chroma.from_documents(
    documents=texts,
    embedding=embedding,
    persist_directory=persist_directory)

print("Saved")

vectordb.persist()
vectordb = None

print("persist")
