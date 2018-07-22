
reddit <- read.csv('reddit.csv')
table(reddit$employment.status)


str(reddit)
summary(reddit)

levels(reddit$age.range)

#install.packages('ggplot2', dependencies = T)
library(ggplot2)
ggplot(data=reddit, x= age.range)

# Setting Levels of Ordered Factors Solution

reddit$age.range<-ordered(reddit$age.range, level=c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above"))

#changer the order for age
qplot(data=reddit, x= income.range)
reddit$income.range<-ordered(reddit$income.range,level=c("Under $20,000","$20,000 - $29,999","$30,000 - $39,999","$40,000 - $49,999","$50,000 - $69,999","$70,000 - $99,999","$100,000 - $149,999","$150,000 or more"))


