"""."""
import os
import typing as t


class Config(t.TypedDict):
    """Конфигурация для сервиса перевода Yandex Cloud"""
    token: str
    folder_id: str
    target_language: str
    translations_api_url: str
    gpt_api_url: str
    prompt: str


default_config = Config(
    token=os.environ.get('YC_TOKEN', ''),
    folder_id=os.environ.get('YC_FOLDER_ID', ''),
    target_language=os.environ.get('YC_FOLDER_ID', ''),
    translations_api_url='https://translate.api.cloud.yandex.net/translate/v2/'
                         'translate',
    gpt_api_url='https://llm.api.cloud.yandex.net/foundationModels/v1/'
                'completion',
    prompt=os.environ.get('YC_GPT_PROMPT', ''),
)
