import numpy as np
import pandas as pd



x = np.array( ((2,3), (3, 5)) )
y = np.array( ((1,2), (5, -1)) )


print(np.dot(x,y))
print(x*y)
print(np.mat(x) * np.mat(y))
#
#
# class FindOrtho(object):
#
# 	def read_model(self, filename_1):
# 		"""
# 		Function to read the model data in format of parameters and the method number
# 		(Model.csv that is the output of estimation.py)
# 		"""
# 		self.model = pd.read_csv(filename_1, sep="\t")
# 		self.model_method = self.model.iloc[-1:].values[0].tolist()[0].split(" ")[-1]
# 		self.model_parameters = self.model["Results"].dropna()
#
# 	def read_data(self, filename):
# 		"""
# 		Function to read the parameters of the model from a .csv file in the following format
# 		m σΔH σΔΝ
# 		"""
# 		data = pd.read_csv(filename, sep="\t")
# 		data = data["Unnamed: 0"].tolist()
# 		self.h = []
# 		self.H = []
# 		self.N = []
# 		flag = 0
# 		for i in range(0, len(data)-1):
# 			if data[i] == "h":
# 				flag = 1
# 			elif data[i] == "H":
# 				flag = 2
# 			elif data[i] == "N":
# 				flag = 3
#
# 			if flag == 1:
# 				self.h.append(data[i+1])
# 			elif flag == 2:
# 				self.H.append(data[i+1])
# 			elif flag == 3:
# 				self.N.append(data[i+1])
#
# 		self.h = self.h[:-1]
# 		self.H = self.H[:-1]
# 		self.N = self.N[:-1]
#
# 	def compute_ortho(self, method):
# 		"""
# 		Function to compute the orthometric heights H based on the model parameters you inputted
# 		and the model you choose from the three currently supported
# 		The three supported models are
# 		m σΔΗ σΔν
# 		m σΔν
# 		m σΔH
# 		"""
# 		if method == 1:
# 			self.H = (self.data[:, 0] - self.data[:, 1] - self.parameters[0] - self.parameters[2]*self.data[:, 1]) / (1 + self.parameters[1])
# 		elif method == 2:
# 			self.H = (self.data[:, 0] - self.data[:, 1] - self.parameters[0] - self.parameters[1] * self.data[:, 1])
# 		elif method == 3:
# 			self.H = (self.data[:, 0] - self.data[:, 1] - self.parameters[0]) / (1 + self.parameters[1])
#
# 		return self.H
#
#
# if __name__ == "__main__":
#
# 	start = FindOrtho()
# 	start.read_data("cross_validation.csv")
# 	print(len(start.h))
# 	# start.create_model("predict_ortho_data/model.csv")
# 	# print(start.compute_ortho(1))
