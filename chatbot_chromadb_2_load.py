from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader, UnstructuredPDFLoader
from langchain.document_loaders import DirectoryLoader

with open('api_key.txt', 'r') as f:
    OPENAI_API_KEY = f.readline().split('=')[1].strip()
    HUGGINGFACEHUB_API_TOKEN = f.readline().split('=')[1].strip()
    SERPAPI_API_KEY = f.readline().split('=')[1].strip()
    PINECONE_API_KEY = f.readline().split('=')[1].strip()

embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

persist_directory = 'db'
vectordb = Chroma(persist_directory=persist_directory,embedding_function=embedding)

retriever = vectordb.as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(openai_api_key=OPENAI_API_KEY),
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True)


def process_llm_response(llm_response):
    print(llm_response['result'])
    print('\n\nSources:')
    for source in llm_response["source_documents"]:
        print(source.metadata['source'])

query = "which model is loggest overall length?"
llm_response = qa_chain(query)
process_llm_response(llm_response)
