import math as mp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import scipy.interpolate as sp
import time


class Computations(object):

	def read_fl(self, filename):
		"""
		Function to read the geographic coordinates φ,λ of the points
		"""
		self.fl = np.genfromtxt(filename, delimiter=',')

	def read_H(self, filename):
		"""
		Function to read the orthometric height H of the points
		"""
		self.H = np.genfromtxt(filename, delimiter=',')

	def read_h(self, filename):
		"""
		Function to read the geometric height h of the points
		"""
		self.h = np.genfromtxt(filename, delimiter=',')

	def read_N(self, filename):
		"""
		Function to read the geoid height N of the points
		"""
		self.N = np.genfromtxt(filename, delimiter=',')

	def estimation(self, method, cut_off=0):
		"""
		Function to compute the parameters of the corrections model with
		Least Squares Estimation
		"""
		self.method = method

		# Create the measurements vector h - H - N
		measurements = np.zeros((len(self.H), 1))
		for i in range(0, len(self.H)):
			measurements[i, 0] = self.h[i, 0] - self.H[i, 0] - self.N[i, 0]
		self.initial = measurements[:]

		# Choose the right error for the geoid heights based on the model
		try:
			self.N[:, 1] = self.N[:, 1] + cut_off
		except:
			pass

		# Get the variances - errors for each point
		measur_errors = np.zeros((len(self.H), 1))
		for i in range(0, len(self.H)):
			measur_errors[i, 0] = 1/(self.h[i, 1]**2 + self.H[i, 1]**2 + self.N[i, 1]**2)

		# Create the weights matrix with the variances of each point
		weights = np.eye((len(self.H)))
		weights = weights * measur_errors

		# Create the state matrix based on the user's preference about the model
		if method == 1:
			A = np.ones((len(self.H), 3))
			A[:, 1] = self.H[:, 0]
			A[:, 2] = self.N[:, 0]
		elif method == 2:
			A = np.ones((len(self.H), 2))
			A[:, 1] = self.N[:, 0]
		elif method == 3:
			A = np.ones((len(self.H), 2))
			A[:, 1] = self.H[:, 0]

		# Compute the apriori variance estimation
		Cx_pre = np.matmul(np.transpose(A), weights)
		Cx = np.linalg.inv(np.matmul(Cx_pre, A))

		# Compute the estimation for the parameters of the model
		x_pre = np.matmul(Cx_pre, measurements)
		self.x = np.matmul(Cx, x_pre)

		# Create a Pandas Dataframe to hold the results
		if method == 1:
			val_pass = np.zeros((3, 2))
			val_pass[:, 0] = self.x[:, 0]
			val_pass[0, 1] = mp.sqrt(Cx[0, 0])
			val_pass[1, 1] = mp.sqrt(Cx[1, 1])
			val_pass[2, 1] = mp.sqrt(Cx[2, 2])
		elif method == 2 or method == 3:
			val_pass = np.zeros((2, 2))
			val_pass[:, 0] = self.x[:, 0]
			val_pass[0, 1] = mp.sqrt(Cx[0, 0])
			val_pass[1, 1] = mp.sqrt(Cx[1, 1])
		columns = ['Results', 'σx']
		if method == 1:
			rows = ['m', 'σΔΗ', 'σΔΝ']
		elif method == 2:
			rows = ['m', 'σΔΝ']
		elif method == 3:
			rows = ['m', 'σΔΗ']
		self.val_pass = pd.DataFrame(val_pass, index=rows, columns=columns)

		# Compute measurements estimation
		self.measurements_estimation = (np.matmul(A, self.x))

		# Compute the error of the estimation
		self.error_estimation = measurements - self.measurements_estimation

		return self.val_pass

	def create_map(self):
		"""
		Function to create a grid - contour map of the correction surface of the model
		"""

		x, y = self.fl[:, 0], self.fl[:, 1]
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
		plt.show(block=False)
		time.sleep(1)

	def plot(self):
		"""
		Function to create two plots, one for the initial and after LSE measurements
		and one for the estimation errors of the model
		"""

		f, axarr = plt.subplots(2, figsize=(7,10))
		f.subplots_adjust(hspace=0.5)
		axarr[0].plot(self.initial, color='b', label='Initial')
		axarr[0].plot(self.measurements_estimation, color='r', label='After LSE')
		axarr[0].set_title("Initial differences - After LSE differences")
		axarr[0].set_ylabel("h - H - N (m)")
		axarr[0].legend()

		axarr[1].plot(self.error_estimation, color='b', label='Estimation Error')
		axarr[1].set_title("Error estimation")
		axarr[1].set_ylabel("Error (m)")
		axarr[1].legend()

		plt.show()

	def save_all_to_csv(self):
		"""
		Function to output results to a .csv file
		"""

		df = pd.DataFrame(self.initial, columns=["Initial_Dif"])
		df = df.assign(After_LSE_Dif=self.measurements_estimation)
		df = df.assign(Estimation_Errors=self.error_estimation)
		df.index.name = "Points"
		self.val_pass.to_csv("Results.csv", sep="\t")
		with open('Results.csv', 'a') as f:
			df.to_csv(f, header=True, sep="\t")

		statistics = np.zeros((4, 3))
		statistics[0, 0] = np.mean(self.initial)
		statistics[1, 0] = np.std(self.initial)
		statistics[2, 0] = np.max(self.initial)
		statistics[3, 0] = np.min(self.initial)
		statistics[0, 1] = np.mean(self.measurements_estimation)
		statistics[1, 1] = np.std(self.measurements_estimation)
		statistics[2, 1] = np.max(self.measurements_estimation)
		statistics[3, 1] = np.min(self.measurements_estimation)
		statistics[0, 2] = np.mean(self.error_estimation)
		statistics[1, 2] = np.std(self.error_estimation)
		statistics[2, 2] = np.max(self.error_estimation)
		statistics[3, 2] = np.min(self.error_estimation)

		df_1 = pd.DataFrame(statistics, index=["Mean", "STD", "Max", 'Min'],
		columns=["Initial_Dif", "After_LSE_Dif", "Estimation_errors"])
		with open('Results.csv', 'a') as f:
			df_1.to_csv(f, header=True, sep="\t")

	# def save_model_to_csv(self):
	# 	"""
	# 	Function to save only the parameters of the model
	# 	"""
	#
	# 	self.val_pass.to_csv("cross_validation.csv", sep="\t")
	# 	with open('cross_validation.csv', 'a') as f:
	# 		f.write("Method used: " + str(self.method))
	# 		f.write("\n" + "h" + "\n")
	# 		np.savetxt(f, self.h[:, 0])
	# 		f.write("\n" + "H" + "\n")
	# 		np.savetxt(f, self.H[:, 0])
	# 		f.write("\n" + "N" + "\n")
	# 		np.savetxt(f, self.N[:, 0])

	def cross_validation(self, method, cut_off=0):

		initial_h = np.copy(self.h)
		initial_H = np.copy(self.H)
		initial_N = np.copy(self.N)
		accuracy = []

		for i in range(0, len(self.h)-1):

			working_h = np.copy(initial_h)
			working_H = np.copy(initial_H)
			working_N = np.copy(initial_N)

			self.h = np.delete(working_h, i, 0)
			self.H = np.delete(working_H, i, 0)
			self.N = np.delete(working_N, i, 0)

			true_H = self.H[i, 0]

			self.estimation(method, cut_off)

			if method == 1:
				predicted = (self.h[i, 0] - self.N[i, 0] - self.x[0] - self.x[2] * self.N[i, 0]) / (1 + self.x[1])
			elif method == 2:
				predicted = (self.h[i, 0] - self.N[i, 0] - self.x[0] - self.x[1] * self.N[i, 0])
			elif method == 3:
				predicted = (self.h[i, 0] - self.N[i, 0] - self.x[0]) / (1 + self.x[1])

			accuracy.append((predicted - true_H)[0])

		return accuracy


if __name__ == "__main__":

	start = Computations()
	start.read_fl("model_data/fl.csv")
	start.read_H("model_data/H_ortho.csv")
	start.read_h("model_data/h_data.csv")
	start.read_N("model_data/N_egm.csv")
	# results = start.estimation(1)
	# print(np.mean(start.initial))
	# print(np.std(start.initial))
	# print(np.mean(start.measurements_estimation))
	# print(np.std(start.measurements_estimation))
	# print(results)
	# start.save_model_to_csv()
	accuracy = start.cross_validation(2)
	print(accuracy)
	plt.plot(accuracy)
	plt.plot(start.error_estimation[1:])
	plt.show()

