import requests
import logging
from models.translation import Translation
from models.base import load_model


class GptService:
    """."""
    def __init__(
        self,
        token: str,
        folder_id: str,
        api_url: str,
    ):
        self._token = token
        self._folder_id = folder_id
        self._api_url = api_url
        self._logger = logging.Logger('GPT')

    def _request_generation(self, prompt: str) -> dict:
        body = {
            "modelUri": f"gpt://{self._folder_id}/yandexgpt-lite/latest",
            "completionOptions": {
                "maxTokens": 500,
            },
            "messages": [
                {
                    "role": "user",
                    "text": prompt,
                },
            ]
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self._token}',
        }

        response = requests.post(
            url=self._api_url,
            json=body,
            headers=headers,
            timeout=5,
        )

        if not response.ok:
            self._logger.error(
                f'Unable to generate text, code={response.status_code}'
            )
            raise RuntimeError('Unable to generate')

        return response.json()

    def get_generated_text(self, prompt: str) -> dict:
        response = self._request_generation(prompt)
        single_result = response.get('result').get('alternatives')[0]

        return single_result.get('message').get('text')
