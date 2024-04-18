from wrappers.cli import CliWrapper
from services.translate import TranslationService
from services.gpt import GptService
import sys


if __name__ == '__main__':
    cli_wrapper = CliWrapper()
    config = cli_wrapper.parse_config(sys.argv[1:])

    gpt_service = GptService(
        token=config['token'],
        folder_id=config['folder_id'],
        api_url=config['gpt_api_url']
    )

    print(f'[GPT] Started generation for prompt {config["prompt"]}...')
    text = gpt_service.get_generated_text(config['prompt'])
    print('[GPT] Text was successfully generated:', text)

    translations_service = TranslationService(
        token=config['token'],
        target_language=config['target_language'],
        folder_id=config['folder_id'],
        api_url=config['translations_api_url']
    )

    print(
        f'[Translation] Started translation to {config["target_language"]}',
        'for generated text...'
    )
    translation = translations_service.get_translation(text)
    print('[Translation] Text was successfully translated:', translation)
