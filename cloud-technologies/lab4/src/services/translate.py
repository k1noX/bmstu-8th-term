import requests
import logging
from models.translation import Translation
from models.base import load_model


class TranslationService:
    """."""
    def __init__(
        self,
        token: str,
        folder_id: str,
        target_language: str,
        api_url: str,
    ):
        self._token = token
        self._folder_id = folder_id
        self._target_language = target_language
        self._api_url = api_url
        self._logger = logging.Logger('Translate')

    def _request_translate(self, text: str) -> dict:
        body = {
            'targetLanguageCode': self._target_language,
            'folderId': self._folder_id,
            'texts': text,
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
            raise RuntimeError('Unable to translate')

        return response.json()

    def get_translations(self, text: str) -> list[Translation]:
        raw_translations = self._request_translate(text).get('translations')

        return [load_model(Translation, x) for x in raw_translations]

    def get_translation(self, text: str) -> Translation:
        return self.get_translations(text)[0].get('text')
