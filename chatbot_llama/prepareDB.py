from langchain.document_loaders import TextLoader, UnstructuredPDFLoader
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

with open('./api_key.txt', 'r') as f:
    OPENAI_API_KEY = f.readline().split('=')[1].strip()
    HUGGINGFACEHUB_API_TOKEN = f.readline().split('=')[1].strip()
    SERPAPI_API_KEY = f.readline().split('=')[1].strip()
    PINECONE_API_KEY = f.readline().split('=')[1].strip()


print(HUGGINGFACEHUB_API_TOKEN)

loader = DirectoryLoader('./data/calltext', glob="*.txt", loader_cls=TextLoader)
documents = loader.load()

print(len(documents))

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

txtSplitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
documentChunks = txtSplitter.split_documents(documents)

print(len(documentChunks))

print(documentChunks[0])

persist_directory = './db/calltext/'
vectordb = Chroma.from_documents(
     documents=documentChunks,
     embedding=embeddings,
     persist_directory=persist_directory)
print("Saved")

vectordb.persist()
vectordb = None
print("persist")