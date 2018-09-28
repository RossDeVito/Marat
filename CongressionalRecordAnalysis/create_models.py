"""Used to create and save doc2vec models.

preprocess_and_tokenize() also useful in other scripts. One example is
	to tokenize queries you are finding the most similar to, as in
	vs_testing.

Parameters are not decided on yet.
"""
import itertools
import inflect

import gensim
from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
import gensim.models.doc2vec
from gensim import utils
from gensim.parsing import preprocessing
from gensim.test.utils import get_tmpfile

from collections import OrderedDict
import multiprocessing

import time
import os
import json
import sys

def get_corpus(location, files, min_length):
	"""Opens json files representing documents from given directories and
		returns them as a list of TaggedDocument objects.

	Args:
		location: path to directory containing files in files
		files: iterable of files that contain text
		min_length: minimum word count to be included in corpus

	Returns:
		List of documents as TaggedDocument objects 

	TODO fix desc ^
	"""
	docs = []
	for file in files:
		docs.extend(
			get_speeches_from_file(os.path.join(location, file), min_length)
		)
	return docs

def get_speeches_from_file(path, min_length):
	#encoding='iso-8859-1'
	with open(path, encoding="utf8", errors='ignore') as speeches:
		next(speeches)
		for line in speeches:
			try:
				speech_id, speech_text = line.split('|')
			except:
				print('Speech improperly split')
				continue
			if (min_length <= len(speech_text.split())):
				yield TaggedDocument(
					preprocess_and_tokenize(speech_text), 
					[speech_id]
				)

def preprocess_and_tokenize(text):
	"""Preprocesses and tokenizes text.

	Numbers and ordinal alphanumerics are converted to words. 
	ex. 
		preprocess_and_tokenize("The 49ers won 1st in 2029 in Dallas-Fort
									Worth, but won't win this year!")

		returns:
			['the',
			'forty',
			'nine',
			'ers',
			'won',
			'first',
			'in',
			'two',
			'thousand',
			'and',
			'twenty',
			'nine',
			'in',
			'dallas',
			'fort',
			'worth',
			'but',
			'wont',
			'win',
			'this',
			'year']
	Args:
		text: a string to be preprocessed and tokenized

	Returns:
		List of tokens
	
	TODO:
		Make except block catch correct exception only. It is the one where a
			numeric number is too long for inflect.
	"""
	inf_eng = inflect.engine()
	text = utils.to_unicode(utils.deaccent(text)).replace("'", "").replace('–', '')
	tokens =  preprocessing.preprocess_string(
				text, 
				[lambda x: x.lower(),
					preprocessing.strip_punctuation, 
					preprocessing.strip_multiple_whitespaces
				])
	try:
		tokens = [inf_eng.number_to_words(token) if (
					token.isdigit() 
					or (len(token) > 2 
						and token[-2:] in ['st', 'nd', 'rd', 'th']
						and token[:-2].isdigit())) 
				else token 
				for token in tokens]
	except:
		#print("E1:\t{}".format(sys.exc_info()[0]))
		pass
	tokens =  preprocessing.preprocess_string(
				' '.join(tokens), 
				[lambda x: x.lower(),
					preprocessing.strip_punctuation, 
					preprocessing.strip_multiple_whitespaces,
					preprocessing.split_alphanum
				])
	try:
		tokens = [inf_eng.number_to_words(token) if token.isdigit()
				else token 
				for token in tokens]
	except:
		#print("E2:\t{}".format(sys.exc_info()[0]))
		pass
	tokens =  preprocessing.preprocess_string(
				' '.join(tokens), 
				[lambda x: x.lower(),
					preprocessing.strip_punctuation, 
					preprocessing.strip_multiple_whitespaces,
					preprocessing.strip_numeric
				])
	return [token for token in tokens if token.isalpha() and token != 's']

