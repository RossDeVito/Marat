import os
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import seaborn as sns

from keras.callbacks import EarlyStopping
from keras.models import Sequential
from keras.layers import Dense, Dropout

from sklearn.model_selection import RepeatedStratifiedKFold #potentially
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split

def load_data():
	"""
	Loads data source df and returns filtered and formatted X and y
	"""
	source = '114thmin100_dbow+w_d300_n5_w15_mc15_s1e-05_t4.h5'
	df = pd.read_hdf(os.path.join('../..', 'dataframes', source), 'df')
	df = df[((df['party']=='R') | (df['party']=='D')) & (df['num_texts'] != 0)]
	df['party_bin'] = (df['party'] == 'D').astype(int) #D is 1, R is 0
	return np.stack(df['avg_vec'].values), df['party_bin'].values

def get_model_1():
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

def get_model_2():
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

def get_model_3():
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

def get_model_4():
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
	n_folds = 10

	res_matrix = []

	earlystop = EarlyStopping(
		monitor='val_loss', 
		patience=5,
		verbose=1, 
		mode='min', 
		restore_best_weights=True)
	callbacks_list = [earlystop]

	X, y = load_data()
	skf = StratifiedKFold(n_splits=n_folds, shuffle=True)

	for fold, (train_indices, test_indices) in enumerate(skf.split(X, y)):
		X_train, X_test = X[train_indices], X[test_indices]
		y_train, y_test = y[train_indices], y[test_indices]

		model_1 = None	#documentation includes this None step
		model_2 = None
		model_3 = None
		model_4 = None
		model_1 = get_model_1()
		model_2 = get_model_2()
		model_3 = get_model_3()
		model_4 = get_model_4()

		model_1.fit(
			X_train, 
			y_train, 
			validation_split=0.1, 
			epochs=100, 
			batch_size=16, #model 4 needs 8, else 16
			callbacks=callbacks_list,
			verbose=2)
		results = model_1.evaluate(X_test, y_test)
		print("model 1, fold "+str(fold)+":\t" +str(results))
		res_matrix.append([1, results[0], results[1]])

		model_2.fit(
			X_train, 
			y_train, 
			validation_split=0.1, 
			epochs=100, 
			batch_size=16, #model 4 needs 8, else 16
			callbacks=callbacks_list,
			verbose=2)
		results = model_2.evaluate(X_test, y_test)
		print("model 2, fold "+str(fold)+":\t" +str(results))
		res_matrix.append([2, results[0], results[1]])

		model_3.fit(
			X_train, 
			y_train, 
			validation_split=0.1, 
			epochs=100, 
			batch_size=16, #model 4 needs 8, else 16
			callbacks=callbacks_list,
			verbose=2)
		results = model_3.evaluate(X_test, y_test)
		print("model 3, fold "+str(fold)+":\t" +str(results))
		res_matrix.append([3, results[0], results[1]])

		model_4.fit(
			X_train, 
			y_train, 
			validation_split=0.1, 
			epochs=100, 
			batch_size=8, #model 4 needs 8, else 16
			callbacks=callbacks_list,
			verbose=2)
		results = model_4.evaluate(X_test, y_test)
		print("model 4, fold "+str(fold)+":\t" +str(results))
		res_matrix.append([4, results[0], results[1]])

	res_df = pd.DataFrame(res_matrix, columns=['model', 'loss', 'accuracy'])
	sns.boxplot(x='model', y='accuracy', data=res_df)
	pprint(res_df)
	plt.show()
	sns.boxplot(x='model', y='loss', data=res_df)
	plt.show()
