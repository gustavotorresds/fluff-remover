'''
export CLASSPATH=$HOME/Downloads/stanford-corenlp-full-2018-10-05/stanford-corenlp-3.9.2.jar
'''

import os

NUM_SENTENCES_PER_FILE = 5
INPUT_FOLDER = './data/fluffed'
SPLIT_FOLDER = './with_split'
RAW_SPLIT_FOLDER = os.path.join(SPLIT_FOLDER, 'splits')
PROCESSED_SPLIT_FOLDER = os.path.join(SPLIT_FOLDER, 'processed')

if __name__ == '__main__':
	for subdir, dirs, files in os.walk(INPUT_FOLDER):
		for file in files:
			file_path = os.path.join(subdir, file)

			sentences = []
				
			with open(file_path, 'r') as f:
				content = f.read()
				sentences = content.split('.')
				senteces = [sentence.strip() for sentence in sentences]

			stripped_file, extension = os.path.splitext(file)
			file_splits_folder = os.path.join(RAW_SPLIT_FOLDER, stripped_file)
			file_processed_folder = os.path.join(PROCESSED_SPLIT_FOLDER, stripped_file)

			for i in range(0, len(sentences), NUM_SENTENCES_PER_FILE):
				splitted_file = os.path.join(file_splits_folder, str(i / NUM_SENTENCES_PER_FILE) + extension)

				if not os.path.exists(os.path.dirname(splitted_file)):
					os.makedirs(os.path.dirname(splitted_file))

				with open(splitted_file, 'w') as f:
					for sentence in sentences[i:i + NUM_SENTENCES_PER_FILE]:
						f.write(sentence + ".")

			os.system("python make_datafiles_for_pgn/make_datafiles.py {} {}".format(file_splits_folder, file_processed_folder))

			os.system("python ./pointer-generator/run_summarization.py --mode=decode --data_path={}/finished_files/test.bin --vocab_path=./finished_files/vocab --log_root=. --exp_name=pretrained_model --max_enc_steps=400 --max_dec_steps=120 --coverage=0 --single_pass=1".format(file_processed_folder))

			split_files_dir = './pretrained_model/decode_test_400maxenc_4beam_35mindec_120maxdec_ckpt-238410/decoded'

			final_content = ''
			for subdir2, dirs2, files2 in os.walk(split_files_dir):
				for file2 in sorted(files2):
					with open(os.path.join(split_files_dir, file2), 'r') as f:
						partial_content = f.read()
						final_content = final_content + partial_content

			with open(os.path.join('./output/', file), 'w') as f:
				f.write(final_content)
