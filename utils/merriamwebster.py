import itertools
import logging
import os
import re
from typing import Optional

import dotenv
import requests

from dictionary.models import Entry, Example, Tag

logger = logging.getLogger(__name__)


class ThesaurusEntry:

    def __init__(self, json_str: dict):
        try:
            json_str = json_str[0]
        except IndexError:
            pass

        try:
            json_str['meta']
        except TypeError:
            raise

        self.antonyms = list(itertools.chain.from_iterable(json_str['meta']['ants']))
        self.synonyms = list(itertools.chain.from_iterable(json_str['meta']['syns']))
        self.offensive: bool = json_str['meta']['offensive']
        self.definitions: list = json_str["shortdef"]
        self.example: str = self.__parse_example(json_str)

    def __parse_example(self, json_str: dict) -> Optional[str]:
        try:
            raw = json_str['def'][0]['sseq'][0][0][1]['dt'][1][1][0]['t']
            return re.sub(r'{/[a-z]*}', '',
                          re.sub(r'{[a-z]*}', '', raw))
        except IndexError:
            return None


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


def load(entry: Entry):
    try:
        data = lookup(entry.word)
    except TypeError:
        logger.debug("Word not in thesaurus")
        return None

    if data.antonyms:
        antonyms = Entry.objects.filter(word__in=data.antonyms).values_list('id', flat=True)
        entry.antonyms.set(antonyms)

    if data.synonyms:
        synonyms = Entry.objects.filter(word__in=data.synonyms).values_list('id', flat=True)
        entry.synonyms.set(synonyms)

    if data.offensive:
        offensive_tag = Tag.objects.get(value="offensive")
        entry.tags.set(offensive_tag.id)

    if data.example:
        Example.objects.create(text=data.example, entry=entry)

    if data.definitions:
        data.definitions.insert(0, entry.definition)
        entry.definition = ";".join(data.definitions)

        entry.save()
