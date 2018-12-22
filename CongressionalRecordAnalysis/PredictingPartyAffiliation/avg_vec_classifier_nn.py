import os
#hello
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
		test_size=.001,
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

	plt.plot(m_1_res.history['acc'])
	plt.plot(m_1_res.history['val_acc'])
	plt.plot(m_2_res.history['acc'])
	plt.plot(m_2_res.history['val_acc'])
	plt.plot(m_3_res.history['acc'])
	plt.plot(m_3_res.history['val_acc'])
	plt.title('model accuracy')
	plt.ylabel('accuracy')
	plt.xlabel('epoch')
	plt.legend(
		['model 1 train', 'model 1 test', 
			'model 2 train', 'model 2 test', 
			'model 3 train', 'model 3 test'], 
		loc='lower right')
	plt.show()

	plt.plot(m_1_res.history['loss'])
	plt.plot(m_1_res.history['val_loss'])
	plt.plot(m_2_res.history['loss'])
	plt.plot(m_2_res.history['val_loss'])
	plt.plot(m_3_res.history['loss'])
	plt.plot(m_3_res.history['val_loss'])
	plt.title('model loss')
	plt.ylabel('loss')
	plt.xlabel('epoch')
	plt.legend(
		['model 1 train', 'model 1 test', 
			'model 2 train', 'model 2 test', 
			'model 3 train', 'model 3 test'], 
		loc='upper left')
	plt.show()