# Apprentice Chef - Classification

## Company Information
 
Apprentice Chef, Inc. is an innovative company with a unique spin on cooking at home. Developed for the busy professional that has little to no skills in the kitchen, they offer a wide selection of daily-prepared gourmet meals delivered directly to your door. Apprentice Chef customers are characters from Games of Thrones.

Each meal set takes at most 30 minutes to finish cooking at home and also comes with Apprentice Chef's award- winning disposable cookware (i.e. pots, pans, baking trays, and utensils), allowing for fast and easy cleanup. Ordering meals is very easy given their user-friendly online platform and mobile app. 

## Objective
In an effort to diversify their revenue stream, Apprentice Chef, Inc. has launched Halfway There, a cross-selling promotion where subscribers receive a half bottle of wine from a local California vineyard every Wednesday (halfway through the work week). The executives at Apprentice Chef also believe this endeavor will create a competitive advantage based on its unique product offering of hard to find local wines. 
 
Halfway There has been exclusively offered to all of the customers in the dataset you received, and the executives would like to promote this service to a wider audience. They have tasked you with analyzing their data, developing your top insights, and building a machine learning model to predict which customers will subscribe to this service. 


## Dataset Metadata
Column	|Description|
:--|:--|
REVENUE	|Total revenue generated over the first year of a customer's journey|
CROSS_SELL_SUCCESS	|Success of promoting Halfway There (1 = SUCCESS, 0 = FAIL)|
NAME|	Full name of customer (collected upon initial registration)|
EMAIL	|Email of customer (collected upon initial registration)|
FIRST_NAME	|First name of customer (collected upon initial registration)|
FAMILY_NAME	|Last name of customer (collected upon initial registration)|
TOTAL_MEALS_ORDERED|	Total count of meals ordered per customer account|
UNIQUE_MEALS_PURCH|	Count of unique meal sets ordered per customer account|
CONTACTS_W_CUSTOMER_SERVICE	|Count of times a customer made contact with customer service (phone, chatbot, or email)|
PRODUCT_CATEGORIES_VIEWED	|Total number of meal categories viewed (online and mobile platforms combined)|
AVG_TIME_PER_SITE_VISIT	|Average platform (web or mobile) visit time per customer account|
MOBILE_NUMBER|	Customer registered with a mobile or landline number (1 = MOBILE, 0 = LANDLINE)|
CANCELLATIONS_BEFORE_NOON	|Number of meals canceled before 12 PM as per cancelation policy|
CANCELLATIONS_AFTER_NOON|	Number of meals canceled after 3 PM as per cancelation policy|
TASTES_AND_PREFERENCES	|Customer specified their tastes and preferences in their profile|
MOBILE_LOGINS|	Count of logins on the mobile platform (app)|
PC_LOGINS|	Count of logins on the web platform (website)|
WEEKLY_PLAN|	Count of weeks a customer subscribed to the weekly plan|
EARLY_DELIVERIES	|Count of orders that we delivered BEFORE the alloted delivery time|
LATE_DELIVERIES	|Count of orders that we delivered AFTER the alloted delivery time|
PACKAGE_LOCKER|	Customer's building has a package locker service or package room|
REFRIGERATED_LOCKER|	Package room has a refrigerated locker|
FOLLOWED_RECOMMENDATIONS_PCT	|Percentage of time a customer followed meal recommendations generated displayed on the web or mobile platform|
AVG_PREP_VID_TIME|	Average time in seconds a customer watched  instructional videos for meal preparation|
LARGEST_ORDER_SIZE	|Largest number of meals a customer has ordered in a single order|
MASTER_CLASSES_ATTENDED|	Count of times a customer attended master class (learning to cook)|
MEDIAN_MEAL_RATING|	Median meal satisfaction rating by customer|
AVG_CLICKS_PER_VISIT|	Average number of clicks per site visit|
TOTAL_PHOTOS_VIEWED|	Count of photos viewed on web and mobile platforms (measured in clicks)|



-------------------------------------------

## Report Overview

    1. Exploration
        - Missing values
        - Descriptive statistics
        - Potential outliers
        - Cross Sell Success
            - Distribution
            - Median Values
            - Correlation
    
    2. Feature Engineering
        - Additional Calculated Fields
        - Log
        - Outlier Detection
        - Trend Analysis
        - Potential Youth
        - Family Name
        - Number of Names
        - Full Name
        - Family Name
        - Discount Plan
        - Email Domains
        - Median Rating

    3. Dataset Preparation
        - Dropping Categorical Values
        - Updated Correlation
        
    4. Variable Selection
        - Stats Model
            - All Explanatory Variables
            - Adjusted Model
        - Pruned Tree
        
    5. Model Building
    
        - Logistic Regression
        - KNN Non Standardized
        - Classification Tree - Pruned
        - Support Vector Machine (SVM)
        - Bayes Model
        - Random Forest
        
    6. Model Performance
    
    7. Project Overview
        - Insights
        - Recommendations
        
    8. Sources
     
# Model Comparison
Now we have all our model results, we can compare how each performed on both explanatory variable sets.

