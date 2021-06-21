import requests
import json  
import hashlib

#1
class MyIterator:
    def __init__(self, url, file_one):
        self.url = url
        self.file_one = file_one
    
    def making_links(self):
        with open(self.file_one, 'w') as file:
            data = requests.get(self.url, stream=True)
            new_data =  data.json()
            for key in new_data:
                country_name = key['name']['official']
                wiki_country_link = f'https://en.wikipedia.org/wiki/{country_name}'
                line = f'{country_name} — {wiki_country_link}\n'
                file.write(line) 
                
        
# MyIterator('https://raw.githubusercontent.com/mledoze/countries/master/countries.json', 'countries_links.txt').making_links()


#2

def MyGenerator(file_path):
    with open(file_path) as file:
        for line in file:
            hash_line = hashlib.md5(line.encode)
            yield hash_line.hexdigest()

for line in MyGenerator('countries_links.txt'):
    print(line)
  
            