import numpy as np


class FindOrtho(object):

	def read_data(self, filename_1):
		self.data = np.genfromtxt(filename_1, delimiter=",")

	def create_model(self, filename):
		self.parameters = np.genfromtxt(filename, delimiter="\t")

	def compute_ortho(self, method):
		if method == 1:
			self.H = (self.data[:, 0] - self.data[:, 1] - self.parameters[0] - self.parameters[2]*self.data[:, 1]) / (1 + self.parameters[1])
		elif method == 2:
			self.H = (self.data[:, 0] - self.data[:, 1] - self.parameters[0] - self.parameters[1] * self.data[:, 1])
		elif method == 3:
			self.H = (self.data[:, 0] - self.data[:, 1] - self.parameters[0]) / (1 + self.parameters[1])

		return self.H


if __name__ == "__main__":

	start = FindOrtho()
	start.read_data("predict_ortho_data/data.csv")
	start.create_model("predict_ortho_data/model.csv")
	print(start.compute_ortho(1))
