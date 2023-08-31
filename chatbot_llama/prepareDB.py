from langchain.document_loaders import TextLoader, UnstructuredPDFLoader
from langchain.document_loaders import DirectoryLoader


with open('./api_key.txt', 'r') as f:
    OPENAI_API_KEY = f.readline().split('=')[1].strip()
    HUGGINGFACEHUB_API_TOKEN = f.readline().split('=')[1].strip()
    SERPAPI_API_KEY = f.readline().split('=')[1].strip()
    PINECONE_API_KEY = f.readline().split('=')[1].strip()


print(OPENAI_API_KEY)

loader = DirectoryLoader('./tesla', glob="*.pdf", loader_cls=UnstructuredPDFLoader)
documents = loader.load()

print(len(documents))
