mydata <- read.csv("~/Projects/FinalYearProject/dataset/dataset.csv", header = T)

head(mydata)
data <- mydata[,18:22]

write.csv(data, "modified_dataset.csv")
pc <- princomp(data ,cor = TRUE ,scores = TRUE)
summary(pc)
pc$loadings
data_with_all_components = pc$scores
new_data = data_with_all_components[,1:4]
result = kmeans(new_data, centers = 4)
tmp <- cbind(data, result$cluster)
write.csv(tmp, "dataset_with_cluters.csv")
