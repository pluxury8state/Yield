from requests import get
import json
from pprint import pprint


def convert(file):
    mas = []
    for item in file:
        a = item['name']['common'].replace(' ','_')
        mas.append(a)
    return mas


class ITERATOR:

    def __init__(self, file=str):
        self.file = file
        with open(self.file) as inform:
            self.json_load = json.load(inform)
        self.countries = convert(self.json_load)
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        url = 'https://ru.wikipedia.org/wiki/'
        if self.counter == len(self.countries)-1:
            raise StopIteration
        self.counter += 1

        dictionary = {}

        dictionary['name'] = self.countries[self.counter]
        dictionary['link'] = url + self.countries[self.counter]

        return dictionary


obj = ITERATOR('countries.json')

mas = []

for items in obj:
    mas.append(items)

with open('new_links.json', 'w', encoding='utf8') as file:
    json.dump(mas, file, ensure_ascii=False, indent=2)
