improperly_labled_data <- read.csv('Projects/FinalYearProject/dataset/clustered_by_pca_kmeans.csv', header = T)
proper_lables <- read.csv('Projects/FinalYearProject/scripts/dataset_for_comparison_1.csv', header = T)
calculated.segment <- proper_lables$Calculated.Segment
data <- cbind(improperly_labled_data, calculated.segment)
write.csv(data, 'Projects/FinalYearProject/dataset/data.csv')

data$result.cluster[data$result.cluster == 1] <- 0
data$result.cluster[data$result.cluster == 3] <- 1
data$result.cluster[data$result.cluster == 0] <- 3
write.csv(data, 'Projects/FinalYearProject/dataset/final_data.csv')
library(caret)
library(e1071)
label_1 <- data$result.cluster
label_2 <- data$calculated.segment
cm <- confusionMatrix(label_1, label_2)
