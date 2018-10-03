import json

import numpy as np

from dec2vec_utils import get_model

groups = [
	{
		'speakers': '100_speakers.json',
		'speech_map': '100_speech_to_speaker.json',
		'model': 'Doc2Vec(doctypes-100thmin50_dbow+w_d300_n5_w15_mc15_s1e-05_t2)',
		'out_name': 'filled_100thmin50_dbow+w_d300_n5_w15_mc15_s1e-05_t2.json'
	}
]

if __name__ == '__main__':
	for group in groups:
		speakers = {}
		with open(group['speakers']) as speakers_json:
			speakers = json.loads(speakers_json.read())
		speech_map = {}
		with open(group['speech_map']) as s_m_json:
			speech_map = json.loads(s_m_json.read())
		model = get_model(group['model'])
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
		
		with open(group['out_name'], 'w') as w_json:
			to_save = group.copy()
			to_save['data'] = list(speakers.values())
			json.dump(to_save, w_json)