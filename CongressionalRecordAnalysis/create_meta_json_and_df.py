import json
import os

import numpy as np
import pandas as pd

from dec2vec_utils import get_model

groups = [
	# {
	# 	'speakers': '100_speakers.json',
	# 	'speech_map': '100_speech_to_speaker.json',
	# 	'model': 'Doc2Vec(doctypes-100thmin50_dbow+w_d300_n5_w15_mc15_s1e-05_t2)',
	# 	'meta_name': 'meta_100thmin50_dbow+w_d300_n5_w15_mc15_s1e-05_t2.json',
	# 	'df_name': '100thmin50_dbow+w_d300_n5_w15_mc15_s1e-05_t2.h5',
	# 	'min_len': 50
	# }
	# {
	# 	'speakers': '100_speakers.json',
	# 	'speech_map': '100_speech_to_speaker.json',
	# 	'model': 'Doc2Vec(100thmin100_dbow+w_d300_n5_w15_mc15_s1e-05_t2)',
	# 	'meta_name': 'meta_100thmin100_dbow+w_d300_n5_w15_mc15_s1e-05_t2.json',
	# 	'df_name': '100thmin100_dbow+w_d300_n5_w15_mc15_s1e-05_t2.h5',
	# 	'min_len': 100
	# }
	{
		'speakers': '114_speakers.json',
		'speech_map': '114_speech_to_speaker.json',
		'model': 'Doc2Vec(114thmin100_dbow+w_d300_n5_w15_mc15_s1e-05_t4)',
		'meta_name': 'meta_114thmin100_dbow+w_d300_n5_w15_mc15_s1e-05_t4.json',
		'df_name': '114thmin100_dbow+w_d300_n5_w15_mc15_s1e-05_t4.h5',
		'min_len': 100
	}
]

if __name__ == '__main__':
	for group in groups:
		speakers = {}
		with open(os.path.join('congress_jsons', group['speakers'])) as speakers_json:
			speakers = json.loads(speakers_json.read())
		speech_map = {}
		with open(os.path.join('congress_jsons', group['speech_map'])) as s_m_json:
			speech_map = json.loads(s_m_json.read())
		model = get_model('models/' + group['model'])
		for speaker in speakers:
			speakers[speaker]['text_vecs'] = []
		doc_tags = model.docvecs.doctags.keys()

		unpaired_texts = 0
		for tag in doc_tags:
			text_vec = model.docvecs[tag]
			try:
				speakers[speech_map[tag]]['text_vecs'].append(text_vec.tolist())
			except Exception as e:
				unpaired_texts = unpaired_texts + 1
				#print(e, "{} was not said by a listed speaker.".format(tag))
		print("{} of {} texts unpaired".format(unpaired_texts, len(doc_tags)))

		with open(os.path.join('meta_jsons', group['meta_name']), 'w') as w_json:
			to_save = group.copy()
			to_save['model_texts'] = len(doc_tags)
			to_save['model_texts_assigned'] = len(doc_tags) - unpaired_texts
			to_save['num_speakers'] = len(speakers)
			json.dump(to_save, w_json)

		df = pd.DataFrame(list(speakers.values()))
		df['text_vecs'] = np.array(df['text_vecs'])
		df['avg_vec'] = df.apply(
			lambda row: np.mean(row['text_vecs'], axis=0),
			axis=1
		)
		df['num_texts'] = df.apply(
			lambda row: len(row['text_vecs']),
			axis=1
		)

		df.to_hdf(os.path.join('dataframes', group['df_name']), 'df')
