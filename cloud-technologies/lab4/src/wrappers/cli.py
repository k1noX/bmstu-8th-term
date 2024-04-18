import argparse
import copy
from models.config import default_config, Config


class CliWrapper:
    def _init_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            description='Yandex Cloud Translations API'
        )

        parser.add_argument('prompt', type=str)
        parser.add_argument('--token', type=str, required=False)
        parser.add_argument('--folder_id', type=str, required=False)
        parser.add_argument('--target_language', type=str, required=False)

        return parser

    def __init__(self):
        self._parser = self._init_parser()

    def parse_config(self, data: str | list[str]) -> Config:
        raw_config = vars(self._parser.parse_args(data))

        config = copy.deepcopy(default_config)

        if token := raw_config.get('token'):
            config['token'] = token

        if folder_id := raw_config.get('folder_id'):
            config['folder_id'] = folder_id

        if target_language := raw_config.get('target_language'):
            config['target_language'] = target_language

        config['prompt'] = raw_config.get('prompt')

        return config
