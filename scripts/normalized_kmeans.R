mydata <- read.csv("~/Projects/FinalYearProject/dataset/dataset.csv", header = T)
data <- mydata[,19:22]
scaled.data <- scale(data)

norm <- function(x){x/max(x)}
norm1 <- function(x){- x/max(x)}

normalized_orders = norm(data$Net.Orders)
normalized_net_revenue = norm(data$Net.Revenue)
normalized_return_percentage = norm1(data$Return.Percentage)
normalized_last_bought_on = norm1(data$Last.Bought.on)

tmp_data <- cbind(normalized_orders, normalized_net_revenue, normalized_return_percentage, normalized_last_bought_on)

km <- kmeans(tmp_data, 4)
library(cluster)
sh <-silhouette(km$cluster[1:15000], dist(tmp_data[1:15000]))
