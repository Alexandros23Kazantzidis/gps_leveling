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

		self.root = Tk()

		self.root.title("Gps Leveling Application")
		self.root.geometry("1600x700")

		# Create three tabs in the GUI
		tabControl = ttk.Notebook(self.root)
		tab1 = Frame(tabControl, padx=200, pady=50)
		tabControl.add(tab1, text="Corrections Model Computation")
		tabControl.grid(row=0, column=0)

		input_frame = Frame(tab1)
		input_frame.grid(row=0, column=0)
		results_frame = Frame(tab1)
		results_frame.grid(row=1, column=0, pady=30)

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
		choose_method.grid(row=1, column=1)
		choose_method = Radiobutton(results_frame, text='Model with m and σΔN ', variable=self.v, value=2)
		choose_method.grid(row=2, column=1)
		choose_method = Radiobutton(results_frame, text='Model with m and σΔH', variable=self.v, value=3)
		choose_method.grid(row=3, column=1)
		choose_method = Radiobutton(results_frame, text='Model with m σΔφ and σΔΝ', variable=self.v, value=4)
		choose_method.grid(row=4, column=1)

		# Button to run the calculation - estimation.py
		calculate = Button(results_frame, text="Calculate Estimation", command=self.calculate)
		calculate.grid(row=5, column=0, ipadx=30, pady=10)

		# The results Text Field area that will shows us the computed values
		self.display = Text(results_frame, height=10, width=25)
		self.display.grid(row=6, column=0)

		# Button to run the calculation of variance components.py
		calculate = Button(results_frame, text="Calculate Variance Components", command=self.calculate_components)
		calculate.grid(row=5, column=2, ipadx=30, pady=10)

		# The results Text Field area that will shows us the computed values
		self.display_components = Text(results_frame, height=10, width=25)
		self.display_components.grid(row=6, column=2)

		# Button to restore the initial covariance matrix
		calculate = Button(results_frame, text="Restore Initial Covariance Matrix", command=self.restore)
		calculate.grid(row=7, column=0, ipadx=30, pady=10)

		self.root.mainloop()

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
		Function that uses the estimation.py module to compute the coefficients of the
		model based on Least Squares Estimation
		"""

		input_value = self.cut_off.get("1.0", END)
		try:
			input_value = float(input_value)
		except:
			pass
		results = self.start.estimation(self.v.get(), input_value)
		self.start.save_all_to_csv()
		self.display.delete(1.0, END)
		self.display.insert(INSERT, results)
		self.start.create_map()
		self.start.plot()

	def calculate_components(self):
		"""
		Function that uses the estimation.py module to compute the variance componenents of the
		model based on MINQUE method
		"""

		input_value = self.cut_off.get("1.0", END)
		try:
			input_value = float(input_value)
		except:
			pass
		results = self.start.variance_component(self.v.get(), input_value)
		self.display_components.delete(1.0, END)
		self.display_components.insert(INSERT, results)

		messagebox.showinfo('Update', 'The Weight Matrix has been updated')

	def restore(self):
		"""
		Function that restores the Initial Weight - Covariance Matrix from the data inputted
		"""

		self.start.restore()

		messagebox.showinfo('Update', 'The Initial Weight Matrix has been restored')


if __name__ == "__main__":

	run = MainGui()
