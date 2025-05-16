import requests

# --- LEITURA DO DOCUMENTO E GERAÇÃO DE RESUMO ---
documents = SimpleDirectoryReader("./docs").load_data()
llm = OpenRouterLLM()
index = GPTListIndex.from_documents(documents, llm=llm)

query_engine = index.as_query_engine()
resposta = query_engine.query("Resuma esse documento em 5 parágrafos claros e objetivos.")
print(resposta)