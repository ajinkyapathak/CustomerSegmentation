data <- read.csv('Projects/FinalYearProject/customer_segmentation.csv', header = T)
summary(data)
normalize <- function(x){
  num <- x- min(x)
  denom <- max(x)-min(x)
  return(num/denom)
}

unnormalized_data1 <- data[,8:14]
unnormalized_data2 <- scale(unnormalized_data1[,1:6])
unnormalized_data <- cbind(unnormalized_data2, unnormalized_data1[,7])
normalized_data <- as.data.frame(lapply(unnormalized_data1[,1:6], normalize))
set.seed(1234567)

ind <- sample(2, nrow(data), replace=TRUE, prob=c(0.67, 0.33))

data.training <- normalized_data[ind==1, 1:6]
data.test <- normalized_data[ind==2, 1:6]

data.trainLabels <- unnormalized_data[ind==1, 7]
data.testLabels <- unnormalized_data[ind==2, 7]

library(caret)
set.seed(7)
fit.lda <- train(data.trainLabels~., data=data.training, method="lda")



dataset = cbind(normalized_data, unnormalized_data1[,7])
colnames(dataset) <- c("App.Customer","Orders.Count","Net.Orders.Count","Net.Revenue","Return.Percentage","Days.Since.Last.Bought", "Segment")


# create a list of 80% of the rows in the original dataset we can use for training
validation_index <- createDataPartition(dataset$Segment, p=0.80, list=FALSE)
# select 20% of the data for validation
validation <- dataset[-validation_index,]
# use the remaining 80% of data to training and testing the models
dataset <- dataset[validation_index,]


# dimensions of dataset
dim(dataset)


# list types for each attribute
sapply(dataset, class)

# summarize the class distribution
percentage <- prop.table(table(dataset$Segment)) * 100
cbind(freq=table(dataset$Segment), percentage=percentage)

x = dataset[,1:6]
y = dataset[,7]



# boxplot for each attribute on one image
par(mfrow=c(1,4))
for(i in 1:4) {
  boxplot(x[,i], main=names(iris)[i])
}


# boxplot for each attribute on one image
par(mfrow=c(1,6))
for(i in 1:6) {
  boxplot(x[,i], main=names(dataset)[i])
}


# barplot for class breakdown
plot(y)
histogram(y)



# scatterplot matrix
featurePlot(x=x, y=y, plot="ellipse")
featurePlot(x=x, y=y, plot="box")


# Run algorithms using 10-fold cross validation
control <- trainControl(method="cv", number=10)
metric <- "Accuracy"




# a) linear algorithms
set.seed(7)
fit.lda <- train(Segment~., data=dataset, method="lda", metric=metric, trControl=control)
# b) nonlinear algorithms
# CART
set.seed(7)
fit.cart <- train(Segment~., data=dataset, method="rpart", trControl=control)
# kNN
set.seed(7)
fit.knn <- train(Segment~., data=dataset, method="knn", trControl=control)
# c) advanced algorithms
# SVM
set.seed(7)
fit.svm <- train(Segment~., data=dataset, method="svmRadial", trControl=control)
# Random Forest
set.seed(7)
fit.rf <- train(Segment~., data=dataset, method="rf", metric=metric, trControl=control)
