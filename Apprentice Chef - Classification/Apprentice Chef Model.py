#!/usr/bin/env python
# coding: utf-8

# In[3]:


# time

# Student Name : Jason Lee
# Cohort       : Valencia


#####################
## IMPORT PACKAGES ##
#####################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn.linear_model
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score 

#####################
#### LOAD DATA ######
#####################

original_df = pd.read_excel("Apprentice_Chef_Dataset.xlsx")



###########################
##### FEATURES - LOG ######
###########################

# for loop to get the log of select columns
log_list = ['TOTAL_MEALS_ORDERED']

for column in log_list:
    original_df['log_'+ column] = original_df[column].transform(np.log)


################################
##### FEATURES - OUTLIERS ######
################################

# Setting thresholds for features
TOTAL_MEALS_ORDERED_hi           = 150         # we can see a normal distribution if we cut of at this point
UNIQUE_MEALS_PURCH_hi            = 8           # we can see a normal distribution if we cut of at this point
CONTACTS_W_CUSTOMER_SERVICE_hi   = 9           # we can see a normal distribution if we cut of at this point
PRODUCT_CATEGORIES_VIEWED_lo     = 2           # setting this as MIN will exclude outliers
PRODUCT_CATEGORIES_VIEWED_hi     = 8           # setting this as MAX will exclude outliers
AVG_TIME_PER_SITE_VISIT_hi       = 175         # we can see a normal distribution if we cut of at this point
CANCELLATIONS_BEFORE_NOON_hi     = 3           # setting this as MIN will exclude outliers
CANCELLATIONS_AFTER_NOON_hi      = 0           # setting this as MIN will exclude outliers
PC_LOGINS_lo                     = 5           # setting this as MIN will exclude outliers
PC_LOGINS_hi                     = 6           # setting this as MAX will exclude outliers
WEEKLY_PLAN_hi                   = 18          # we can see a normal distribution if we cut of at this point
EARLY_DELIVERIES_hi              = 2           # we can see a normal distribution if we cut of at this point
LATE_DELIVERIES_hi               = 7           # we can see a normal distribution if we cut of at this point
AVG_PREP_VID_TIME_hi             = 250         # we can see a normal distribution if we cut of at this point
LARGEST_ORDER_SIZE_lo            = 3           # setting this as MIN will exclude outliers
LARGEST_ORDER_SIZE_hi            = 6           # setting this as MAX will exclude outliers  
MASTER_CLASSES_ATTENDED_hi       = 1           # we can see a normal distribution if we cut of at this point
MEDIAN_MEAL_RATING_hi            = 3           # we can see a normal distribution if we cut of at this point
AVG_CLICKS_PER_VISIT_lo          = 9           # setting this as MIN will exclude outliers
AVG_CLICKS_PER_VISIT_hi          = 17.5        # setting this as MAX will exclude outliers 
TOTAL_PHOTOS_VIEWED_hi           = 50          # we can see a normal distribution if we cut of at this point

# Feature Engineering (outlier thresholds)
###########################################


# total meals ordered
original_df['out_TOTAL_MEALS_ORDERED'] = 0
total_hi = original_df.loc[0:,'out_TOTAL_MEALS_ORDERED'][original_df['TOTAL_MEALS_ORDERED'] > TOTAL_MEALS_ORDERED_hi]

original_df['out_TOTAL_MEALS_ORDERED'].replace(to_replace = total_hi,
                                value      = 1,
                                inplace    = True)

# unique meals purchase
original_df['out_UNIQUE_MEALS_PURCH'] = 0
unique_hi = original_df.loc[0:,"out_UNIQUE_MEALS_PURCH"][original_df['UNIQUE_MEALS_PURCH'] > UNIQUE_MEALS_PURCH_hi]

original_df['out_UNIQUE_MEALS_PURCH'].replace(to_replace = unique_hi,
                                    value = 1,
                                    inplace = True)

# customer service contacts
original_df['out_CONTACTS_W_CUSTOMER_SERVICE'] = 0
customer_service_hi = original_df.loc[0:,"out_CONTACTS_W_CUSTOMER_SERVICE"][original_df['CONTACTS_W_CUSTOMER_SERVICE'] > CONTACTS_W_CUSTOMER_SERVICE_hi]

original_df['out_CONTACTS_W_CUSTOMER_SERVICE'].replace(to_replace = customer_service_hi,
                                    value = 1,
                                    inplace = True)

