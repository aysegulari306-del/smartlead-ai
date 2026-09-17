import requests
from flask import current_app


class AIServiceError(Exception):
    """Yapay zeka servisi ile ilgili hatalar için özel istisna sınıfı"""
    pass


class AIService:
    def __init__(self):
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama-3.1-8b-instant"

    def _sistem_talimati(self):
        return current_app.config['BUSINESS_CONTEXT']

    def yanit_uret(self, mesaj, gecmis=None):
        api_key = current_app.config['GROQ_API_KEY']

        if not api_key:
            return "Demo modu: Şu an yapay zekâ servisine bağlı değilim, ama size normalde AKTİS koleksiyonları hakkında yardımcı olurdum. Lütfen GROQ_API_KEY ayarlayın."

        messages = [{"role": "system", "content": self._sistem_talimati()}]
        if gecmis:
            messages.extend(gecmis)
        messages.append({"role": "user", "content": mesaj})

        try:
            response = requests.post(
                self.api_url,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": messages,
                    "temperature": 0.7
                },
                timeout=15
            )
            response.raise_for_status()
            data = response.json()
            return data['choices'][0]['message']['content']

        except requests.exceptions.RequestException as e:
            raise AIServiceError(f"Yapay zeka servisine ulaşılamadı: {str(e)}")
        except (KeyError, IndexError) as e:
            raise AIServiceError(f"Yapay zeka yanıtı işlenemedi: {str(e)}")


ai_service = AIService()
