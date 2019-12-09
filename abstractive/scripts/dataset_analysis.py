import os

running_sum = 0
max_len = 0
min_len = 1000

longest = 0

DIR = '../fluffed_data/news/fluffed'

for f in os.listdir(DIR):
	file_path = os.path.join(DIR, f)
	with open(file_path, 'rb') as text:
		content = text.read()
		content_len = len(content.split())
		running_sum += content_len
		if content_len > max_len:
			max_len = content_len
		if content_len < min_len:
			min_len = content_len
		if content_len > 800:
			longest += 1


print("AVG: " + str(running_sum / len(os.listdir(DIR))))
print("MAX: " + str(max_len))
print("MIN: " + str(min_len))
print("L: " + str(longest))