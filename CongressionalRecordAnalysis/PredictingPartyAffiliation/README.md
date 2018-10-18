# Predicting Party Affiliation
Task: Based only on what a congressperson said while in a congressional session, predict part affiliation as either Democat or Republican.
May add Independant as option later.

## Feature Selection

Will experiment using the following as the feature vector for each congressperson:

### [X] Avg. Vector
All individual speach segments will be converted to vectors. The average of these vectors will be used.

### [ ] Length Weighted Avg. Vector
Same as above, but using weighted geometric mean based on length of speach segment. This would make longer speach segments have a greater impact on the average vector.

### Vectorized Union of Speach Segments
A union of all speach segments are combined and the original doc2vec model is used to determine a vector representation.

### N Clusters
Vector representations of speach segments will be clustered into N groups. The average vectors of all N groups will be used as a feature vector.

## Machine Learning Methods

###
