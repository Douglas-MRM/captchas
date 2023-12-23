from os.path import join, dirname, exists
from json import load, dumps
import os


SUCCESS = lambda msg: f'\033[92m{msg}\033[0m'
INFO    = lambda msg: f'\033[94m{msg}\033[0m'
BOLD    = lambda msg: f'\033[1m{msg}\033[0m'

FILE_KEYS = join(dirname(__file__), 'keys.json')

def load_keys() -> dict:
    if exists(FILE_KEYS):
        with open(FILE_KEYS, 'r') as f:
            return load(f)

    with open(FILE_KEYS, 'w') as f:
        f.write('{}')

    return {}

keys = load_keys()

def save_keys() -> None:
    with open(FILE_KEYS, 'w') as f:
        f.write(dumps(keys))

def add_key(key: str, value: str) -> None:
    keys[key] = value
    save_keys()

def get_key(key: str) -> str:
    if keys.get(key):
        return keys[key]

    while True:
        value = input(
            BOLD('Lib capthcas informa: ') +
            INFO('A chave %s não está configurada em nossa biblioteca!\n' % (key)) +
            BOLD('Por favor, informe a chave desta API: ')
        ).strip()

        if not value:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        add_key(key, value)
        print(SUCCESS(f'A chave {key} foi configurada com sucesso!'))
        break

    return keys[key]
