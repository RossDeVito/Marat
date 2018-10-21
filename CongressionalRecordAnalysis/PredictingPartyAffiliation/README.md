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

#### Best Performing Model Chosen Hyper-Parameters:

<table><tr><th>Round</th><th>Layer 1:<br>Neurons<br></th><th><br>Activation<br></th><th><br>Dropout</th><th>Layer 2:<br>Neurons<br></th><th><br>Activation<br></th><th><br>Dropout<br></th><th>Layer 3:<br>Neurons<br></th><th><br>Activation</th><th><br>Dropout<br></th><th>Optimizer</th><th>Batch Size</th><th>Test Set Accuracy</th><th>Test Set Loss</th></tr><tr><td>1</td><td>300</td><td>relu</td><td>.54424</td><td>512</td><td>tanh</td><td>.43404</td><td>300</td><td>relu</td><td>.69751</td><td>rmsprop</td><td>16</td><td>0.9259259281335054</td><td>0.5632826244389569</td></tr><tr><td>2</td><td>300</td><td>tanh</td><td>.06570</td><td>350</td><td>relu</td><td>.73664</td><td>512</td><td>relu</td><td>.78715</td><td>adam</td><td>16</td><td>0.9351851851851852</td><td>0.7920230677765276</td></tr><tr><td>3</td><td>450</td><td>tanh</td><td>.06570</td><td>550</td><td>relu</td><td>.73664</td><td>600</td><td>relu</td><td>.78715</td><td>adam</td><td>16</td><td>0.907407405199828</td><td>0.6660188585519791</td></tr></table>