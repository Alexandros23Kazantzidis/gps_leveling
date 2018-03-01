from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn import linear_model
from sklearn.datasets import make_regression
from sklearn.model_selection import (cross_val_score, train_test_split)
from estimation import Computations
import numpy as np
from estimation import Computations
import matplotlib.pyplot as plt

start = Computations("data.csv")

data = start.data

X = np.zeros((22, 2))
X[:, 0] = data[:, 1]
X[:, 1] = data[:, 6]

y = data[:, 3] - data[:, 4] - data[:, 6]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# clf = RandomForestRegressor(random_state=0)
# clf = linear_model.Ridge(alpha=0.5)
clf = linear_model.LinearRegression()
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))
scores = cross_val_score(clf, X, y, cv=8)
print(scores)

X_predict = np.zeros((22, 2))
X_predict[:, 0] = data[:, 1]
X_predict[:, 1] = data[:, 6]

machine_learning = clf.predict(X_predict) - y

start = Computations("data.csv")
results = start.estimation(6, 1)
parametric_model = (start.measurements_estimation - start.initial)

plt.plot(np.abs(machine_learning), color='b')
plt.plot(np.abs(parametric_model), color='r')
plt.show()




#
# regr.fit(X, y)
#
# X_predict = np.zeros((5, 2))
# X_predict[:, 0] = data[-5:, 1]
# X_predict[:, 1] = data[-5:, 6]
#
# print(regr.feature_importances_)
# print(regr.predict(X_predict))
# print(data[-2:, 3] - data[-2:, 4] - data[-2:, 6])
#


