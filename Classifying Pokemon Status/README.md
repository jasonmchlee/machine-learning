# Classification for Legendary Pokemon
For this analysis I’m going to dive into Pokemon ratings and whether or not they are marked as being “Legendary”. I will focus on creating a logistic model and a desicion tree model to help predict whether or not a pokemon will be Legendary based on specific variables.

- [Towards Data Science Publication](https://towardsdatascience.com/introduction-to-machine-learning-with-pokemon-ccb7c9d1351b)
- [RPubs Markdown](http://rpubs.com/jasonmchlee/pokemon)

This dataset is a database of pokemon and their characteristics.

1. Type_1
2. Type_2
3. Total
4. HP
5. Attack
6. Defense
7. Sp_Atk
8. Sp_Def
9. Speed
10. Generation
11. Legendary

Our goal is to use these features to determine whether we can predict a pokemon is classified as Legendary or not.

## Objectives
1. Create a training and testing dataset
2. Build a logistic model
3. Build decision model
4. Test both models
5. Compare performance of both models

## Results
If we use the models we can try predict two Pokemon ID numbers and determine if they are Legendary.

Pokemon ID 59
- Model Prediction: Most likely not legendary
- Actual: Not legendary

Pokemon ID 799
- Model Prediction: Most likely legendary
- Actual: Legendary

Looking at both models in our analysis we can see that the Logisitic Model performs better and therefore is a stronger choice to use when predicting if a Pokemon will be Legendary.
