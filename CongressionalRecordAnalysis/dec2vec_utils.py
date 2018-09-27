import json
import string
import math
import itertools
import time

import numpy as np
import pandas as pd

import gensim
from gensim.models import Doc2Vec
import gensim.models.doc2vec

from create_models import preprocess_and_tokenize

def get_model(filename):
	"""Loads a saved gensim doc2vec model from file and removes training data.
	
	Args:
		filename: path to or file that is saved gensim doc2vec model

	Returns:
		doc2vec model that can no longer be trained, but which can be used 
			in similarity searches and to infer new vectors from text with
			infer_vector()
	"""
	model = Doc2Vec.load(filename)
	model.delete_temporary_training_data(
		keep_doctags_vectors=True, 
		keep_inference=True)
	return model

def load_models(model_files):
	"""Loads saved models from memory.

	Args:
		model_files: List of lists which represent a model to load in
			the format [filename, doc_type, model_type]

	Returns:
		List of lists in which each list is formatted:
			[gensim.models.doc2vec.Doc2Vec object, 
				filename, 
				doc_type, 
				model_type]
	"""
	models = []
	for row in model_files:
		model = get_model(row[0])
		models.append([model] + row)
	return models

def std_filename(filename):
	"""Removes punctuation and capitals from filenames for better comparison.

	Needed because some original filenames ha to be modified for compatibility
	with different file systems.

	Args:
		filename: filename whose extension or suffix has already been removed

	Returns:
		Stripped and lowered filename.
	"""
	translator = str.maketrans('','',string.punctuation)
	return filename.translate(translator).lower()

def vectorize_query(model, query):
	"""Infers a vector for a query based on model.

	Query is preprocessed and tokenized by preprocess_and_tokenize()
		from create_models.py
	
	Args:
		model: trained gensim doc2vec model
		query: text query

	Returns:
		Vector representation of query
	"""
	tokens = preprocess_and_tokenize(query)
	return model.infer_vector(tokens)

def get_most_similar(model, query, topn=10):
	"""Finds topn most similar documents to query that model was trained on.

	Args:
		model: trained gensim doc2vec model
		query: text query
		topn: number of top-n similar docvecs to return

	Returns:
		Sequence of (doctag, similarity)
	"""
	return model.docvecs.most_similar([vectorize_query(model, query)], topn=topn)

def is_word_in_file(word, path):
	with open(path, 'r') as open_file:
		text = json.load(open_file)['doc_text']
		return word.lower() in text.lower()

def first_true_index(row, field):
	for i, value in enumerate(row[field]):
		if value:
			return i
	return None


if __name__ == '__main__':
	models = load_models(model_files)
	questions = get_relevant_questions(models[0][0], qa_files)
	evaluated_models = [evaluate_model(m, questions, 25, 5) for m in models]
	plot_scores(evaluated_models)
	df_c=make_curves(evaluated_models)
