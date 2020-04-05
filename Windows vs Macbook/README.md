# MACHINE LEARNING - UNPSUPERVISED LEARNING
    
    Owner: Jason Lee
    Topic: Machine Learning

<p align="center">
<img src="https://github.com/jasonmchlee/machine-learning/blob/master/Windows%20vs%20Macbook/Cover%20Photo.png" width="500" height="300">
</p>    
    
# Windows vs. Macbook

Countless consumers have pondered this question when preparing to buy a new computer. As a result, Apple (AAPL) and Microsoft (MSFT) have been rigorously researching several aspects of consumer buying behavior in regards to the decision making behind this question. Both firms have commissioned research and analysis teams to study aspects such as system architecture, security, and overall performance.

Recently, Microsoft has decided to approach this question from the perspective of the Big Five personality traits as well as the Hult DNA. As such, your team has been commissioned to run an analysis on these factors. Microsoft is looking forward to receiving your key insights, as well as an organized Jupyter Notebook that can be shared with their internal analytical teams. They also have sent you a kind reminder to utilize external research to support your findings and to give details related to important information such as audience size.

The Big Five personality test measures the five personality factors that psychologists have determined are core to our personality makeup. The Five Factors of personality are:

- Openness - How open a person is to new ideas and experiences
- Conscientiousness - How goal-directed, persistent, and organized a person is
- Extraversion - How much a person is energized by the outside world
- Agreeableness - How much a person puts others' interests and needs ahead of their own
- Neuroticism - How sensitive a person is to stress and negative emotional triggers

# ANALYSIS OVERVIEW
In this analysis we will look into 392 survey responders that answered 77 questions. We will look into separating the types of questions into their Big Five personality traits. We will also separate the Hult DNA questions into 3 groups based on information provided in the Hult Handbook. Using this information we will explore the data and determine if there are any overarching insights prior to diving deeper into the analysis.

After exploration, we will organize our data and utilize unsupervised machine learning techniques - PCAs and Clustering to determine the types of customer that would purchase either a Macbook or Windows computer. Our goal is to help Microsoft determine unique customers that can be isolated and find out which customers are more inclined to remain or switch from their current laptop owned.

### Data Source: [392 Hult Graduate Students](https://github.com/jasonmchlee/machine-learning/blob/master/Windows%20vs%20Macbook/Survey_Data_Final_Exam.xlsx)

# REPORT CONTENTS

    1. Hypothesis
    2. Exploration / Cleaning
        1. Cleaning
        2. Demographics
    3. Initial Insights
    4. Data Preparation
        1. Big Five Grouping
        2. Big Five Formula
        3. Hult DNA Grouping
        4. Hult DNA Formula
        5. Correlation
    5. PCA Model
        1. Scaling Data
        2. PCA - No Max Components
        3. PCA - Limited Components
        4. Factor Loading
            1. User Personas
            2. Potential Customer Segments
    6. Clustering
        1. Scaling PCA Data
        2. Test Clusters
        3. Centroids
    7. Results
        1. Combined Results
        2. Continued Exploration
    8. Overview
        1. Insights
        2. Recommendations
    9. Sources
    
 --------------------
# OVERVIEW

Finally, after exploring demographic trends within our responders, and learning more about laptop preference we can see how the effects of Big Five personality traits and Hult DNA groupings define preference. Exploring the results of our PCAs and Cluster analysis provide insights into unique customer segments, and showcases the impact of Windows demand over time and characteristics.

## Main Insights

### Insight 1
There was an even split for both Macbook and Windows laptops; 51% of audience size for Macbook and 49% for Windows. However, there was a 7% drop; 4.9% to Macbook and the rest to Chromebook, in future laptop ownerships for Windows. In grouping the age for further analysis, Gen Z preferred purchasing a Macbook (75%: 45 users). The Windows proportion for Gen Y, declined by 9% from 53%, totaling 30 users, which is a significant drop in interest from their older customers. This indicates an overall loss in market share for Windows if laptops are the same price.

### Insight 2
Focusing on South America, there is a clear distinction in their laptop ownership. Looking at Windows laptop preference, for South America, 69% (35 users) favor a Windows laptop. Macbook prices in South America are some of the highest rates in comparison to other countries, which could be a big reason Windows computers are preferred (Nottrodt, 2020). However, despite the apparent higher prices in South America, when asked what would be their ideal next laptop, there is a decline in Windows users, falling from 69% to 52%, totaling 8 users. 

### Insight 3
Comparing the regions, we analyzed vs. the top 5 nationalities surveyed, we found:
 - All regions except Europe lose interest in Windows by an average 11%.
 - We observed Chinese, German and American students increase interest by an average of 13%.
 
Considering these factors, there is an opportunity to explore more and find final conclusions for marketing opportunities:
 - This could mean that highly educated people, in the countries mentioned above, see benefits in using Windows.
 - International students could be an interesting market for Microsoft to target.
 - Young professionals may see an added value to buying Windows early on their careers.

------------------------

## Additional Insights

### Insight 4
Focusing on genders currently, 55% (125 users) of males own a Windows, compared to 41% of females. However, looking at how males respond to their next laptop preference, males ownership of Windows laptops drop by 8% (31 users), Macbook increases by 5% (20 users), and some switch their preference to Chromebooks (12 users). There is an evident decline in male's Windows laptop preference. In comparison, females' preference Macbooks stays consistent, seeing growth in current ownership to future ownership from 59% (97 users) to 63% (104 users).

