import json
import os

# 2 data structs
#  dict of congresspeople
#  dict mapping

speaker_map_files = [
	'114_SpeakerMap.txt',
]

def create_congressperson_jsons(path, file):
	speakers = {}
	speeches = {}
	with open(os.path.join(path, file), 
				encoding="utf8", 
				errors='ignore') as persons:
		next(persons)
		for line in persons:
			#try:
			(speaker_id, speech_id, lastname, firstname, chamber, state, gender, party, 
				district, voting_status) = line.split('|')
			# except:
			# 	print('Person improperly split')
			# 	continue
			if speaker_id not in speakers.keys():
				speakers[speaker_id] = {
					'speaker_id': 	speaker_id,
					'speech_ids':	[speech_id],
					'lastname':		lastname,
					'firstname':	firstname,
					'chamber':		chamber,
					'state':		state,
					'gender':		gender,
					'party':		party,
					'district':		district
				}
			else:
				speakers[speaker_id]['speech_ids'].append(speech_id)
			speeches[speech_id] = speaker_id
	cong_num, _ = file.split('_')
	with open(os.path.join('congress_jsons', cong_num + '_speakers.json'), 
				'w') as w_json:
		#json.dump(list(speakers.values()), w_json, indent=4)
		json.dump(speakers, w_json, indent=4)
	with open(os.path.join('congress_jsons', cong_num + '_speech_to_speaker.json'), 
				'w') as w_json:
		json.dump(speeches, w_json)
			

if __name__ == '__main__':
	path_to_files = '../CongressionalRecordData/hein-daily/hein-daily/'

	for file in speaker_map_files:
		create_congressperson_jsons(path_to_files, file)
