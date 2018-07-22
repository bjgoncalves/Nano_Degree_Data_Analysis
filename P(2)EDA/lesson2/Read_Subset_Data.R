getwd()
setwd('C:/Users/Alex-PC/Desktop/Udacity/NanoDegree Data Analytics/P(2)EDA/lesson2')

stateinfo <- read.csv('stateData.csv')

##Subseting the dataset
stateSubset<- subset(stateinfo,state.region == 1 )
head(stateSubset)
dim(stateSubset)


#stateinfo[ROWS,COLUMNS]
stateSubsetBracket <- stateinfo[stateinfo$state.region == 1, ]
head(stateSubset)
dim(stateSubset)

##Subsetting 
##Which state has illiteracy rate of .50% ?

colnames(stateinfo)

subset(stateinfo, illiteracy ==.5)

##Which States has high school graduation of above 50%?
colnames(stateinfo)

subset(stateinfo, highSchoolGrad >50)