def setup_models(corpus, group_name, model_selection=0):
	'''model_selection=0 all
	model_selection=1 short
	model_selection=2 long

	TODO:
		Not worth cleaning up at the moment since changing which models
			to use
	'''
	cores = multiprocessing.cpu_count()
	assert gensim.models.doc2vec.FAST_VERSION > -1, "This will be painfully slow otherwise"

	#called base models because full list of models will also include ConcatenatedDoc2Vec 
	#models using combinations of these base models
	base_models = []
	if model_selection == 0 or model_selection == 1:
		base_models += [
			#PV-DBOW - distributed bag of words training algorithm
			#1 from https://arxiv.org/pdf/1607.05368.pdf
			#beacause each piece of text will appear three times (as part of its full text,
			#section, and paragraph) min counts multiplied by three where >1 for this paper
			Doc2Vec(vector_size=300, 
					window=15, 
					min_count=15,
					sample=1e-5, 
					workers=cores, 
					hs=0, 
					dm=0, 
					negative=5,
					dbow_words=1,
					epochs=20,
					comment='{}'.format(group_name)),
			# #DBOW with smaller vector, higher min word count, smaller window, higher epochs
			# Doc2Vec(vector_size=100, 
			# 		window=5, 
			# 		min_count=50,
			# 		sample=1e-5, 
			# 		workers=cores, 
			# 		hs=0, 
			# 		dm=0, 
			# 		negative=5,
			# 		dbow_words=1,
			# 		epochs=100,
			# 		comment='doctypes-{}'.format(group_name)),
			# #DBOW from https://groups.google.com/forum/#!topic/gensim/QuVMR8yso4s
			# Doc2Vec(dm=0, 
			# 		dbow_words=1, 
			# 		vector_size=200, 
			# 		window=8, 
			# 		min_count=20,
			# 		sample=1e-5,
			# 		epochs=20, 
			# 		workers=cores,
			# 		hs=0,
			# 		negative=5,
			# 		comment='doctypes-{}'.format(group_name))
		]
	if model_selection == 0 or model_selection == 2:
		base_models += [
			#2,3,4 from https://arxiv.org/pdf/1607.05368.pdf
			Doc2Vec(vector_size=300, 
					window=15, 
					min_count=1,
					sample=1e-5, 
					workers=cores, 
					hs=0, 
					dm=0, 
					negative=5,
					dbow_words=1,
					epochs=400,
					comment='doctypes-{}'.format(group_name)),
			Doc2Vec(dm=1, 
					dm_mean=1, 
					vector_size=300, 
					window=5, 
					negative=15, 
					hs=0, 
					min_count=5,
					sample=1e-6, 
					workers=cores,
					epochs=600,
					comment='doctypes-{}'.format(group_name)),
			Doc2Vec(dm=1, 
					dm_mean=1, 
					vector_size=300, 
					window=5, 
					negative=5, 
					hs=0, 
					min_count=1,
					sample=1e-6, 
					workers=cores,
					epochs=1000,
					comment='doctypes-{}'.format(group_name))
		]
	if model_selection == 0 or model_selection == 3:
		base_models += [
			#best of round 1
			Doc2Vec(vector_size=300, 
					window=15, 
					min_count=15,
					sample=1e-5, 
					workers=cores, 
					hs=0, 
					dm=0, 
					negative=5,
					dbow_words=1,
					epochs=20,
					comment='doctypes-{}'.format(group_name)),
			#best of round 1, but 10 more epochs
			Doc2Vec(vector_size=300, 
					window=15, 
					min_count=15,
					sample=1e-5, 
					workers=cores, 
					hs=0, 
					dm=0, 
					negative=5,
					dbow_words=1,
					epochs=20,
					comment='doctypes-{}'.format(group_name)),
			#DBOW with smaller vector, higher min word count, smaller window, higher epochs
			Doc2Vec(vector_size=100, 
					window=15, 
					min_count=50,
					sample=1e-5, 
					workers=cores, 
					hs=0, 
					dm=0, 
					negative=5,
					dbow_words=1,
					epochs=20,
					comment='doctypes-{}'.format(group_name)),
			#best of round 1, but smaller window
			Doc2Vec(vector_size=300, 
					window=8, 
					min_count=15,
					sample=1e-5, 
					workers=cores, 
					hs=0, 
					dm=0, 
					negative=5,
					dbow_words=1,
					epochs=20,
					comment='doctypes-{}'.format(group_name)),
		]

	for model in base_models:
		build_vocab_start_time = time.time()
		print("Building vocab for model {}".format(str(model)))
		model.build_vocab(corpus)
		print("\tTrained in {} s".format(time.time() - build_vocab_start_time))

	return base_models

def train_models(models, corpus):
	"""Trains given models on given corpus and saves trained model as a file."""
	file_names = []
	print("{} models to train".format(len(models)))
	for model in models:
		print("\tStarting training of model {}".format(str(model)))
		training_start_time = time.time()
		model.train(corpus, 
					total_examples=len(corpus), 
					epochs=model.epochs)
		print("\t\ttrained in {} s".format(time.time()-training_start_time))
		file_name = str(model).replace('"', '').replace('/', '').replace(',', '_')
		model.save(file_name)
		file_names.append(file_name)
		print("\t\tmodel saved")
	return file_names

if __name__ == '__main__':
	file_names = []
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
		# 1,
		# 30,
		#50,
		 100
	]
	for min_length in min_speech_length:
		for group_name, files in file_groups.items():
			doc_corpus = get_corpus(path_to_files, files, min_length)
			base_models = setup_models(
				doc_corpus, 
				group_name + 'min{}'.format(str(min_length)), 
				1
			)
			file_names.extend(train_models(base_models, doc_corpus))

	print(file_names)
		

