from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
import warnings
warnings.filterwarnings("ignore")

FILE_PATH = '../documents/du_lieu_cay_canh.pdf'

# Create Loader
loader = PyPDFLoader(FILE_PATH)

# Split document
pages  = loader.load_and_split()

# embedding function
embedding_function = SentenceTransformerEmbeddings(
    model_name='all-MiniLM-L6-v2'
)

# Create vector store
vectordb = Chroma.from_documents(
    documents=pages,
    embedding=embedding_function,
    persist_directory='../vector_db',
    collection_name='du_lieu_cay_canh'
)

# make persistant
vectordb.persist()