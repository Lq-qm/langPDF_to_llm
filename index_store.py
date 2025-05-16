from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('./').load_data()
index = VectorStoreIndex.from_documents(documents)

response = index.query('What is your name?')
print(response)