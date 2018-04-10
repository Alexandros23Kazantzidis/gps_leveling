from tkinter import *
from tkinter import filedialog, StringVar, ttk, messagebox
from estimation import Computations
import numpy as np


class MainGui(object):
	"""
	Main class that creates and runs the GUI.
	"""

	def __init__(self):

		self.start = Computations()

		root = Tk()

		root.title("Gps Leveling Application")
		root.geometry("1600x700")

		# Create three tabs in the GUI
		tabControl = ttk.Notebook(root)
		tab1 = Frame(tabControl, padx=200, pady=50)
		tabControl.add(tab1, text="Corrections Model Computation")
		tabControl.grid(row=0, column=0)

		tab2 = Frame(tabControl,  padx=200, pady=50)
		tabControl.add(tab2, text="Prediction Cross Validation")
		tabControl.grid(row=0, column=0)

		tab3 = Frame(tabControl,  padx=200, pady=50)
		tabControl.add(tab3, text="Variance Component Estimation")
		tabControl.grid(row=0, column=0)

		input_frame = Frame(tab1)
		input_frame.grid(row=0, column=0)

		results_frame = Frame(tab1)
		results_frame.grid(row=1, column=0, pady=30)

		input_frame_2 = Frame(tab2)
		input_frame_2.grid(row=0, column=0)

		results_frame_2 = Frame(tab2)
		results_frame_2.grid(row=1, column=0, pady=30)

		# Button for importing the data
		import_data = Button(input_frame, text="Import φ,λ", command=self.import_fl)
		import_data.grid(row=1, column=0, ipadx=30, pady=10)

		info_label_fl = Label(input_frame, text="Format = Φ, Λ")
		info_label_fl.grid(row=2, column=0)

		self.list_fl = Text(input_frame, height=10, width=26)
		self.list_fl.grid(row=3, column=0, pady=10)

		# Button for importing the data
		import_data = Button(input_frame, text="Import H", command=self.import_H)
		import_data.grid(row=1, column=1, ipadx=30, pady=10)

		info_label_H = Label(input_frame, text="Format = H, σ")
		info_label_H.grid(row=2, column=1)

		self.list_H = Text(input_frame, height=10, width=30)
		self.list_H.grid(row=3, column=1, pady=10)

		# Button for importing the data
		import_data = Button(input_frame, text="Import h", command=self.import_h)
		import_data.grid(row=1, column=2, ipadx=30, pady=10)

		info_label_h = Label(input_frame, text="Format = h, σ")
		info_label_h.grid(row=2, column=2)

		self.list_h = Text(input_frame, height=10, width=30)
		self.list_h.grid(row=3, column=2, pady=10)

		# Button for importing the data
		import_data = Button(input_frame, text="Import N", command=self.import_N)
		import_data.grid(row=1, column=3, ipadx=30, pady=10)

		info_label_N = Label(input_frame, text="Format = N, σ")
		info_label_N.grid(row=2, column=3)

		self.list_N = Text(input_frame, height=10, width=20)
		self.list_N.grid(row=3, column=3, pady=10)

		info_label_cut_off = Label(input_frame, text="Input the cutoff error of the model")
		info_label_cut_off.grid(row=4, column=3)

		self.cut_off = Text(input_frame, height=1, width=10)
		self.cut_off.grid(row=5, column=3, padx=10)

		# Radio Button to choose the method - model of corrections
		self.v = IntVar()
		choose_method = Radiobutton(results_frame, text='Model with m, σΔH and σΔΝ', variable=self.v, value=1)
		choose_method.grid(row=1, column=0)
		choose_method = Radiobutton(results_frame, text='Model with m and σΔN ', variable=self.v, value=2)
		choose_method.grid(row=2, column=0)
		choose_method = Radiobutton(results_frame, text='Model with m and σΔH', variable=self.v, value=3)
		choose_method.grid(row=3, column=0)

		# Button to run the calculation - estimation.py
		calculate = Button(results_frame, text="Calculate", command=self.calculate)
		calculate.grid(row=4, column=0, ipadx=30, pady=10)

		# The results Text Field area that will shows us the computed values
		self.display = Text(results_frame, height=10, width=25)
		self.display.grid(row=5, column=0)






		# Tab 2 Estimate Orthometric Heights

		# Import the model parameters
		import_data = Button(input_frame_2, text="Import Model", command=self.import_parameters)
		import_data.grid(row=0, column=0, ipadx=20, pady=10)

		info_label_h = Label(input_frame_2, text="Format = m, σΔH, σΔN")
		info_label_h.grid(row=1, column=0)

		self.list_model = Text(input_frame_2, height=10, width=16)
		self.list_model.grid(row=2, column=0, pady=10)

		# Import the data (h,N)
		import_data = Button(input_frame_2, text="Import Data", command=self.import_data)
		import_data.grid(row=0, column=1, ipadx=30, pady=10)

		info_label_h = Label(input_frame_2, text="Format = h, N")
		info_label_h.grid(row=1, column=1)

		self.list_data = Text(input_frame_2, height=10, width=20)
		self.list_data.grid(row=2, column=1, pady=10)

		# Button to run the calculation - ortho.py
		calculate_2 = Button(results_frame_2, text="Calculate Orthometric", command=self.calculate_ortho)
		calculate_2.grid(row=4, column=2, ipadx=30, pady=10)

		# The results Text Field area that will shows us the computed values
		self.display_2 = Text(results_frame_2, height=10, width=13)
		self.display_2.grid(row=5, column=2)

		info_label_h = Label(results_frame_2, text="What kind of model have you inputted?")
		info_label_h.grid(row=0, column=2)

		# Radio Button for the user to select the model that he has inputted
		self.method_var = IntVar()
		choose_method = Radiobutton(results_frame_2, text='Model with m, σΔH and σΔΝ', variable=self.method_var, value=1)
		choose_method.grid(row=1, column=2)
		choose_method = Radiobutton(results_frame_2, text='Model with m and σΔN ', variable=self.method_var, value=2)
		choose_method.grid(row=2, column=2)
		choose_method = Radiobutton(results_frame_2, text='Model with m and σΔH', variable=self.method_var, value=3)
		choose_method.grid(row=3, column=2)

		root.mainloop()






	def calculate_ortho(self):
		"""
		Function to compute the orthometric heights from the model and the h,N
		"""

		results = self.start_2.compute_ortho(self.method_var.get())
		self.display_2.delete(1.0, END)
		self.display_2.insert(INSERT, results)

	def import_parameters(self):
		"""
		Function to import the model parameters from a file. Returns the name of the file
		selected by the user.
		"""

		file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
		self.start_2.create_model(file)
		self.list_model.delete(1.0, END)
		self.list_model.insert(INSERT, self.start_2.parameters[:])

	def import_data(self):
		"""
		Function to import the data h,N from a file. Returns the name of the file
		selected by the user.
		"""

		file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
		self.start_2.read_data(file)
		self.list_data.delete(1.0, END)
		self.list_data.insert(INSERT, self.start_2.data[:])

	def import_fl(self):
		"""
		Function to import the φ,λ from a file. Returns the name of the file
		selected by the user.
		"""

		file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
		self.start.read_fl(file)
		self.list_fl.delete(1.0, END)
		self.list_fl.insert(INSERT, self.start.fl[:])

	def import_h(self):
		"""
		Function to import the h from a file. Returns the name of the file
		selected by the user.
		"""

		file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
		self.start.read_h(file)
		self.list_h.delete(1.0, END)
		self.list_h.insert(INSERT, self.start.h[:])

	def import_H(self):
		"""
		Function to import the H from a file. Returns the name of the file
		selected by the user.
		"""

		file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
		self.start.read_H(file)
		self.list_H.delete(1.0, END)
		self.list_H.insert(INSERT, self.start.H[:])

	def import_N(self):
		"""
		Function to import the N from a file. Returns the name of the file
		selected by the user.
		"""

		file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
		self.start.read_N(file)
		self.list_N.delete(1.0, END)
		self.list_N.insert(INSERT, self.start.N[:])

	def calculate(self):
		"""
		Function that used the estimation.py module to compute the coefficients of the
		model based on Least Squares Estimation
		"""

		input_value = self.cut_off.get("1.0", END)
		try:
			input_value = float(input_value)
		except:
			pass
		results = self.start.estimation(self.v.get(), input_value)
		self.start.save_model_to_csv()
		self.start.save_all_to_csv()
		self.display.delete(1.0, END)
		self.display.insert(INSERT, results)
		self.start.create_map()
		self.start.plot()


if __name__ == "__main__":

	run = MainGui()
