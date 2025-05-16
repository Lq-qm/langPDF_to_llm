# --- CLASSE CUSTOMIZADA PARA USAR OPENROUTER COMO LLM ---
class OpenRouterLLM(LLM):
    def complete(self, prompt: str, **kwargs) -> CompletionResponse:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
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