import requests
from llama_index import SimpleDirectoryReader, GPTListIndex
from llama_index.llms.base import LLMMetadata, CompletionResponse
from llama_index.llms.base import LLM
from typing import Optional

# --- CONFIGURAÇÃO DA API DO OPENROUTER ---
OPENROUTER_API_KEY = "your-api-key-here"
MODEL = "openrouter/mistral-7b"  # ou outro modelo suportado
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# --- LEITURA DO DOCUMENTO E GERAÇÃO DE RESUMO ---
documents = SimpleDirectoryReader("./docs").load_data()
llm = OpenRouterLLM()
index = GPTListIndex.from_documents(documents, llm=llm)

query_engine = index.as_query_engine()
resposta = query_engine.query("Resuma esse documento em 5 parágrafos claros e objetivos.")
print(resposta)