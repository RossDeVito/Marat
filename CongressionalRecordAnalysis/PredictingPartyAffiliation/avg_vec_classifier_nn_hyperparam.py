import os

import numpy as np 
import pandas as pd

from hyperas import optim
from hyperas.distributions import choice, uniform
from hyperopt import Trials, STATUS_OK, tpe

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

	df = pd.read_hdf(os.path.join('../', 'dataframes', source), 'df')
	df = df[((df['party']=='R') | (df['party']=='D')) & (df['num_texts'] != 0)]
	df['party_bin'] = (df['party'] == 'D').astype(int) #D is 1, R is 0

	X_train, X_test, y_train, y_test = train_test_split(
		df['avg_vec'],
		df['party_bin'],
		test_size=.2,
		shuffle=True,
		random_state=7)
	X_train = np.stack(X_train.values)
	y_train = y_train.values  
	X_test = np.stack(X_test.values)
	y_test = y_test.values

	return X_train, y_train, X_test, y_test

def create_model(X_train, y_train, X_test, y_test):
	model = Sequential()
	model.add(Dense(
		{{choice([256, 300, 350, 400, 450, 500, 550, 600])}}, 
		input_dim=300, 
		activation={{choice(['relu', 'tanh'])}}))
	model.add(Dropout({{uniform(0, 1)}}))

	model.add(Dense(
		{{choice([256, 300, 350, 400, 450, 500, 550, 600])}}, 
		activation={{choice(['relu', 'tanh'])}}))
	model.add(Dropout({{uniform(0, 1)}}))

	n_hidden = {{choice(['two', 'three', 'four', 'five'])}}

	if n_hidden != 'two':
		model.add(Dense(
			{{choice([256, 300, 350, 400, 450, 500, 550, 600])}}, 
			activation={{choice(['relu', 'tanh'])}}))
		model.add(Dropout({{uniform(0, 1)}}))

		if n_hidden != 'three':
			model.add(Dense(
				{{choice([256, 300, 350, 400, 450, 500, 550, 600])}}, 
				activation={{choice(['relu', 'tanh'])}}))
			model.add(Dropout({{uniform(0, 1)}}))

			if n_hidden != 'four':
				model.add(Dense(
					{{choice([256, 300, 350, 400, 450, 500, 550, 600])}}, 
					activation={{choice(['relu', 'tanh'])}}))
				model.add(Dropout({{uniform(0, 1)}}))

				if n_hidden != 'five':
					model.add(Dense(
						{{choice([256, 300, 350, 400, 450, 500, 550, 600])}}, 
						activation={{choice(['relu', 'tanh'])}}))
					model.add(Dropout({{uniform(0, 1)}}))
	
	model.add(Dense(1, activation='sigmoid'))
	model.compile(loss='binary_crossentropy',
					optimizer={{choice(['rmsprop', 'adam', 'sgd'])}},
					metrics=['accuracy'])

	result = model.fit(X_train, y_train,
		batch_size={{choice([8, 16, 32])}},
		epochs={{choice([150, 200])}},
		verbose=2,
		validation_split=0.1)
	#get the highest validation accuracy of the training epochs
	validation_acc = np.amax(result.history['val_acc']) 
	print('Best validation acc of epoch:', validation_acc)
	return {'loss': -validation_acc, 'status': STATUS_OK, 'model': model}

if __name__ == '__main__':
	best_run, best_model = optim.minimize(
		model=create_model,
		data=data,
		algo=tpe.suggest,
		max_evals=100,
		trials=Trials())

	X_train, y_train, X_test, y_test = data()
	print("Evalutation of best performing model:")
	print(best_model.evaluate(X_test, y_test))
	print("Best performing model chosen hyper-parameters:")
	print(best_run)