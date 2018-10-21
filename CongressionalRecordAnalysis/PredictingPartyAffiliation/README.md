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

#### Round 1 Potential Parameters:
- 1-3 hidden layers with: 
	- either 100, 150, 256, 300, or 512 neurons
	- either relu or tanh activation function
	- dropout from 0-1
- rmsprop, adam, or sgd optimizer
- batch size of 16, 32, 64, or 128

#### Round 2 Potential Parameters:
- 2-5 hidden layers with: 
	- either 150, 200, 256, 300, 350, 400, or 512 neurons
	- either relu or tanh activation function
	- dropout from 0-1
- rmsprop, adam, or sgd optimizer
- batch size of 8, 16, 32, or 64

#### Round 3 Potential Parameters:
- 2-5 hidden layers with: 
	- either 256, 300, 350, 400, 450, 500, 550, or 600 neurons
	- either relu or tanh activation function
	- dropout from 0-1
- rmsprop, adam, or sgd optimizer
- batch size of 8, 16, 32, or 64

|         | Layer 1 |            |          | Layer 2 |            |          | Layer 3 |            |          | Optimizer | Batch Size | Test Set           |                    |
|---------|---------|------------|----------|---------|------------|----------|---------|------------|----------|-----------|------------|--------------------|--------------------|
|         | Nuerons | Activation | Droupout | Nuerons | Activation | Droupout | Nuerons | Activation | Droupout |           |            | Accuracy           | Loss               |
| Round1  | 300     | relu       | .54424   | 512     | tanh       | .43404   | 300     | relu       | .69751   | rmsprop   | 16         | 0.9259259281335054 | 0.5632826244389569 |
| Round 2 | 300     | tanh       | .06570   | 350     | relu       | .73664   | 512     | relu       | .78715   | adam      | 16         | 0.9351851851851852 | 0.7920230677765276 |
| Round 3 | 450     | tanh       | .06570   | 550     | relu       | .73664   | 600     | relu       | .78715   | adam      | 16         | 0.907407405199828  | 0.6660188585519791 |