### Insight 5
Although the users from the African region only accounted for 7% (28 users) of the dataset, they had large changes in laptop preference. Current ownership for Windows laptops with African users is 43%, but when asked what they preferred for their next laptop, the proportion dropped by 15%. The total percentage of Windows laptop ownership for users from the African region dropped to 29%. We can stipulate that consumers are more interested in Macbooks if given a choice for their next laptop.

---------------------------

## Recommendation

As demand for Windows laptops generally seems to decrease for US students, the demand for some of the international students is still increasing. Additionally, the number of international students in the US was at an all-time high in 2019 ([IIE](https://www.iie.org/Why-IIE/Announcements/2019/11/Number-of-International-Students-in-the-United-States-Hits-All-Time-High)) making it a huge potential market for Windows. Especially students from China coming to the US are growing at a strong rate creating a potential market of almost 370,000 students.

Based on these facts, it is recommended to target a specific marketing campaign towards this group of students. As Microsoft is already offering a discount for international students ([EduRef](https://www.eduref.net/discount-laptops-college-students/)), we recommend broadening that campaign to collaborate with international schools offering them the opportunity to get their PCs. This could be targeted towards locking students in the long-term by making them familiar with the handling and processes within their suite. It is also recommended to broaden this campaign to include the suite for free on those discounted devices. Like that, students will be familiar with the software and might start paying for it even after their student life as part of a regular subscription, yielding return and maintaining market share for Microsoft in the long run. 


--------------------------

# SOURCES

1.	Bresman, H., & Rao, V. D. (2017, August 25). A Survey of 19 Countries Shows How Generations X, Y, and Z Are - and Aren't - Different. Retrieved from https://hbr.org/2017/08/a-survey-of-19-countries-shows-how-generations-x-y-and-z-are-and-arent-different
2.	Eriksson, L. (n.d.). What is principal component analysis (PCA) and how it is used? Retrieved from https://blog.umetrics.com/what-is-principal-component-analysis-pca-and-how-it-is-used
3.	Factor Analysis. (n.d.). Retrieved from https://www.statisticssolutions.com/factor-analysis-sem-factor-analysis/
4.	Factor Loadings. (n.d.). Retrieved from https://methods.sagepub.com/reference/encyc-of-research-design/n149.xml
5.	Jaadi, Z. (2019, September 4). A Step by Step Explanation of Principal Component Analysis. Retrieved from https://builtin.com/data-science/step-step-explanation-principal-component-analysis
6.	Mac vs PC People: Personality Traits & Aesthetic/Media Choices. (2009, November 24). Retrieved from https://kellynford.com/2009/11/24/mac-vs-pc-people-personality-traits-aestheticmedia-choices/
7.	Maklin, C. (2019, July 21). Hierarchical Agglomerative Clustering Algorithm Example In Python. Retrieved from https://towardsdatascience.com/machine-learning-algorithms-part-12-hierarchical-agglomerative-clustering-example-in-python-1e18e0075019
8.	Neuroticism. (2020, March 9). Retrieved from https://en.wikipedia.org/wiki/Neuroticism
9.	Ngo, L. (2018, December 5). How to read PCA biplots and scree plots. Retrieved from https://blog.bioturing.com/2018/06/18/how-to-read-pca-biplots-and-scree-plots/
10.	sklearn.cluster.KMeans¶. (n.d.). Retrieved from https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
11.	The Big Five Personality Test. (n.d.). Retrieved from https://openpsychometrics.org/printable/big-five-personality-test.pdf
12.	What is Extraversion? - Learn All About the Big Five Personality Traits. (n.d.). Retrieved from https://www.123test.com/personality-extraversion/
13. Nordatt (2020), Cheapest Places World Buy Apple Devices. Retrieved from https://toomanyadapters.com/cheapest-places-world-buy-apple-devices/
14. About the AuthorJordan NottrodtJordan works remotely, Author, A. the, remotely, J. N. J. works, Nottrodt, J., & remotely, J. works. (2020, February 21). The Cheapest Places in the World to Buy Apple Devices. Retrieved March 24, 2020, from https://toomanyadapters.com/cheapest-places-world-buy-apple-devices/
15. Number of International Students in the United States Hits All-Time High. (n.d.). Retrieved March 25, 2020, from https://www.iie.org/Why-IIE/Announcements/2019/11/Number-of-International-Students-in-the-United-States-Hits-All-Time-High
16. Duffin, E. (2019, November 19). International students in the U.S., by country of origin 2018/19. Retrieved March 25, 2020, from https://www.statista.com/statistics/233880/international-students-in-the-us-by-country-of-origin/
17. *, N. (n.d.). List of Manufacturers Offering Student Laptop Discounts. Retrieved March 25, 2020, from https://www.eduref.net/discount-laptops-college-students/
18. Education Store: Student Discounts & Deals - Microsoft Store. (n.d.). Retrieved March 25, 2020, from https://www.microsoft.com/en-us/store/b/education
19. Hanson, M. (2019, May 24). 71% of students would prefer a Mac to a PC – if they could afford one. Retrieved March 25, 2020, from https://www.techradar.com/news/71-of-students-would-prefer-a-mac-to-a-pc-if-they-could-afford-one
