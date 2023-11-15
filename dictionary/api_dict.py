import requests


class ApiDictionary:
    """Retrieve words from third part API."""

    base_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

    def get_definition(self, word: str) -> list[str]:
        """Return list of definitions of the word."""

        r = requests.get(f'{self.base_url}{word}')

        if r:
            definitions = list()

            for i in r.json():
                for j in i['meanings']:
                    for dfn in j['definitions']:
                        definitions.append(dfn['definition'])

            return definitions

        else:
            return ['Not Found... Check you word, please.']