Model | Logistic Regression Features | Pruned Tree Features	|
------|------------------------------|----------------------|
Logistic Regression | 0.7242 | 0.6961|
KNN Non-Standardized | 0.7557 |0.7721|
CART - Pruned | 0.7314 | 0.7162|
SVM | 0.815 | 0.818|
Bayes |0.7906 | 0.7467|
Random Forest |  0.7378 | 0.7214|

Overall we see that the explanatory variables from the Stats Model Logistic Regression performed better on Scikit Learn Models:

    - Logistic Regression
    - CART - Pruned
    - Bayes
    - Random Forest
    
and the Pruned Tree explanatory variables performed better on:

    - SVM
    - KNN Non-Standardized
    
### Top Model
In the end the final model with the highest AUC score was the Support Vector Machine (SVM), which it outperformed all the models consistently, with the pruned tree explanatory variables having a slightly higher score.

    Support Vector Machine (SVM) Model AUC Score: 0.818
    
    
---------------------------------

# Project Overview

### Insight #1

Users that signed up for their accounts using their professional work emails had shown strong significance in model performance. Users with professional emails totaled 36% (696 users) of the entire customer base and converted 80% of the time to the cross-sell campaign. 

With this information, we can potentially determine that users signing up with their work email could be earning more income, have less time to cook and prepare their food, and are at minimum age to consume wine. These users would be getting a more efficient cooking experience using Apprentice Chef’s product and would purchase wine more frequently.

### Insight #2

Classifying customers into discount levels, Basic, Premium, and no discount, there were no users in the basic discount, compared to 72% (1400) of users with a premium discount, and 546 users with no discounts.  Surprisingly the wine promotion had the same success rate, 68% for both premium and no discount groups. 

One would expect that customers with discounts would be more attracted to the wine promotion. However, the company could be losing more money, offering a premium discount to customers who are not converting the cross-sell wine promotion.  Financially the discounts could be counterproductive for cross-sell success.

### Recommendation

The business opportunity for Apprentice Chef would be to increase its presence in corporate partnerships. We saw users with professional emails, produce more robust results in converting the wine promotion. 

The startup culture, in particular, have great meal benefits, providing their employee's food at lunch and sometimes at night post work. On average, Apprentice Chef's meals cost $16.50, and a company spends $15-17 per employee meal (HighFive, 2019). Apprentice Chef should be approaching companies to provide exclusive partnership prices to supply their meals to their employees, so instead of staying back to eat lunch or dinner, they can head home and cook for themselves and their family. 

Competitor Blue Apron, provide exclusive discounts for corporates depending on meal frequency and company size (Blue Apron). With these employees spending more time at home and enjoying the services from Apprentice Chef, the wine promotion could be easier to convert. Given that their employers will supply the employees Apprentice Chef meals, the employee could add the wine promotion out of their pocket and wouldn't incur that much cost overall.
Working with companies to supply meals to their employees could monumentally increase new users, grow revenue, and cross-sell success of the wine promotion.

------------------------------------------------

# Sources

1.	Blue Apron. (n.d.). Retrieved from https://www.blueapron.com/pages/corporate-sales
2.	Brownlee, J. (2019, December 26). Discover Feature Engineering, How to Engineer Features and How to Get Good at It. Retrieved from https://machinelearningmastery.com/discover-feature-engineering-how-to-engineer-features-and-how-to-get-good-at-it/
3.	Chakure, A. (2019, July 7). Decision Tree Classification. Retrieved from https://towardsdatascience.com/decision-tree-classification-de64fc4d5aac
4.	Google Developers. (n.d.). Classification: ROC Curve and AUC  |  Machine Learning Crash Course. Retrieved from https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
5.	Highfive. (2019, August 24). The Value of Providing Lunch for Employees. Retrieved from https://highfive.com/blog/value-of-providing-lunch-for-employees
6.	Mcleod, S. (2019, May 20). P-values and statistical significance. Retrieved from https://www.simplypsychology.org/p-value.html
7.	Minitab. (n.d.). Three Common P-Value Mistakes You'll Never Have to Make. Retrieved from https://blog.minitab.com/blog/understanding-statistics/three-common-p-value-mistakes-youll-never-have-to-make
8.	Princeton. (n.d.). DSS - Interpreting Regression Output. Retrieved from https://dss.princeton.edu/online_help/analysis/interpreting_regression.htm
9.	Reinstein, I. (n.d.). Random Forests®, Explained. Retrieved from https://www.kdnuggets.com/2017/10/random-forests-explained.html
10.	Ren, E. (2019, April 1). Fundamental Techniques of Feature Engineering for Machine Learning. Retrieved from https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114
11.	Srivastava, T. (2019, September 3). Introduction to KNN, K-Nearest Neighbors : Simplified. Retrieved from https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/
12.	Stephanie. (2017, October 12). Stratification: Definition. Retrieved from https://www.statisticshowto.datasciencecentral.com/stratification-definition/
13.	Zornoza, J. (2019, September 5). Probability Learning II: How Bayes' Theorem is applied in Machine Learning. Retrieved from https://towardsdatascience.com/probability-learning-ii-how-bayes-theorem-is-applied-in-machine-learning-bd747a960962
