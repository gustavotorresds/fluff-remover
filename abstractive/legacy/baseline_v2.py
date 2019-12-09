'''
Things you might have to run every time before you run this script:
- export CLASSPATH=$HOME/Downloads/stanford-corenlp-full-2018-10-05/stanford-corenlp-3.9.2.jar
- pyrouge_set_rouge_path /Users/gustavotorres/Downloads/pyrouge-master/tools/ROUGE-1.5.5

V2 of Baseline Model for Fluff Remover.
1. Converts .txt input to .bin
2. Runs Pointer Generator pretrained model over .bin files to obtain summaries of each file
3. Outputs ROUGE of generated summaries
'''

import os
from pyrouge import Rouge155

INPUT_DATA = './data/fluffed'
PROCESSED_DATA = './no_split/processed'

if __name__ == '__main__':
	os.system("python make_datafiles_for_pgn/make_datafiles.py {} {}".format(INPUT_DATA, PROCESSED_DATA))
	os.system("python ./pointer-generator/run_summarization.py --mode=decode --data_path={}/finished_files/test.bin --vocab_path=./finished_files/vocab --log_root=. --exp_name=pretrained_model --max_enc_steps=400 --max_dec_steps=120 --coverage=0 --single_pass=1".format(PROCESSED_DATA))

	r = Rouge155()
	r.system_dir = './data/concise'
	r.model_dir = './pretrained_model/decode_test_400maxenc_4beam_35mindec_120maxdec_ckpt-238410/decoded'
	r.system_filename_pattern = '(\d+)_concise.txt'
	r.model_filename_pattern = '(\d+)_decoded.txt'

	output = r.convert_and_evaluate()
	print(output)