import pandas as pd
data = pd.DataFrame.from_csv('~/Projects/FinalYearProject/customer_segmentation.csv')

print data.groupby(['Segment', 'Crop'])['Farmer'].count()
