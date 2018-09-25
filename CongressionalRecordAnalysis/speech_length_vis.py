from create_models import *

def vis_corpus

if __name__ == '__main__':
	#file_names = []
	path_to_files = '../CongressionalRecordData/hein-daily/hein-daily/'
	file_groups = {
		'100th': ['speeches_100.txt']#,
		# '106th': ['speeches_106.txt'],
		# 'HWBush': ['speeches_101.txt',
		# 			'speeches_102.txt']#,
		# 'Obama': ['speeches_111.txt',
		# 			'speeches_112.txt',
		# 			'speeches_113.txt',
		# 			'speeches_114.txt']
	} 
	min_speech_length = [
		1
	]
	for min_length in min_speech_length:
		for group_name, files in file_groups.items():
			doc_corpus = get_corpus(path_to_files, files, min_length)
			vis_corpus(doc_corpus)
