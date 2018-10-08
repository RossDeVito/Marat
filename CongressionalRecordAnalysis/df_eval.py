import os

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import seaborn as sns

from sklearn import decomposition 

def plot_text_count_dist(df, upper_bound=1000000000, kde=True, bins=None):
	counts = list(df['num_texts'])
	over = [n for n in counts if n > upper_bound]
	print("Values over upper display bound of {}".format(upper_bound))
	print(over)
	under = [n for n in counts if n <= upper_bound]
	sns.distplot(under, kde=kde, bins=bins)
	plt.show()

def generate_pca(df):
	all_vecs = [vec for veclist in df['text_vecs'] for vec in veclist]
	pca = decomposition.PCA(n_components=2)
	pca.fit(all_vecs)
	return pca


if __name__ == '__main__':
	sources = ['100thmin100_dbow+w_d300_n5_w15_mc15_s1e-05_t2.h5']
	sns.set(style='darkgrid')
	for source in sources:
		df = pd.read_hdf(os.path.join('dataframes', source), 'df')
		plot_text_count_dist(df, 1000)
		plot_text_count_dist(df, 700)
		plot_text_count_dist(df, 200, kde=False)
		plot_text_count_dist(df, 20, kde=False, 
			bins=[-.5,.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5])

		df.drop(df[df['num_texts'] == 0].index, inplace=True)
		pca = generate_pca(df)
		df['avg_vec_pc'] = df.apply(
			lambda row: pca.transform([row['avg_vec']])[0],
			axis=1
		)
		df['avg_vec_pc_1'] = df.apply(
			lambda row: pca.transform([row['avg_vec']])[0][0],
			axis=1
		)
		df['avg_vec_pc_2'] = df.apply(
			lambda row: pca.transform([row['avg_vec']])[0][1],
			axis=1
		)

		ax = sns.scatterplot(x='avg_vec_pc_1', y='avg_vec_pc_2', hue='party',
			style='chamber', data=df)

		plt.show()

		by_vec_list = []
		for index, row in df.iterrows():
			for vec in row['text_vecs']:
				by_vec_list.append({
					'chamber': row['chamber'],
					'district': row['district'],
					'firstname': row['firstname'],
					'lastname': row['lastname'],
					'gender': row['gender'],
					'party': row['party'],
					'speaker_id': row['speaker_id'],
					'state': row['state'],
					'text_vec': vec,
				})
		df_bv = pd.DataFrame(by_vec_list)

		df_bv['vec_pc'] = df_bv.apply(
			lambda row: pca.transform([row['text_vec']])[0],
			axis=1
		)
		df_bv['vec_pc_1'] = df_bv.apply(
			lambda row: row['vec_pc'][0],
			axis=1
		)
		df_bv['vec_pc_2'] = df_bv.apply(
			lambda row: row['vec_pc'][1],
			axis=1
		)

		ax = sns.scatterplot(x='vec_pc_1', y='vec_pc_2', hue='party',
			style='chamber', data=df_bv)

		plt.show()





	