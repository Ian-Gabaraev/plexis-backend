import requests
from bs4 import BeautifulSoup


def get_sat_6000() -> list:
    url = "https://satvocabulary.us/INDEX.ASP?CATEGORY=6000LIST"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, features="html.parser")
    rows = soup.findAll("tr")
    words = []

    for row in rows:
        tds = row.findAll("td")
        word: str = tds[1].string
        definition: str = tds[2].string

        if word is not None:
            words.append(
                (word.rstrip(' '), definition.rstrip(' '))
            )

    return words
