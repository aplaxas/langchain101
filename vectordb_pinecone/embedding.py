import commonHelp
from langchain.vectorstores import Pinecone

index_name = "docqa"
folder = "./data/esg/"
tag = "ESG"

index = commonHelp.getPinecone()
embeddings = commonHelp.getEmbeddings()

# file = "Tesla_Model_3.pdf"
# commonHelp.embedding(folder, file, index_name, embeddings, tag)


# file = "Tesla_Model_S.pdf"
# commonHelp.embedding(folder, file, index_name, embeddings, tag)


# file = "Tesla_Model_X.pdf"
# commonHelp.embedding(folder, file, index_name, embeddings, tag)


# file = "Tesla_Model_Y.pdf"
# commonHelp.embedding(folder, file, index_name, embeddings, tag)

# file = "audi-e-tron-5.pdf"
# commonHelp.embedding(folder, file, index_name, embeddings, tag)

# file = "EQS SUV Owners Manual.pdf"
# commonHelp.embedding(folder, file, index_name, embeddings, tag)

# file = "kia-ev6-owners-manual-my22.pdf"
# commonHelp.embedding(folder, file, index_name, embeddings, tag)

# file = "Kona-EV-Owner's-Manual.pdf"
# commonHelp.embedding(folder, file, index_name, embeddings, tag)

file = "fxnesg.pdf"
commonHelp.embedding(folder, file, index_name, embeddings, tag)
