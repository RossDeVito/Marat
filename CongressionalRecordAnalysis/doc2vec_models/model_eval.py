from create_models import get_corpus
from dec2vec_utils import get_model
from dec2vec_utils import get_most_similar

model_source_minlen = [
	[
		'models/Doc2Vec(100thmin25_dbow+w_d300_n5_w15_mc15_s1e-05_t4)',
		['speeches_100.txt'],
		25
	]
]

def get_most_similar_from_tokens(model, tokens, topn=1):
	"""Finds topn most similar documents to query that model was trained on.

	Args:
		model: trained gensim doc2vec model
		query: text query
		topn: number of top-n similar docvecs to return

	Returns:
		Sequence of (doctag, similarity)
	"""
	return model.docvecs.most_similar([model.infer_vector(tokens)], topn=topn)

def replicability_percision(model_file, corpus):
	model = get_model(model_file)
	docs_checked = 0
	docs_correct = 0
	similarity_correct = 0
	similarity_incorrect = 0
	for doc in corpus:
		most_similar = get_most_similar_from_tokens(model, doc.words)
		if most_similar[0][0] == doc.tags[0]:
			docs_correct += 1
			similarity_correct += most_similar[0][1]
		else:
			similarity_incorrect += most_similar[0][1]
		docs_checked += 1
	return {
		'docs_checked': docs_checked,
		'docs_correct':	docs_correct,
		'percision': (float(docs_correct)/docs_checked),
		'avg_similarity_correct': (float(similarity_correct)/docs_correct),
		'avg_similarity_incorrect': 
			(float(similarity_incorrect)/(docs_checked-docs_correct)),
		'avg_similarity': 
			(float(similarity_correct+similarity_incorrect)/docs_checked)
	}



if __name__ == '__main__':
	path_to_files = '../CongressionalRecordData/hein-daily/hein-daily/'

	for triple in model_source_minlen:
		corpus = get_corpus(path_to_files, triple[1], triple[2])
		rep_perc_stats = replicability_percision(triple[0], corpus)
		print("Replicabilty percision for model {}:")
		print(rep_perc_stats)
		
