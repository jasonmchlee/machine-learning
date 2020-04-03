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
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split, cross_val_score

#####################
#### LOAD DATA ######
#####################

original_df = pd.read_excel("Apprentice_Chef_Dataset.xlsx")


###########################
##### FEATURES - LOG ######
###########################

# for loop to get the log of select columns
log_list = ['TOTAL_MEALS_ORDERED','UNIQUE_MEALS_PURCH','CONTACTS_W_CUSTOMER_SERVICE',
            'PRODUCT_CATEGORIES_VIEWED','AVG_TIME_PER_SITE_VISIT','PC_LOGINS',
            'AVG_PREP_VID_TIME','MEDIAN_MEAL_RATING','AVG_CLICKS_PER_VISIT']

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




################################
##### FEATURES - TRENDS ########
################################

# Setting thresholds for features
TOTAL_MEALS_ORDERED_hi           = 200        # plots begin to scatter
CONTACTS_W_CUSTOMER_SERVICE_hi   = 9          # plots begin to scatter
AVG_TIME_PER_SITE_VISIT_hi       = 200        # plots begin to scatter  
LATE_DELIVERIES_hi               = 9          # plots begin to scatter
AVG_PREP_VID_TIME_hi             = 225        # plots begin to scatter

MASTER_CLASSES_ATTENDED_at       = 1          # one inflated
UNIQUE_MEALS_PURCH_at            = 0          # zero inflated  
CANCELLATIONS_AFTER_NOON_at      = 0          # zero inflated          
WEEKLY_PLAN_at                   = 0          # zero inflated  
MEDIAN_MEAL_RATING_at            = 3          # three inflated      
TOTAL_PHOTOS_VIEWED_at           = 0          # zero inflated                


# total meals ordered
original_df['tre_TOTAL_MEALS_ORDERED'] = 0
total_hi = original_df.loc[0:,'tre_TOTAL_MEALS_ORDERED'][original_df['TOTAL_MEALS_ORDERED'] > TOTAL_MEALS_ORDERED_hi]

original_df['tre_TOTAL_MEALS_ORDERED'].replace(to_replace = total_hi,
                                value      = 1,
                                inplace    = True)

# unique meals purchase
original_df['tre_UNIQUE_MEALS_PURCH'] = 0
unique_hi = original_df.loc[0:,"tre_UNIQUE_MEALS_PURCH"][original_df['UNIQUE_MEALS_PURCH'] == UNIQUE_MEALS_PURCH_at]

original_df['tre_UNIQUE_MEALS_PURCH'].replace(to_replace = unique_hi,
                                    value = 1,
                                    inplace = True)

# customer service contacts
original_df['tre_CONTACTS_W_CUSTOMER_SERVICE'] = 0
customer_service_hi = original_df.loc[0:,"tre_CONTACTS_W_CUSTOMER_SERVICE"][original_df['CONTACTS_W_CUSTOMER_SERVICE'] > CONTACTS_W_CUSTOMER_SERVICE_hi]

original_df['tre_CONTACTS_W_CUSTOMER_SERVICE'].replace(to_replace = customer_service_hi,
                                    value = 1,
                                    inplace = True)

# after noon cancels
original_df['tre_CANCELLATIONS_AFTER_NOON'] = 0
after_noon_hi = original_df.loc[0:,"tre_CANCELLATIONS_AFTER_NOON"][original_df['CANCELLATIONS_AFTER_NOON'] == CANCELLATIONS_AFTER_NOON_at]

original_df['tre_CANCELLATIONS_AFTER_NOON'].replace(to_replace = after_noon_hi,
                                    value = 1,
                                    inplace = True)

# weekly plan
original_df['tre_WEEKLY_PLAN'] = 0
weekly_hi = original_df.loc[0:,"tre_WEEKLY_PLAN"][original_df['WEEKLY_PLAN'] == WEEKLY_PLAN_at]

original_df['tre_WEEKLY_PLAN'].replace(to_replace = weekly_hi,
                                    value = 1,
                                    inplace = True)

# late delivery
original_df['tre_LATE_DELIVERIES'] = 0
late_hi = original_df.loc[0:,"tre_LATE_DELIVERIES"][original_df['LATE_DELIVERIES'] > LATE_DELIVERIES_hi]

original_df['tre_LATE_DELIVERIES'].replace(to_replace = late_hi,
                                    value = 1,
                                    inplace = True)

# avergae video time
original_df['tre_AVG_PREP_VID_TIME'] = 0
avg_video_hi = original_df.loc[0:,"tre_AVG_PREP_VID_TIME"][original_df['AVG_PREP_VID_TIME'] > AVG_PREP_VID_TIME_hi]

