library(quantreg)
library(ggplot2)
library(rpart)
library(rpart.plot)
library(ROCR)
library(plotly)
library(readxl)


####### GERMAN CREDIT CARD ##############
mydf <- read_excel("german credit card.xls")
mydf$purpose <- as.numeric(replace(mydf$purpose, "", "x"))[1:1000]
mydf$good_bad <- gsub("good", "1", mydf$good_bad)
mydf$good_bad <- gsub("bad", "0", mydf$good_bad)
mydf$good_bad <- as.numeric(mydf$good_bad)


############ LINEAR REGREESSION ON ALL DATA ##############
my_lin <- lm(amount~age+purpose, data=mydf) 
summary(my_lin)


rq_ger <- rq(amount~age, data=mydf, tau=.9)
summary(rq_ger)


##################### LOGISTIC REGRESSION AND DECISION TREE#############

#taking a look at german credit: logistic vs. tree

# GERMAN TREE
ger_tree <- rpart(good_bad~age+amount+checking+duration+savings, 
                  data=mydf, method="class")
rpart.plot(ger_tree, extra=1, type=1)


# GERMAN LOGISTIC
ger_logit <- glm(good_bad~age+amount+checking+duration+savings, 
                 data=mydf, family="binomial")
summary(ger_logit)

# PREDICT
predict_tree <- predict(ger_tree, mydf, type="prob")
predict_logit<- predict(ger_logit, mydf, type="response")

#PREDICITION
pred_val_tree <- prediction(predict_tree[,2], mydf$good_bad)
pred_val_logit <- prediction(predict_logit, mydf$good_bad)

#PERFORMACE
perf_tree <- performance(pred_val_tree, "tpr", "fpr")
perf_logit <- performance(pred_val_logit, "tpr", "fpr")

# PLOT
plot(perf_tree, col="black")
plot(perf_logit, col="blue", add=TRUE)

# Fairly even with logistic regression showing better performance but eventually the decision tree is better

