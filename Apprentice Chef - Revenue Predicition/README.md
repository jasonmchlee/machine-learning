# Apprentice Chef Case Study - Revenue Prediction

    Owner: Jason Lee
    Topic: Machine Learning

<p align="center">
<img src="https://github.com/jasonmchlee/machine-learning/blob/master/Apprentice%20Chef%20-%20Revenue%20Predicition/Apprentice%20Chef%20-%20Cover%20Photo.png" width="600" height="350">
</p>

# Company Information
 
Apprentice Chef, Inc. is an innovative company with a unique spin on cooking at home. Developed for the busy professional that has little to no skills in the kitchen, they offer a wide selection of daily-prepared gourmet meals delivered directly to your door.

Each meal set takes at most 30 minutes to finish cooking at home and also comes with Apprentice Chef's award- winning disposable cookware (i.e. pots, pans, baking trays, and utensils), allowing for fast and easy cleanup. Ordering meals is very easy given their user-friendly online platform and mobile app. 

# Objective
After three years serving customers across the San Francisco Bay Area, the executives at Apprentice Chef have come to realize that over 90% of their revenue comes from customers that have been ordering meal sets for 12 months or less.

Given this information, they would like to better understand how much revenue to expect from each customer within their first year of orders. Thus, they have hired you on a full-time contract to analyze their data, develop your top insights, and build a machine learning model to predict revenue over the first year of each customer’s life cycle. 

# Report Overview

    1. Exploration
        - Missing values
        - Descriptive statistics
        - Potential outliers
    
    2. Feature Engineering
        - Logarithm
        - Outlier Distribution
        - Trend Analysis
        - Email Grouping
        - Email Dummy Variables
        
    3. Model Building
        I.  Stats Model
              - Original Model
              - After removing p-values
        II. Scikit Learn 
              - Train/Test Split
                  - Using new X Variables
              - Ordinary Least Squares (OLS) Regression
              - Ridge Regression
              - Lasso Regression
              - ARD Regression
              - Gradient Boosting Regressor
              - K Nearest Neighbors
                  - Standardized
                  - Non Standardized
        
    4. Model Performance
        - Overall Results
        
    5. Project Overview
        - Insights
        - Recommendations
        
    6. Sources
    
   
# Model Overview

Model|      Train Score    |  Test Score
-----   |   -----------  |    ----------
OLS      |  0.8066       |    0.7693
Ridge    |  0.8052       |    0.7648
Lasso     | 0.3726       |    0.3551
ARD      |  0.7949       |    0.7603
GB       |  0.839       |   0.802
KNN_NS_9 | 0.6204  | 0.4883
KNN_S_20 | 0.6919   | 0.5851


For our results we can see the the best overall performing model is our Gradient Boosting with a testing set score of,

    •    Gradient Boosting Test Score of 0.802

As expected the Lasso model performed very poorly due to us already utilizing log variables, which would effect the results. We can see that the KNN models for both performed poorly. It is interesting to see that the KNN model with standardized variables perfomed almost 0.1 better than the KNN without standardized data. With this information we could test out different variations of parameter and feature tuning to try get this model competing with the other regression models.Overall the OLS, Ridge and ARD regression model all came close of one another, paving the way for more opportunities to develop features that would suit their respective model. 

Using Gradient Boosting, we were able to pass in a number for the CV argument allowing more iterations to be tested. After running this model with different variations of CV, the final number 10 deemed to be the most optimal to maintain a model run time of under 1 minute. Adjusting this further would require more computational power and may delay the performance. 

# Project Overview

## Insight #1
We can see that a great metric for improving revenue was how much time a user spent watching videos. Through the analysis, there is a pattern when more time is spent viewing and learning how to prepare the meals, and it would also affect the amount of revenue a customer would bring into the company. Studying customer engagement and viewing how they respond to the video content will provide two avenues for growth - increased revenue and better user experience. They can assess the demand for the videos and cater to more personalized video solutions for their audience.

## Insight #2
Looking at a possible influence of the churn rate for the Apprentice customers, we can observe that when customers contact the support team, there is initially a positive association with revenue. However, we see there is a drastic shift in the relationship. When a customer spends more time contacting support, their revenue has a negative relationship. Increased contacts for support is most likely due to errors in the orders or a bad user experience, which is prompting users to reach out. We see the trigger point around ten contacts with the support team. A good strategy would be to monitor the frequency of users communicating to make sure to mitigate and manage possible mishaps before they happen.


## Recommendation
My recommendation would be to expand its customer acquisition channels and improve revenue by introducing enhanced and unique video prepping sessions. Using their current strategy but expanding to unique demographics, cuisines, and time frames. An idea could be providing themed meal video preps throughout the week, for example, "Thai food Tuesday," "Mexican Monday," etc. Creating mini-series of food prep videos will stimulate interest and engagement within their community. Increasing video prep and tutorials will also potentially help reduce contacts with customer support. Assuming that the current issues with the support team are related to food prep or techniques, the video can help address this and essentially kill two birds with one stone. Continuing the focus on videos, easy "how to get started" tutorials in how to operate the service and set up the first few orders is always great to simplify the user experience and provide as much support before any issues from occurring.


----------------------------------------------------------------

# Sources
1. Datacamp, (Tutorial) Handling Categorical Data in Python. (n.d.). Retrieved March 7, 2020, from https://www.datacamp.com/community/tutorials/categorical-data
2. DataRobot, Feature Engineering for Automated Machine Learning: Dataset Features. (n.d.). Retrieved March 7, 2020, from https://www.datarobot.com/wiki/feature-engineering/
3. Alto, V. (2019, August 17). Understanding the OLS method for Simple Linear Regression. Retrieved from https://towardsdatascience.com/understanding-the-ols-method-for-simple-linear-regression-e0a4e8f692cc
4. Brownlee, J. (2019, December 26). Discover Feature Engineering, How to Engineer Features and How to Get Good at It. Retrieved from https://machinelearningmastery.com/discover-feature-engineering-how-to-engineer-features-and-how-to-get-good-at-it/
5. Elsinghorst, S. (2018, November 29). Machine - - - Learning Basics - Gradient Boosting & XGBoost. Retrieved from https://shirinsplayground.netlify.com/2018/11/ml_basics_gbm/Feature
6. Mcleod, S. (2019, May 20). P-values and statistical significance. Retrieved from https://www.simplypsychology.org/p-value.html
7. Princeton, DSS - Interpreting Regression Output. (n.d.). Retrieved from https://dss.princeton.edu/online_help/analysis/interpreting_regression.htm

8. Rençberoğlu, E. (2019, April 1). Fundamental Techniques of Feature Engineering for Machine Learning. Retrieved from https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114
9. Srivastava, T. (2019, September 3). Introduction to KNN, K-Nearest Neighbors : Simplified. Retrieved from https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering
10. Three Common P-Value Mistakes You'll Never Have to Make. (n.d.). Retrieved from https://blog.minitab.com/blog/understanding-statistics/three-common-p-value-mistakes-youll-never-have-to-make
--------------------------------------------------------------
