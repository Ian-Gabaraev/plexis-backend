import itertools
import os

import dotenv
import requests


class ThesaurusEntry:

    def __init__(self, json_str: dict):
        self.antonyms = list(itertools.chain.from_iterable(json_str[0]['meta']['ants']))
        self.synonyms = list(itertools.chain.from_iterable(json_str[0]['meta']['syns']))
        self.offensive: bool = json_str[0]['meta']['offensive']
        self.definitions: list = json_str[0]["shortdef"]
        self.example: str = json_str[0]['def'][0]['sseq'][0][0][1]['dt'][1][1][0]['t']


def generate_url(word: str) -> str:
    dotenv.load_dotenv(dotenv.find_dotenv())
    env = os.environ.get
    api_key = env('MW_THESAURUS_KEY')

    if not api_key:
        raise ValueError("API key not found in environment")

    url = "https://www.dictionaryapi.com/api/v3/" \
          "references/thesaurus/json/{}?key={}".format(word, api_key)

    return url


def lookup(word: str) -> ThesaurusEntry:
    url = generate_url(word)
    resp = requests.get(url).json()

    return ThesaurusEntry(resp)
