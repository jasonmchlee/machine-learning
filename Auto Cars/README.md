# Kaggle Challenge - Auto Car Dataset


Train a regression tree to predict the mpg (miles per gallon) consumption of cars in the auto-mpg [dataset](https://www.kaggle.com/uciml/autompg-dataset) using all the six available features.

### Content
- Title: Auto-Mpg Data
- Sources: (a) Origin: This dataset was taken from the StatLib library which is maintained at Carnegie Mellon University. The dataset was used in the 1983 American Statistical Association Exposition. (c) Date: July 7, 1993
- Past Usage:
    - Quinlan,R. (1993). Combining Instance-Based and Model-Based Learning. In Proceedings on the Tenth International Conference of Machine Learning, 236-243, University of Massachusetts, Amherst. Morgan Kaufmann.


### Relevant Information:

This dataset is a slightly modified version of the dataset provided in the StatLib library. In line with the use by Ross Quinlan (1993) in predicting the attribute "mpg", 8 of the original instances were removed because they had unknown values for the "mpg" attribute. The original dataset is available in the file "auto-mpg.data-original".

"The data concerns city-cycle fuel consumption in miles per gallon, to be predicted in terms of 3 multivalued discrete and 5 continuous attributes." (Quinlan, 1993)

- Number of Instances: 398
- Number of Attributes: 9 including the class attribute
- Attribute Information:
    -  mpg: continuous
    -  cylinders: multi-valued discrete
    -  displacement: continuous
    -  horsepower: continuous
    -  weight: continuous
    -  acceleration: continuous
    -  model year: multi-valued discrete
    -  origin: multi-valued discrete
    -  car name: string (unique for each instance)
 -  Missing Attribute Values: horsepower has 6 missing values
 
 
 ### Performance
I will evaluate the test set performance of dt using the Root Mean Squared Error (RMSE) metric. The RMSE of a model measures, on average, how much the model's predictions differ from the actual labels. The RMSE of a model can be obtained by computing the square root of the model's Mean Squared Error (MSE).

The RMSE is the square root of the variance of the residuals. It indicates the absolute fit of the model to the data–how close the observed data points are to the model’s predicted values. Lower values of RMSE indicate better fit. RMSE is a good measure of how accurately the model predicts the response, and it is the most important criterion for fit if the main purpose of the model is prediction.
