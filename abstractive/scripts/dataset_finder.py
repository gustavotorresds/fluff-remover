import os

DIR = '../../fluffed_data/news/fluffed'

str_lookup = input('What are you looking for? ')

for f in os.listdir(DIR):
	file_path = os.path.join(DIR, f)
	with open(file_path, 'rb') as text:
		content = text.read().decode('ascii')
		if str_lookup in content.lower():
			print(content)

			if input('is this what you want? (y/n) ') == 'y':
				break
