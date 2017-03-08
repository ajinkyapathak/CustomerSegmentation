mydata <- read.csv("Projects/FinalYearProject/dataset/dataset.csv", header = TRUE)
mydata <- na.omit(mydata) # listwise deletion of missing
mydata <- scale(mydata) # standardize variables

total_orders <- mydata$Total.Orders
result <- kmeans(total_orders,4)
result$size
result$cluster
dunn_score <- dunn.test(result$cluster, method = "bonferroni")
