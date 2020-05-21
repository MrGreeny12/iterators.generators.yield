import wikipedia
import json
from wikipedia import PageError, DisambiguationError


class Iterator():

    def __init__(self, data_file, path):
        with open(data_file, 'r', encoding='utf8') as read_file:
            self.data = json.load(read_file)
        self.file_output = open(path, 'w')
        self.countries_name = self.data
        self.count = 0
        self.max = int(len(self.data))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_c_name = self.data[self.count]['name']['official']
            response = wikipedia.search(next_c_name)
            page = wikipedia.page(response[0], auto_suggest=False).url
        except DisambiguationError:
            response[0] = response[1]
            return response[0]
        except StopIteration:
            self.file_output.close()
            raise StopIteration
        else:
            countries_info = next_c_name + ' - ' + page
            self.count += 1
            if self.count == self.max:
                raise StopIteration
        self.file_output.write(countries_info + '\n')
        return countries_info

if __name__ == '__main__':
    for item in Iterator('countries.json', 'countries_wiki_links.txt'):
        print(item)