original_df['tre_AVG_PREP_VID_TIME'].replace(to_replace = avg_video_hi,
                                    value = 1,
                                    inplace = True)

# master classess attended
original_df['tre_MASTER_CLASSES_ATTENDED'] = 0
master_hi = original_df.loc[0:,"tre_MASTER_CLASSES_ATTENDED"][original_df['MASTER_CLASSES_ATTENDED'] == MASTER_CLASSES_ATTENDED_at]

original_df['tre_MASTER_CLASSES_ATTENDED'].replace(to_replace = master_hi,
                                    value = 1,
                                    inplace = True)

# meal rating
original_df['tre_MEDIAN_MEAL_RATING'] = 0
rating_hi = original_df.loc[0:,"tre_MEDIAN_MEAL_RATING"][original_df['MEDIAN_MEAL_RATING'] == MEDIAN_MEAL_RATING_at]

original_df['tre_MEDIAN_MEAL_RATING'].replace(to_replace = rating_hi,
                                    value = 1,
                                    inplace = True)

# total photos viewed
original_df['tre_TOTAL_PHOTOS_VIEWED'] = 0
photos_hi = original_df.loc[0:,"tre_TOTAL_PHOTOS_VIEWED"][original_df['TOTAL_PHOTOS_VIEWED'] > TOTAL_PHOTOS_VIEWED_at]

original_df['tre_TOTAL_PHOTOS_VIEWED'].replace(to_replace = photos_hi,
                                    value = 1,
                                    inplace = True)


################################
##### FEATURES - EMAILS ########
################################

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

original_df = original_df.drop(['NAME','EMAIL','FAMILY_NAME', 
             'FIRST_NAME', 'EMAIL_DOMAIN', 'DOMAIN_TYPE'],
             axis = 1)





################################
##### TRAIN TEST SPLIT #########
################################
x_variables = [           'TOTAL_MEALS_ORDERED',
                          'UNIQUE_MEALS_PURCH',
                          'CONTACTS_W_CUSTOMER_SERVICE',
                          'PRODUCT_CATEGORIES_VIEWED',                                   
                          'EARLY_DELIVERIES',
                          'LARGEST_ORDER_SIZE',
                          'MASTER_CLASSES_ATTENDED',
                          'MEDIAN_MEAL_RATING',
                          'log_TOTAL_MEALS_ORDERED',
                          'log_UNIQUE_MEALS_PURCH',
                          'log_PRODUCT_CATEGORIES_VIEWED',
                          'log_AVG_PREP_VID_TIME',
                          'log_MEDIAN_MEAL_RATING',
                          'out_TOTAL_MEALS_ORDERED',
                          'out_UNIQUE_MEALS_PURCH',
                          'out_CONTACTS_W_CUSTOMER_SERVICE',
                          'out_CANCELLATIONS_AFTER_NOON',
                          'out_AVG_PREP_VID_TIME',
                          'out_MASTER_CLASSES_ATTENDED',
                          'out_MEDIAN_MEAL_RATING',
                          'out_TOTAL_PHOTOS_VIEWED',
                          'tre_TOTAL_MEALS_ORDERED',
                          'tre_CONTACTS_W_CUSTOMER_SERVICE',
                          'tre_CANCELLATIONS_AFTER_NOON',
                          'tre_MASTER_CLASSES_ATTENDED',
                          'tre_MEDIAN_MEAL_RATING',
                          'junk',
                          'personal',
                          'professional']

# drop remaining categorical variables - creating the features
customer_data = original_df.loc[:, x_variables]

# drop remaining categorical variables - creating the y variable
customer_target = original_df["REVENUE"].transform(np.log)                   

# preparing training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
            customer_data,
            customer_target,
            test_size = 0.25,
            random_state = 222)


################################
##### FINAL MODEL - GB  ########
################################

gb_model = sklearn.ensemble.GradientBoostingRegressor()

# FITTING the training data
gb_fit = gb_model.fit(X_train,y_train)


# PREDICTING on new data
gb_pred = gb_model.predict(X_test)



################################
##### FINAL MODEL SCORE ########
################################


# saving scoring data for future use
train_score = cross_val_score(gb_model,
                             X_train,
                             y_train,
                             scoring = 'r2',
                             cv=10,
                             n_jobs =-1).mean().round(3)

test_score = cross_val_score(gb_model,
                             X_test,
                             y_test,
                             scoring = 'r2',
                             cv=10,
                             n_jobs =-1).mean().round(3)


# check scores
print(f"Gradient Boosting Model Test Score {test_score}")