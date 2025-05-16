from llama_index.core.settings import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index import SimpleDirectoryReader, VectorStoreIndex

# Use embeddings locais
Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Carrega os documentos
documents = SimpleDirectoryReader("./docs").load_data()

# Cria o índice
index = VectorStoreIndex.from_documents(documents)
