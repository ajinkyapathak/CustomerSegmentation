install.packages("clValid")
library('clValid')
mydata <- read.csv('Projects/FinalYearProject/scripts/dataset_for_comparison.csv', header = T)
express <- mydata[1:10000,3:7]
intern <- clValid(express, 3:4, clMethods=c("hierarchical","kmeans","pam"), validation="internal")
install.packages("clusteval")
library("clusteval")
pc <- princomp(data ,cor = TRUE ,scores = TRUE)

data_with_all_components = pc$scores
new_data = data_with_all_components[1:15000,1:4]
result = kmeans(new_data, centers = 4)
library('cluster')
si <- silhouette(result$cluster, dist(new_data))
si2 <- silhouette(mydata$Calculated.Segment[1:15000], dist(mydata[1:15000, 3:7]))
cluster_similarity(mydata$result.cluster, mydata$Calculated.Segment)
