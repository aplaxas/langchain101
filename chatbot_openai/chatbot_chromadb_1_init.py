from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader, UnstructuredPDFLoader
from langchain.document_loaders import DirectoryLoader

# https://colab.research.google.com/drive/1MlrF0Mo8KHrxcrAeulCP3t9hroc073YN?usp=sharing#scrollTo=3__nT0D4Fkmg
# pip install langchain openai tiktoken chromadb 
# pdf
# pip install unstructured pdf2image pdfminer pdfminer.six
# pip install pdfminer.six

# read OPENAI_API_KEY, HUGGINGFACEHUB_API_TOKEN, SERPAPI_API_KEY, PINECONE_API_KEY from api_key.txt and get key only
with open('api_key.txt', 'r') as f:
    OPENAI_API_KEY = f.readline().split('=')[1].strip()
    HUGGINGFACEHUB_API_TOKEN = f.readline().split('=')[1].strip()
    SERPAPI_API_KEY = f.readline().split('=')[1].strip()
    PINECONE_API_KEY = f.readline().split('=')[1].strip()

  
print(OPENAI_API_KEY)

loader = DirectoryLoader('./tesla', glob="*.pdf", loader_cls=UnstructuredPDFLoader)
documents = loader.load()

print(len(documents))

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

print(len(texts))


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
