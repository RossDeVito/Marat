# Predicting Party Affiliation
Task: Based only on what a congressperson said while in a congressional session, predict part affiliation as either Democat or Republican.
May add Independant as option later.

## Feature Selection

Will experiment using the following as the feature vector for each congressperson:

### Average Vector
All individual speach segments are converted to vectors with the original Gensim doc2vec model. The average of these vectors for each congressperson will be used.

Below are the PCA plots for all speach segments and the averages of the vectors for each speakers' segments. For the chamber parameter, H represents the House of Representatives and S the Senate.

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

Data on model selection and hyperparameter tuning found [here.](https://github.com/RossDeVito/Marat/tree/master/CongressionalRecordAnalysis/PredictingPartyAffiliation/nn_vec_avg/README.md)