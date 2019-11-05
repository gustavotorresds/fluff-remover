'''
Things you might have to run every time before you run this script:
- export CLASSPATH=$HOME/Downloads/stanford-corenlp-full-2018-10-05/stanford-corenlp-3.9.2.jar
- pyrouge_set_rouge_path /Users/gustavotorres/Downloads/pyrouge-master/tools/ROUGE-1.5.5
'''

import os
from pyrouge import Rouge155

if __name__ == '__main__':
	# os.system("python make_datafiles_for_pgn/make_datafiles.py ./data ./no_split/processed")
	# os.system("python ./pointer-generator/run_summarization.py --mode=decode --data_path=./no_split/processed/finished_files/test.bin --vocab_path=./finished_files/vocab --log_root=. --exp_name=pretrained_model --max_enc_steps=400 --max_dec_steps=120 --coverage=0 --single_pass=1")

	r = Rouge155()
	r.system_dir = './data/concise'
	r.model_dir = './pretrained_model/decode_test_400maxenc_4beam_35mindec_120maxdec_ckpt-238410/decoded'
	r.system_filename_pattern = 'concise_(\d+).txt'
	r.model_filename_pattern = 'decoded_(\d+).txt'

	output = r.convert_and_evaluate()
	print(output)
	output_dict = r.output_to_dict(output)