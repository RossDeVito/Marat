import os

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense, Dropout

from sklearn.model_selection import train_test_split

if __name__ == '__main__':
	source = '114thmin100_dbow+w_d300_n5_w15_mc15_s1e-05_t4.h5'
	df = pd.read_hdf(os.path.join('dataframes', source), 'df')
	df = df[((df['party']=='R') | (df['party']=='D')) & (df['num_texts'] != 0)]
	df['party_bin'] = (df['party'] == 'D').astype(int) #D is 1, R is 0
	# X = np.array(df['avg_vec'].tolist())
	# X_train, X_test, y_train, y_test = train_test_split(
	# 	df['avg_vec'],
	# 	df['party_bin'],
	# 	test_size=.2,
	# 	shuffle=True,
	# 	random_state=7
	# )
	# X_train = np.stack(X_train.tolist())
	# X_test = np.matrix(X_test.tolist())
	X = np.array(df['avg_vec'])
	X = np.stack(X)
	y = np.array(df['party_bin'])
	
	model = Sequential()
	model.add(Dense(150, input_dim=300, activation='relu'))
	model.add(Dropout(.25))
	model.add(Dense(1, activation='sigmoid'))

	model.compile(loss='binary_crossentropy',
					optimizer='rmsprop',
					metrics=['accuracy'])

	# history = model.fit(
	# 	X,
	# 	y,
	# 	batch_size=32,
	# 	epochs=20,
	# 	verbose=1
	# )

	history = model.fit(
		X, 
		y, 
		validation_split=0.2, 
		epochs=150, 
		batch_size=32,
		shuffle=True,
		verbose=1)

	print(history.history.keys())

	plt.plot(history.history['acc'])
	plt.plot(history.history['val_acc'])
	plt.title('model accuracy')
	plt.ylabel('accuracy')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()

	plt.plot(history.history['loss'])
	plt.plot(history.history['val_loss'])
	plt.title('model loss')
	plt.ylabel('loss')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()


