import os

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense, Dropout

from sklearn.model_selection import train_test_split

def data():
	"""
	Data providing function.

	This function is separated from create_model() so that hyperopt
	won't reload data for each evaluation run.
	"""
	source = '114thmin100_dbow+w_d300_n5_w15_mc15_s1e-05_t4.h5'

	df = pd.read_hdf(os.path.join('../..', 'dataframes', source), 'df')
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

if __name__ == '__main__':
	X_train, y_train, X_test, y_test = data()

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

	m_1_res = model_1.fit(
		X_train, 
		y_train, 
		validation_split=0.1, 
		epochs=100, 
		batch_size=16,
		verbose=2)

	m_2_res = model_2.fit(
		X_train, 
		y_train, 
		validation_split=0.1, 
		epochs=100, 
		batch_size=16,
		verbose=2)

	m_3_res = model_3.fit(
		X_train, 
		y_train, 
		validation_split=0.1, 
		epochs=100, 
		batch_size=16,
		verbose=2)

	m_4_res = model_4.fit(
		X_train, 
		y_train, 
		validation_split=0.1, 
		epochs=100, 
		batch_size=8,
		verbose=2)

	plt.plot(m_1_res.history['acc'], c='#a6cee3')
	plt.plot(m_1_res.history['val_acc'], c='#1f78b4')
	plt.plot(m_2_res.history['acc'], c='#b2df8a')
	plt.plot(m_2_res.history['val_acc'], c='#33a02c')
	plt.plot(m_3_res.history['acc'], c='#fb9a99')
	plt.plot(m_3_res.history['val_acc'], c='#e31a1c')
	plt.plot(m_4_res.history['acc'], c='#fdbf6f')
	plt.plot(m_4_res.history['val_acc'], c='#ff7f00')
	plt.title('model accuracy')
	plt.ylabel('accuracy')
	plt.xlabel('epoch')
	plt.legend(
		['model 1 train', 'model 1 test', 
			'model 2 train', 'model 2 test', 
			'model 3 train', 'model 3 test',
			'model 4 train', 'model 4 test'], 
		loc='lower right')
	plt.show()

	plt.plot(m_1_res.history['loss'], c='#a6cee3')
	plt.plot(m_1_res.history['val_loss'], c='#1f78b4')
	plt.plot(m_2_res.history['loss'], c='#b2df8a')
	plt.plot(m_2_res.history['val_loss'], c='#33a02c')
	plt.plot(m_3_res.history['loss'], c='#fb9a99')
	plt.plot(m_3_res.history['val_loss'], c='#e31a1c')
	plt.plot(m_4_res.history['loss'], c='#fdbf6f')
	plt.plot(m_4_res.history['val_loss'], c='#ff7f00')
	plt.title('model loss')
	plt.ylabel('loss')
	plt.xlabel('epoch')
	plt.legend(
		['model 1 train', 'model 1 test', 
			'model 2 train', 'model 2 test', 
			'model 3 train', 'model 3 test',
			'model 4 train', 'model 4 test'], 
		loc='upper left')
	plt.show()
