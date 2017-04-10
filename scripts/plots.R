mydata <- read.csv('/home/shree/Projects/FinalYearProject/dataset/clustered_by_pca_kmeans.csv', header = T)

cluster <- mydata$result.cluster
count <- table(cluster)
barplot(count, main = 'Cluster and Its Size', xlab = 'Cluster', ylab = 'Size', col = 'light blue')


