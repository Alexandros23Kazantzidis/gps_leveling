import math as mp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import scipy.interpolate as sp


class Computations(object):

	def __init__(self, filename):
		self.data = np.genfromtxt(filename, delimiter=',')

	def estimation(self, col_N, method):
		"""
		Function to compute the parameters of the corrections model with
		Least Squares Estimation
		"""
		data = self.data

		# Create the measurements vector h - H - N
		measurements = np.zeros((len(data), 1))
		for i in range(0, len(data)):
			measurements[i, 0] = data[i, 3] - data[i, 4] - data[i, col_N]

		# Get the variances - errors for each point
		measur_errors = np.zeros((len(data), 1))
		for i in range(0, len(data)):
			measur_errors[i, 0] = 1/(data[i, 10]**2 + data[i, 11]**2 + 0.0757**2)

		# Create the weights matrix with the variances of each point
		weights = np.eye((len(data)))
		weights = weights * measur_errors


		# Create the state matrix based on the user's preference about the model
		if method == 1:
			A = np.ones((len(data), 3))
			A[:, 1] = data[:, 4]
			A[:, 2] = data[:, col_N]
		elif method == 2:
			A = np.ones((len(data), 2))
			A[:, 1] = data[:, col_N]
		elif method == 3:
			A = np.ones((len(data), 2))
			A[:, 1] = data[:, 4]

		# Compute the apriori variance estimation
		Cx_pre = np.dot(np.transpose(A), weights)
		Cx = np.linalg.inv(np.dot(Cx_pre, A))


		# Compute the estimation for the parameters of the model
		x_pre = np.dot(Cx, Cx_pre)
		x = np.dot(x_pre, measurements)

		# Create a Pandas Dataframe to hold the results
		if method == 1:
			val_pass = np.zeros((3, 2))
			val_pass[:, 0] = x[:, 0]
			val_pass[0, 1] = mp.sqrt(Cx[0, 0])
			val_pass[1, 1] = mp.sqrt(Cx[1, 1])
			val_pass[2, 1] = mp.sqrt(Cx[2, 2])
		elif method == 2 or method == 3:
			val_pass = np.zeros((2, 2))
			val_pass[:, 0] = x[:, 0]
			val_pass[0, 1] = mp.sqrt(Cx[0, 0])
			val_pass[1, 1] = mp.sqrt(Cx[1, 1])
		columns = ['Results', 'σx']
		if method == 1:
			rows = ['m', 'σΔΗ', 'σΔΝ']
		elif method == 2:
			rows = ['m', 'σΔΝ']
		elif method == 3:
			rows = ['m', 'σΔΗ']
		val_pass = pd.DataFrame(val_pass, index=rows, columns=columns)

		# Compute measurements estimation
		self.measurements_estimation = (np.dot(A, x))

		# Compute the error of the estimation
		self.error_estimation = measurements - self.measurements_estimation

		return val_pass

	def create_map(self):

		x, y = self.data[:, 1], self.data[:, 2]
		z = self.measurements_estimation
		X = np.linspace(np.min(x), np.max(x))
		Y = np.linspace(np.min(y), np.max(y))
		X, Y = np.meshgrid(X, Y)
		Z = sp.griddata((x, y), z, (X, Y)).reshape(50, 50)

		plt.contourf(Y, X, Z)
		plt.colorbar()
		plt.xlabel("Lon")
		plt.ylabel("Lat")
		plt.title("Correction Surface (m)")
		plt.show()


if __name__ == "__main__":

	start = Computations("data.csv")
	results = start.estimation(6, 1)
	print(results)
	# start.create_map()


