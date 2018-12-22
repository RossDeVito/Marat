## Hyperparameter Optimization
Using [Hyperas](https://github.com/maxpumperla/hyperas). The same test set was used for all rounds. Potential parameters were modified based on results of previous round

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

#### Round 4 Potential Parameters:
- 2-6 hidden layers with: 
	- either 256, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, or 700 neurons
	- either relu or tanh activation function
	- dropout from 0-1
- rmsprop, adam, or sgd optimizer
- batch size of 8, 16, or 32

#### Best Performing Model Chosen Hyper-Parameters and Test Set Performance:
All rounds resulted in a best performing model with 3 hidden layers.

<table><tr><th>Round</th><th>Layer 1:<br>Neurons<br></th><th><br>Activation<br></th><th><br>Dropout</th><th>Layer 2:<br>Neurons<br></th><th><br>Activation<br></th><th><br>Dropout<br></th><th>Layer 3:<br>Neurons<br></th><th><br>Activation</th><th><br>Dropout<br></th><th>Optimizer</th><th>Batch Size</th><th>Test Set Accuracy</th></tr><tr><td>1</td><td>300</td><td>relu</td><td>.54424</td><td>512</td><td>tanh</td><td>.43404</td><td>300</td><td>relu</td><td>.69751</td><td>rmsprop</td><td>16</td><td>0.9259259281335054</td></tr><tr><td>2</td><td>300</td><td>tanh</td><td>.06570</td><td>350</td><td>relu</td><td>.73664</td><td>512</td><td>relu</td><td>.78715</td><td>adam</td><td>16</td><td>0.9351851851851852</td></tr><tr><td>3</td><td>450</td><td>tanh</td><td>.06570</td><td>550</td><td>relu</td><td>.73664</td><td>600</td><td>relu</td><td>.78715</td><td>adam</td><td>16</td><td>0.907407405199828</td></tr><tr><td>4</td><td>600</td><td>relu</td><td>.84691</td><td>525</td><td>tanh</td><td>.32104</td><td>575</td><td>relu</td><td>.59487</td><td>rmsprop</td><td>8</td><td>0.8703703725779498</td></tr></table>