# product categories viewed
original_df['out_PRODUCT_CATEGORIES_VIEWED'] = 0
product_hi = original_df.loc[0:,'out_PRODUCT_CATEGORIES_VIEWED'][original_df['PRODUCT_CATEGORIES_VIEWED'] > PRODUCT_CATEGORIES_VIEWED_hi]
product_lo = original_df.loc[0:,'out_PRODUCT_CATEGORIES_VIEWED'][original_df['PRODUCT_CATEGORIES_VIEWED'] < PRODUCT_CATEGORIES_VIEWED_lo]

original_df['out_PRODUCT_CATEGORIES_VIEWED'].replace(to_replace = product_hi,
                                 value      = 1,
                                 inplace    = True)

original_df['out_PRODUCT_CATEGORIES_VIEWED'].replace(to_replace = product_lo,
                                 value      = 1,
                                 inplace    = True)


# average visit time
original_df['out_AVG_TIME_PER_SITE_VISIT'] = 0
avg_time_hi = original_df.loc[0:,"out_AVG_TIME_PER_SITE_VISIT"][original_df['AVG_TIME_PER_SITE_VISIT'] > AVG_TIME_PER_SITE_VISIT_hi]

original_df['out_AVG_TIME_PER_SITE_VISIT'].replace(to_replace = avg_time_hi,
                                    value = 1,
                                    inplace = True)

# before noon cancels
original_df['out_CANCELLATIONS_BEFORE_NOON'] = 0
before_noon_hi = original_df.loc[0:,"out_CANCELLATIONS_BEFORE_NOON"][original_df['CANCELLATIONS_BEFORE_NOON'] > CANCELLATIONS_BEFORE_NOON_hi]

original_df['out_CANCELLATIONS_BEFORE_NOON'].replace(to_replace = before_noon_hi,
                                    value = 1,
                                    inplace = True)

# after noon cancels
original_df['out_CANCELLATIONS_AFTER_NOON'] = 0
after_noon_hi = original_df.loc[0:,"out_CANCELLATIONS_AFTER_NOON"][original_df['CANCELLATIONS_AFTER_NOON'] > CANCELLATIONS_AFTER_NOON_hi]

original_df['out_CANCELLATIONS_AFTER_NOON'].replace(to_replace = after_noon_hi,
                                    value = 1,
                                    inplace = True)

# product categories viewed
original_df['out_PC_LOGINS'] = 0
pc_logins_hi = original_df.loc[0:,'out_PC_LOGINS'][original_df['PC_LOGINS'] > PC_LOGINS_hi]
pc_logins_lo = original_df.loc[0:,'out_PC_LOGINS'][original_df['PC_LOGINS'] < PC_LOGINS_lo]

original_df['out_PC_LOGINS'].replace(to_replace = pc_logins_hi,
                                 value      = 1,
                                 inplace    = True)

original_df['out_PC_LOGINS'].replace(to_replace = pc_logins_lo,
                                 value      = 1,
                                 inplace    = True)


# weekly plan
original_df['out_WEEKLY_PLAN'] = 0
weekly_hi = original_df.loc[0:,"out_WEEKLY_PLAN"][original_df['WEEKLY_PLAN'] > WEEKLY_PLAN_hi]

original_df['out_WEEKLY_PLAN'].replace(to_replace = weekly_hi,
                                    value = 1,
                                    inplace = True)

# early delivery
original_df['out_EARLY_DELIVERIES'] = 0
early_hi = original_df.loc[0:,"out_EARLY_DELIVERIES"][original_df['EARLY_DELIVERIES'] > EARLY_DELIVERIES_hi]

original_df['out_EARLY_DELIVERIES'].replace(to_replace = early_hi,
                                    value = 1,
                                    inplace = True)

# late delivery
original_df['out_LATE_DELIVERIES'] = 0
late_hi = original_df.loc[0:,"out_LATE_DELIVERIES"][original_df['LATE_DELIVERIES'] > LATE_DELIVERIES_hi]

original_df['out_LATE_DELIVERIES'].replace(to_replace = late_hi,
                                    value = 1,
                                    inplace = True)

# avergae video time
original_df['out_AVG_PREP_VID_TIME'] = 0
avg_video_hi = original_df.loc[0:,"out_AVG_PREP_VID_TIME"][original_df['AVG_PREP_VID_TIME'] > AVG_PREP_VID_TIME_hi]

original_df['out_AVG_PREP_VID_TIME'].replace(to_replace = avg_video_hi,
                                    value = 1,
                                    inplace = True)

# largest order size
original_df['out_LARGEST_ORDER_SIZE'] = 0
order_hi = original_df.loc[0:,'out_LARGEST_ORDER_SIZE'][original_df['LARGEST_ORDER_SIZE'] > LARGEST_ORDER_SIZE_hi]
order_lo = original_df.loc[0:,'out_LARGEST_ORDER_SIZE'][original_df['LARGEST_ORDER_SIZE'] < LARGEST_ORDER_SIZE_lo]

