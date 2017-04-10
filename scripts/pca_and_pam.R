mydata <- read.csv('Projects/FinalYearProject/scripts/dataset_for_comparison.csv', header = T)
library(cluster)
data <- mydata[2:6]
pc <- princomp(data,scores = T, cor = T)
summary(pc)
new_dimensions = pc$scores[1:30000,1:4]
clusters1 = pam(new_dimensions, k = 4)
first_half = clusters1$clustering
new_dimensions = pc$scores[30001:62929,1:4]
clusters2 = pam(new_dimensions, k = 4)
second_half = clusters2$clustering
pam.Clusters <- c(first_half, second_half)
tmp <- cbind(mydata, pam.Clusters)
write.csv(tmp, 'Projects/FinalYearProject/scripts/dataset_for_comparison.csv')
