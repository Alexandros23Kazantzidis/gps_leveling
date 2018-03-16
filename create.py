import numpy as np

data = np.genfromtxt("data.csv", delimiter=",")

fl = np.zeros((len(data), 2))
fl[:, 0] = data[:, 9]
fl[:, 1] = np.ones(len(data)) * 0.0437


np.savetxt("N_ndir.csv", fl, delimiter=",")