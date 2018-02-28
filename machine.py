from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from estimation import Computations
import numpy as np

start = Computations("data.csv")

data = start.data

X = np.zeros((20, 2))

X[:, 0] = data[:-2, 3]
X[:, 1] = data[:-2, 5]

y = data[:-2, 4]

print(y)
regr = RandomForestRegressor(random_state=0)
regr.fit(X, y)

X_predict = np.zeros((2, 2))
X_predict[:, 0] = data[-2:, 3]
X_predict[:, 1] = data[-2:, 5]

print(regr.predict(X_predict))



