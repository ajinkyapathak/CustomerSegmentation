from sklearn.externals import joblib

clf = joblib.load('finalized_naive_bayes.sav')

x = [[1, 6, 10950, 0, 16]]

from sklearn import preprocessing
x = preprocessing.scale(x)
print x
y = clf.predict(x)
print y
