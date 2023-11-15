import requests
import json


class ApiDictionary:
    """Retrieve words from third part API."""

    base_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

    def get_definition(self, word: str) -> list[str]:
        """Return list of definitions of the word."""

        r = requests.get(f'{self.base_url}{word}')

        definitions = list()

        for i in json.loads(r.text):
            for j in i['meanings']:
                for dfn in j['definitions']:
                    definitions.append(dfn['definition'])

        return definitions


# word = 'phone'
# dfs = ApiDictionary().get_definition(word)
# print(type(dfs))
