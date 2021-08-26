 requests
 dataclasses  dataclass
 typing  List

dataclass
 Hadith:
    arabic: str
    english: str
    reference: str

        __str__(self):
               "\n".join((self.english,self.arabic,self.reference))

bukhari(i: int) -> List[Hadith]:
    res  requests.get(f"https://raw.githubusercontent.com/4thel00z/hadith.json/master/bukhari/bukhari_{i}.json")
    res.raise_for_status()
    return [Hadith(**h)  h   res.json()]
