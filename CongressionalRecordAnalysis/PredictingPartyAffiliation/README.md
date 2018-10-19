# Predicting Party Affiliation
Task: Based only on what a congressperson said while in a congressional session, predict part affiliation as either Democat or Republican.
May add Independant as option later.

## Feature Selection

Will experiment using the following as the feature vector for each congressperson:

### Average Vector
All individual speach segments are converted to vectors with the original Gensim doc2vec model. The average of these vectors for each congressperson will be used.

Below are the PCA plots for all speach segments and the averages or the vectors for a speakers segments.

![all](https://github.com/RossDeVito/Marat/blob/master/Images/PCA_plot_all_vecs.png)
![avg](https://github.com/RossDeVito/Marat/blob/master/Images/PCA_plot_avg_vecs.png)


### Length Weighted Avg. Vector
Same as above, but using weighted geometric mean based on length of speach segment. This would make longer speach segments have a greater impact on the average vector.

### Vectorized Union of Speach Segments
A union of all speach segments are combined and the original Gensim doc2vec model is used to determine a vector representation.

### N Clusters
Vector representations of speach segments will be clustered into N groups. The average vectors of all N groups will be used as a feature vector.

# Implemented Approaches

## 1. Neural Network using Average Vectors

### Hyperparameter Optimization
Using [Hyperas](https://github.com/maxpumperla/hyperas). The same test set was used for all rounds.

#### Round 1:
Potential Parameters:
- 1-3 hidden layers with: 
	- either 100, 150, 256, 300, or 512 neurons
	- either relu or tanh activation function
	- dropout from 0-1
- rmsprop, adam, or sgd optimizer
- batch size of 16, 32, 64, or 128

Best Performing Model:
- Hidden Layer 1:
	- nuerons: 		300
	- activation: 	relu
	- dropout: 		0.54424
- Hidden Layer 2:
	- nuerons: 		512
	- activation: 	tanh
	- dropout: 		0.43404
- Hidden Layer 3:
	- nuerons: 		300
	- activation: 	relu
	- dropout: 		0.69751
- Optimizer:	rmsprop
- Batch Size:	16
- Performance on Test Set:
	- Accuracy: 	0.9259259281335054
	- Loss: 		0.5632826244389569

#### Round 2:
Potential Parameters:
- 2-5 hidden layers with: 
	- either 150, 200, 256, 300, 350, 400, or 512 neurons
	- either relu or tanh activation function
	- dropout from 0-1
- rmsprop, adam, or sgd optimizer
- batch size of 8, 16, 32, or 64

Best Performing Model:
- Hidden Layer 1:
	- nuerons: 		300
	- activation: 	tanh
	- dropout: 		0.06570
- Hidden Layer 2:
	- nuerons: 		350
	- activation: 	relu
	- dropout: 		0.73664
- Hidden Layer 3:
	- nuerons: 		512
	- activation: 	relu
	- dropout: 		0.78715
- Optimizer:	adam
- Batch Size:	16
- Performance on Test Set:
	- Accuracy: 	0.9351851851851852
	- Loss: 		0.7920230677765276