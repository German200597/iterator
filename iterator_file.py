import json
import hashlib


class CountryLinks:

	WIKI_URL = 'https://en.wikipedia.org/wiki/'

	def __init__(self, countries_file_path: str):
		with open(countries_file_path) as file:
			countries_data = json.load(file)
			country_names = (country['name']['official'] for country in countries_data)  # генератор возвращающий
			                                                                           # имена стран
			self.countries_names_iter = iter(country_names)  # итератор по именам стран

	def __iter__(self):
		return self

	def make_link(self, country_name: str):
		country_name = country_name.replace(' ', '_')
		return f'{self.WIKI_URL}{country_name}'

	def __next__(self):
		country_name = next(self.country_names_iter)                               
		return f'{country_name} - {self.make_link(country_name)}'


def get_hash(path: str):
	with open(path, 'rb') as file:
		for line in file:
			yield hashlib.md5(line).hexdigest()


if __name__ == '__main__':
	with open('country_names.txt', 'w') as country_names_file:
		for country_link in CountryLinks('countries.json'): 
			country_names_file.write(f'{country_link}\n')  
	for hash_string in get_hash('country_names.txt'):
		print(hash_string)
  
            