import requests
from dataclasses import dataclass
from typing import List

@dataclass
class Hadith:
    arabic: str
    english: str
    reference: str

    def __str__(self):
        return "\n".join((self.english,self.arabic,self.reference))

def bukhari(i: int) -> List[Hadith]:
    res = requests.get(f"https://raw.githubusercontent.com/4thel00z/hadith.json/master/bukhari/bukhari_{i}.json")
    res.raise_for_status()
    return [Hadith(**h) for h in res.json()]
