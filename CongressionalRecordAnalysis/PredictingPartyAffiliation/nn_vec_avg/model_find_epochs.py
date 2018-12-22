import os
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import seaborn as sns

from keras.callbacks import EarlyStopping
from keras.models import Sequential
from keras.layers import Dense, Dropout

from sklearn.model_selection import train_test_split

def load_source_df():
	"""
	Loads dataframe stored as h5 from memory to speed up subsequent data()
	calls.
	"""
	source = '114thmin100_dbow+w_d300_n5_w15_mc15_s1e-05_t4.h5'
	df = pd.read_hdf(os.path.join('../..', 'dataframes', source), 'df')
	return df

def data(df):
	"""
	Data providing function.
	"""
	df = df[((df['party']=='R') | (df['party']=='D')) & (df['num_texts'] != 0)]
	df['party_bin'] = (df['party'] == 'D').astype(int) #D is 1, R is 0

	X_train, X_test, y_train, y_test = train_test_split(
		df['avg_vec'],
		df['party_bin'],
		test_size=.1,
		shuffle=True)
	X_train = np.stack(X_train.values)
	y_train = y_train.values  
	X_test = np.stack(X_test.values)
	y_test = y_test.values

	return X_train, y_train, X_test, y_test

def model_1():
	model_1 = Sequential()
	model_1.add(Dense(300, input_dim=300, activation='relu'))
	model_1.add(Dropout(.54424))
	model_1.add(Dense(512, activation='tanh'))
	model_1.add(Dropout(.43404))
	model_1.add(Dense(300, activation='relu'))
	model_1.add(Dropout(.69751))
	model_1.add(Dense(1, activation='sigmoid'))
	model_1.compile(loss='binary_crossentropy',
					optimizer='rmsprop',
					metrics=['accuracy'])
	return model_1

def model_2():
	model_2 = Sequential()
	model_2.add(Dense(300, input_dim=300, activation='tanh'))
	model_2.add(Dropout(.06570))
	model_2.add(Dense(350, activation='relu'))
	model_2.add(Dropout(.73664))
	model_2.add(Dense(512, activation='relu'))
	model_2.add(Dropout(.78715))
	model_2.add(Dense(1, activation='sigmoid'))
	model_2.compile(loss='binary_crossentropy',
					optimizer='adam',
					metrics=['accuracy'])
	return model_2

def model_3():
	model_3 = Sequential()
	model_3.add(Dense(450, input_dim=300, activation='tanh'))
	model_3.add(Dropout(.06570))
	model_3.add(Dense(550, activation='relu'))
	model_3.add(Dropout(.73664))
	model_3.add(Dense(600, activation='relu'))
	model_3.add(Dropout(.78715))
	model_3.add(Dense(1, activation='sigmoid'))
	model_3.compile(loss='binary_crossentropy',
					optimizer='adam',
					metrics=['accuracy'])
	return model_3

def model_4():
	model_4 = Sequential()
	model_4.add(Dense(600, input_dim=300, activation='relu'))
	model_4.add(Dropout(.84691))
	model_4.add(Dense(525, activation='tanh'))
	model_4.add(Dropout(.32104))
	model_4.add(Dense(575, activation='relu'))
	model_4.add(Dropout(.59487))
	model_4.add(Dense(1, activation='sigmoid'))
	model_4.compile(loss='binary_crossentropy',
					optimizer='rmsprop',
					metrics=['accuracy'])
	return model_4

if __name__ == '__main__':
	train_epochs = 40
	this_test_epochs = 100
	sns.set_style('darkgrid')

	df_acc = pd.DataFrame(
		np.nan, 
		index=np.arange(this_test_epochs*2), 
		columns=['split']+[n for n in range(1, train_epochs+1)])
	df_loss = pd.DataFrame(
		np.nan, 
		index=np.arange(this_test_epochs), 
		columns=['split']+[n for n in range(1, train_epochs+1)])

	source_df = load_source_df()

	for i in range(this_test_epochs):
		X_train, y_train, X_test, y_test = data(source_df)
		model = model_1()

		model_res = model.fit(
			X_train, 
			y_train, 
			validation_split=0.1, 
			epochs=train_epochs, 
			batch_size=16, #model 4 needs 8, else 16
			verbose=2)

		df_acc.loc[i] = ['acc'] + model_res.history['acc']
		df_acc.loc[i + this_test_epochs] = ['val_acc'] + model_res.history['val_acc']
		df_loss.loc[i] = ['loss'] + model_res.history['loss']
		df_loss.loc[i + this_test_epochs] = ['val_loss'] + model_res.history['val_loss']

	df_acc_plot_format = df_acc.copy().melt(
		id_vars=['split'],
		value_vars=[n for n in range(1, train_epochs+1)],
		var_name='epoch',
		value_name='acc')
	sns.lineplot(
		x='epoch',
		y='acc',
		hue='split',
		ci=95,
		data=df_acc_plot_format)
	plt.show()

	val_acc_avgs = df_acc[df_acc['split']=='val_acc'].mean()
	print("Max Accuracy: " + str(max(val_acc_avgs)) 
			+ "\tEpoch: " + str(val_acc_avgs.idxmax()))
	pprint(val_acc_avgs)

	df_loss_plot_format = df_loss.copy().melt(
		id_vars=['split'],
		value_vars=[n for n in range(1, train_epochs+1)],
		var_name='epoch',
		value_name='acc')
	sns.lineplot(
		x='epoch',
		y='acc',
		hue='split',
		ci=95,
		data=df_loss_plot_format)
	plt.show()

	val_loss_avgs = df_loss[df_loss['split']=='val_loss'].mean()
	print("Min Loss: " + str(min(val_loss_avgs)) 
			+ "\tEpoch: " + str(val_loss_avgs.idxmin()))
	pprint(val_loss_avgs)