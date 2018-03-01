from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import KFold
from estimation import Computations
import numpy as np

start = Computations("data.csv")

data = start.data

X = np.zeros((20, 2))

X[:, 0] = data[:-2, 1]
X[:, 1] = data[:-2, 6]

y = data[:-2, 3] - data[:-2, 4] - data[:-2, 6]

regr = RandomForestRegressor(random_state=0)
regr.fit(X, y)

X_predict = np.zeros((5, 2))
X_predict[:, 0] = data[-5:, 1]
X_predict[:, 1] = data[-5:, 6]

print(regr.feature_importances_)
print(regr.predict(X_predict))
print(data[-2:, 3] - data[-2:, 4] - data[-2:, 6])



