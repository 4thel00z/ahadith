# ahadith

![hadith.json.png](https://raw.githubusercontent.com/4thel00z/logos/master/hadith.json.png)

## Motivation

A little python library to consume [hadith.json](https://github.com/4thel00z/hadith.json).

## Installation

```
pip install ahadith
```

## Usage
### Get bukhari book by id

```python
from ahadith import bukhari

book = bukhari(1)
first_hadith = book[0]
print(first_hadith)
```

## License

This project is licensed under the GPL-3 license.