original_df['out_LARGEST_ORDER_SIZE'].replace(to_replace = order_hi,
                                 value      = 1,
                                 inplace    = True)

original_df['out_LARGEST_ORDER_SIZE'].replace(to_replace = order_lo,
                                 value      = 1,
                                 inplace    = True)


# master classess attended
original_df['out_MASTER_CLASSES_ATTENDED'] = 0
master_hi = original_df.loc[0:,"out_MASTER_CLASSES_ATTENDED"][original_df['MASTER_CLASSES_ATTENDED'] > MASTER_CLASSES_ATTENDED_hi]

original_df['out_MASTER_CLASSES_ATTENDED'].replace(to_replace = master_hi,
                                    value = 1,
                                    inplace = True)

# meal rating
original_df['out_MEDIAN_MEAL_RATING'] = 0
rating_hi = original_df.loc[0:,"out_MEDIAN_MEAL_RATING"][original_df['MEDIAN_MEAL_RATING'] > MEDIAN_MEAL_RATING_hi]

original_df['out_MEDIAN_MEAL_RATING'].replace(to_replace = rating_hi,
                                    value = 1,
                                    inplace = True)


# average clicks per visit
original_df['out_AVG_CLICKS_PER_VISIT'] = 0
clicks_hi = original_df.loc[0:,'out_AVG_CLICKS_PER_VISIT'][original_df['AVG_CLICKS_PER_VISIT'] > AVG_CLICKS_PER_VISIT_hi]
clicks_lo = original_df.loc[0:,'out_AVG_CLICKS_PER_VISIT'][original_df['AVG_CLICKS_PER_VISIT'] < AVG_CLICKS_PER_VISIT_lo]

original_df['out_AVG_CLICKS_PER_VISIT'].replace(to_replace = clicks_hi,
                                 value      = 1,
                                 inplace    = True)

original_df['out_AVG_CLICKS_PER_VISIT'].replace(to_replace = clicks_lo,
                                 value      = 1,
                                 inplace    = True)

# total photos viewed
original_df['out_TOTAL_PHOTOS_VIEWED'] = 0
photos_hi = original_df.loc[0:,"out_TOTAL_PHOTOS_VIEWED"][original_df['TOTAL_PHOTOS_VIEWED'] > TOTAL_PHOTOS_VIEWED_hi]

original_df['out_TOTAL_PHOTOS_VIEWED'].replace(to_replace = photos_hi,
                                    value = 1,
                                    inplace = True)




##########################
##### FEATURE - YOUTH ####
##########################

# potential youth
original_df['potential_youth'] = 0

#looping to find youth
for index, val in original_df.iterrows():
    if 'son' in original_df.loc[ index , 'NAME']:
        original_df.loc[index, 'potential_youth'] = 1
    elif 'daughter' in original_df.loc[ index , 'NAME']:
        original_df.loc[index, 'potential_youth'] = 1
        
        
##########################
##### FEATURE - FREY #####
##########################

# Most common family name - making them binary
original_df['FAMILY_NAME'] = original_df['FAMILY_NAME'].astype(str)

#column with all 0s
original_df['frey_family'] = 0

#loop to calissify frey family
for index, val in original_df.iterrows():
    if 'Frey' in original_df.loc[ index , 'FAMILY_NAME']:
        original_df.loc[index, 'frey_family'] = 1

        
##########################
##### FEATURE - NAME #####
##########################

# function to split names
#########################
def text_split_feature(col, df, sep=' ', new_col_name='number_of_names'):
    """
Splits values in a string Series (as part of a DataFrame) and sums the number
of resulting items. Automatically appends summed column to original DataFrame.

PARAMETERS
----------
col          : column to split
df           : DataFrame where column is located
sep          : string sequence to split by, default ' '
new_col_name : name of new column after summing split, default
               'number_of_names'
"""
    
    df[new_col_name] = 0
    
    
    for index, val in df.iterrows():
        df.loc[index, new_col_name] = len(df.loc[index, col].split(sep = ' '))
        
        
##################
#### FULL NAME ###
##################
# number of names in full name
text_split_feature(col = 'NAME',
                   df  = original_df,
                   new_col_name = 'NUM_OF_NAMES')


####################
#### FAMILY NAME ###
####################
# number of family names
text_split_feature(col = 'FAMILY_NAME',
                   df  = original_df,
                   new_col_name = 'NUM_OF_FAMILY_NAMES')


##############################
##### FEATURE - DISCOUNT #####
##############################
# engineer discount
discount_plan = []

