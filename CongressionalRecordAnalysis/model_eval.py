from create_models import get_corpus
from doc2vec_utils import get_model
from doc2vec_utils import get_most_similar

model_source_minlen = [
	[
		'Doc2Vec(doctypes-100thmin50_dbow+w_d300_n5_w15_mc15_s1e-05_t2)',
		['speeches_100.txt'],
		50
	]
]

if __name__ == '__main__':
	path_to_files = '../CongressionalRecordData/hein-daily/hein-daily/'

	for triple in model_source_minlen:
		corpus = get_corpus(path_to_files, triple[1], triple[2])
		success = 0
		
