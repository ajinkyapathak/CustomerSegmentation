from pandas import DataFrame
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import decomposition
import matplotlib.pyplot as plt

data = pd.read_csv('~/Projects/FinalYearProject/customer_segmentation.csv', low_memory=False)
data = data.as_matrix()
print data.shape

feature1 = data[:, 7:8]
feature2 = data[:, 9:12]
features = np.concatenate((feature1,feature2), axis=1)
print features.shape

labels = data[:, 13].ravel()
print labels.shape