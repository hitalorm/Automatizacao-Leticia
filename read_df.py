import pandas as pd
from sklearn import svm
from sklearn import cross_validation
import numpy as np

df = pd.read_pickle('dataframe.dat')



matrix = df.as_matrix()

energy_depos = matrix[:,[4]]
print(energy_depos[energy_depos==0])

##X = matrix[:,[0,1,2,3]]
##y = matrix[:,4]
##
##
##X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.1, random_state=1)
##
##
##
##clf = svm.SVR(kernel='rbf', C=1e3, gamma=0.1)


#print(clf.score(X_test, y_test))



