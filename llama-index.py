from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('PATH_TO_DIRECTORY').load_data()