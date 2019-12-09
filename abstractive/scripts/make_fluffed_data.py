import os
import urllib
import urllib2
import argparse
import re
import time

parser = argparse.ArgumentParser()
parser.add_argument("--base_path", 
	default="/Users/katesalmon/Desktop/CS_230/BBC News Summary/News Articles")
parser.add_argument("--target_path",
	default="/Users/katesalmon/Desktop/CS_230/BBC News Summary/Fluffed Articles")
args = parser.parse_args()

URL = "http://www.textinflator.com/php/inflatePhpTag.php"


#Function takes in the the text file and pings the server
#Function returns the fluffed text if the ping to the
#server was successful or an error message if not
def fluff_text(text, desperation=75):
	
	#Formats the data 
	data = {"desperation" : desperation, "text" : text}
	
	#Encodes data
	encoded_data = urllib.urlencode(data)

	#Sends encoded data to serever and gets back fluffed text
	content = urllib2.urlopen(URL, encoded_data)

	stuff = content.readlines()
	stuff = " ".join(stuff)
	if stuff[-3:] != "200":
		return "Error: fluffing failed"
	return stuff[:-3]
	#return content_string[:-3] #removes random 200 at end of each piece

 #Function Loops over all of the sub directories
 #within the BBC News Summary Articles and fluffs
 #each of the text files in each directory and saves
 #them to a folder called "Fluffed_Articles" in
 #BBC News Articles  
def process_all(base_path, target_path):
	sub_directories = next(os.walk(base_path))[1]

	for sub_directory in sub_directories:
		dir_path = os.path.join(base_path, sub_directory) #establishes path
		file_names = os.listdir(dir_path)

		target_dir = os.path.join(target_path, sub_directory) #joins target path with directory

		if not os.path.exists(target_dir):
			os.mkdir(target_dir)

		# iterate through all the files
		for file_name in file_names:
			file_path = os.path.join(dir_path, file_name)
			with open(file_path) as f:
				contents = f.read()
			contents = contents.replace("\n", " ") #removes line breaks and replace them with " "
			
			#Joins lines and gets rid of non alpaha and numeric characters"
			contents = "".join([c for c in contents if c.isalnum() or c in [".", " ", ",", "?", "!"]])
			try :

				#Calls function "fluffed_text" to fluff the text
				fluffed_text = fluff_text(contents, desperation=75) 
				time.sleep(1)
				f_name = os.path.join(target_path, sub_directory, file_name)
				with open(f_name, "w+") as f2:
					result = f2.write(fluffed_text) #writes a new file with the fluffed text
			except:
				pass
		
if __name__ == "__main__":
	process_all(args.base_path, args.target_path)