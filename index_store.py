from llama_index.core.settings import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# Carrega os documentos
documents = SimpleDirectoryReader("./docs").load_data()

# Cria o índice
index = VectorStoreIndex.from_documents(documents)