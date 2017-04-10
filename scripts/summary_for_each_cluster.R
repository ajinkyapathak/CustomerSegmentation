mydata <- read.csv('Projects/FinalYearProject/dataset/final_data.csv', header = T)
df_result_1 = subset(mydata, (result.cluster == 1))
summary(df_result_1)

df_result_2 = subset(mydata, (result.cluster == 2))
summary(df_result_2)

df_result_3 = subset(mydata, (result.cluster == 3))
summary(df_result_3)

df_result_4 = subset(mydata, (result.cluster == 4))
summary(df_result_4)


df_segment_1 = subset(mydata, (calculated.segment == 1))
summary(df_segment_1)

df_segment_2 = subset(mydata, (Calculated.Segment == 2))
summary(df_segment_2)

df_segment_3 = subset(mydata, (Calculated.Segment == 3))
summary(df_segment_3)

df_segment_4 = subset(mydata, (Calculated.Segment == 4))
summary(df_segment_4)

df_pam_1 = subset(mydata, (pam.Clusters == 1))
summary(df_pam_1)

df_pam_2 = subset(mydata, (pam.Clusters == 2))
summary(df_pam_2)

df_pam_3 = subset(mydata, (pam.Clusters == 3))
summary(df_pam_3)

df_pam_4 = subset(mydata, (pam.Clusters == 4))
summary(df_pam_4)