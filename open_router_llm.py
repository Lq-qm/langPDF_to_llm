# --- CLASSE CUSTOMIZADA PARA USAR OPENROUTER COMO LLM ---
# --- CONFIGURAÇÃO DA API DO OPENROUTER ---
openrouter_api_txt = open('openrouter_api.txt')
openrouter_api_key = openrouter_api_txt.read()
print(f'OpenRouter API Key: {openrouter_api_key}')

MODEL = "openrouter/mistral-7b"  # ou outro modelo suportado
API_URL = "https://openrouter.ai/api/v1/chat/completions"

class OpenRouterLLM(LLM):
    def complete(self, prompt: str, **kwargs) -> CompletionResponse:
        headers = {
            "Authorization": f"Bearer {openrouter_api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        completion = response.json()["choices"][0]["message"]["content"]
        return CompletionResponse(text=completion)

    @property
    def metadata(self) -> LLMMetadata:
        return LLMMetadata(
            context_window=4096,
            num_output=512,
            is_chat_model=True,
            model_name=MODEL,
        )