survey=read.csv("survey.csv")
print(survey)
survey1=data.frame(X=5,Y=7)
print(survey1)
survey2=survey[1:2]
print(survey2)
library(class)
pred=knn(survey2,survey1,survey$Z,k=3)
pred

