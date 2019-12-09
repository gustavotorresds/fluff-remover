import os


def pad(orig_str, target_len=11):
	to_pad = target_len - len(orig_str)
	result = ''.join(to_pad * ['0']) + orig_str
	return result

sub_dirs = ['business', 'entertainment', 'politics', 'sport', 'tech']

i = 0

for sub_dir in sub_dirs:
	orig_directory1 = os.path.join('./', 'concise' , sub_dir)
	orig_directory2 = os.path.join('./', 'fluffed' , sub_dir)

	new_directory1 = os.path.join('./', 'concise')
	new_directory2 = os.path.join('./', 'fluffed')

	orig_files = os.listdir(orig_directory1)

	for orig_file in orig_files:
		src1 = os.path.join(orig_directory1, orig_file)
		src2 = os.path.join(orig_directory2, orig_file)

		new_filename = str(i) + '.txt'
		new_filename = pad(new_filename)

		dest1 = os.path.join(new_directory1, new_filename)
		dest2 = os.path.join(new_directory2, new_filename)
		
		os.rename(src1, dest1)
		os.rename(src2, dest2)

		i += 1

	os.rmdir(orig_directory1)
	os.rmdir(orig_directory2)
