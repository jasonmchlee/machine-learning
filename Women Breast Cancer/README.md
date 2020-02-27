# Women Breast Cancer
In this notebook I'll work with the Wisconsin Breast Cancer [Dataset](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data) from the UCI machine learning repository.

I'll predict whether a tumor is malignant or benign based on two features: the mean radius of the tumor (radius_mean) and its mean number of concave points (concave points_mean). In order to have target variables I will need to replace the B (Benign) for a 0 and M (Malignant) for a 1.

## Classification Tree
Splitting the dataset nto 80% training, and 20% testing set. Giving us X_train, x_test, y_train and y_test. Our y variable will be the diagnosis feature, which tells us whether or not the patient was diagnosed with breast cancer. For the X variable the dataframe will contain 2 features - radius_mean, and concave points_mean.

Using a classification tree model to predic the performance on the testing set, we can see the model performed relative well. There is a test accruacy of 89%. 

## Using entropy as a criterion
Entropy, as it relates to machine learning, is a measure of the randomness in the information being processed. The higher the entropy, the harder it is to draw any conclusions from that information. Flipping a coin is an example of an action that provides information that is random. For a coin that has no affinity for heads or tails, the outcome of any number of tosses is difficult to predict. Why? Because there is no relationship between flipping and the outcome. This is the essence of entropy.

I will want to make a classification model using 30 features in the dataset. I will need to create new dataframes.

Now I build a new training and test set, with the same y variable - diagnosis, but now the X variable dataframe will contain the remaining necessary columns to have 30 features.

The X columns will include:

*['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
       'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']*
  
## Using gini index as criteria
Information Gain is used to determine which feature/attribute gives us the maximum information about a class. It is based on the concept of entropy, which is the degree of uncertainty, impurity or disorder. It aims to reduce the level of entropy starting from the root node to the leave nodes.

We will use the same test and train datasets from the entrophy criterion.

## Results
 - Accuracy achieved by using entropy:  0.9298245614035088
 - Accuracy achieved by using the gini index:  0.9298245614035088

Notice how the two models achieve exactly the same accuracy. Most of the time, the gini index and entropy lead to the same results. The gini index is slightly faster to compute and is the default criterion used in the DecisionTreeClassifier model of scikit-learn.