for index, col in original_df.iterrows():
    
    if (original_df.loc[index, 'WEEKLY_PLAN'] > 1) and (original_df.loc[index, 'TOTAL_MEALS_ORDERED'] == 3 or original_df.loc[index, 'TOTAL_MEALS_ORDERED'] == 4):
        discount_plan.append('basic_discount')
    elif (original_df.loc[index, 'WEEKLY_PLAN'] > 1) and (original_df.loc[index, 'TOTAL_MEALS_ORDERED'] > 4):
        discount_plan.append('premium_discount')
    else:
        discount_plan.append('no_discount')

discount_df = pd.DataFrame(discount_plan)

discount_df.columns = ['discount']
discount_df.head()


original_df = pd.concat([original_df, discount_df], axis = 1)


one_hot_discount = pd.get_dummies(original_df['discount'])

original_df = original_df.join([one_hot_discount])


##############################
##### FEATURE - EMAILS  ######
##############################
# create email dummy variables

# Splitting emails
email_list = []

# looping over each email address
for index, col in original_df.iterrows():
    
    # splitting email domain at '@'
    email_split = original_df.loc[index, 'EMAIL'].split(sep = "@")
    
    # add for loop results to list
    email_list.append(email_split)
    
# converting into a DataFrame 
email_df = pd.DataFrame(email_list)

# renaming columns
email_df.columns = ['name' , 'EMAIL_DOMAIN']

# concat email to df
original_df = pd.concat([original_df, email_df['EMAIL_DOMAIN']],
                   axis = 1)

# email domains
personal_emails = [ 'gmail.com','protonmail.com', 'yahoo.com', 'msn.com']
 
professional_emails = [ 'amex.com','merck.com', 'mcdonalds.com','cocacola.com','jnj.com','nike.com', 'apple.com',            
                        'ibm.com', 'ge.org','dupont.com','microsoft.com','chevron.com','unitedhealth.com',
                        'travelers.com', 'exxon.com','boeing.com','verizon.com','mmm.com','pg.com','caterpillar.com',
                        'disney.com','walmart.com','visa.com','pfizer.com','jpmorgan.com', 'unitedtech.com',
                       'cisco.com','goldmansacs.com','intel.com','homedepot.com']   

jumk_emails = ['me.com', 'aol.com','hotmail.com', 'live.com', 'msn.com','passport.com' ]


domain_list = []

for domain in original_df['EMAIL_DOMAIN']:
    
    # crete lists for personal
    if domain in personal_emails:
        domain_list.append("personal") # categorical list
        
    elif domain in professional_emails:
        domain_list.append("professional") # categorical list

    elif domain in jumk_emails:
        domain_list.append("junk") # categorical list    
        
    else:
        print(domain)

# create new series for domain type
original_df['DOMAIN_TYPE'] = pd.Series(domain_list)

# one hot emails
one_hot_email             = pd.get_dummies(original_df['DOMAIN_TYPE'])

# joining codings together
original_df = original_df.join([one_hot_email],
              sort=False)

original_df = original_df.drop(['EMAIL','EMAIL_DOMAIN', 'DOMAIN_TYPE'],
             axis = 1)



################################
##### TRAIN TEST SPLIT #########
################################
x_variables = [     'professional',
                    'junk',
                    'NUM_OF_NAMES',
                    'FOLLOWED_RECOMMENDATIONS_PCT',
                    'WEEKLY_PLAN',
                    'CANCELLATIONS_BEFORE_NOON']

# drop remaining categorical variables - creating the features
customer_data = original_df.loc[:, x_variables]

# drop remaining categorical variables - creating the y variable
customer_target =  original_df['CROSS_SELL_SUCCESS'] 

# train test split
X_train, X_test, y_train, y_test = train_test_split(
            customer_data,
            customer_target,
            test_size    = 0.25,
            random_state = 222,
            stratify     = customer_target)



################################
##### FINAL MODEL - SVM  #######
################################


#instantiate model
svc_kernal_model = SVC(kernel = 'rbf', random_state = 222)

#fit model
svc_kernal_fit = svc_kernal_model.fit(X_train, y_train)

# PREDICTING on new data
svc_kernal_pred = svc_kernal_model.predict(X_test)


################################
##### FINAL MODEL SCORE ########
################################

train_score = svc_kernal_model.score(X_train, y_train).round(4)


test_score = svc_kernal_model.score(X_test, y_test).round(4)

AUC_score   = roc_auc_score(y_true  = y_test, y_score = svc_kernal_pred).round(4)

# check scores
print(f"Support Vector Machine Model AUC Score: {AUC_score}")


# In[ ]:




