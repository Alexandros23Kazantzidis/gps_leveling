from tkinter import *
from tkinter import filedialog, StringVar, ttk, messagebox
from estimation import Computations


def main():
	"""
	Main function that runs the GUI.
	"""

	def import_fl():
		"""
		Function to import the data from a file. Returns the name of the file
		selected by the user.
		"""
		global start
		file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
		start.read_fl(file)
		list_fl.delete(1.0, END)
		list_fl.insert(INSERT, start.fl[:])

	def import_h():
		"""
		Function to import the data from a file. Returns the name of the file
		selected by the user.
		"""
		global start
		file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
		start.read_h(file)
		list_h.delete(1.0, END)
		list_h.insert(INSERT, start.h[:])

	def import_H():
		"""
		Function to import the data from a file. Returns the name of the file
		selected by the user.
		"""
		global start
		file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
		start.read_H(file)
		list_H.delete(1.0, END)
		list_H.insert(INSERT, start.H[:])

	def import_N():
		"""
		Function to import the data from a file. Returns the name of the file
		selected by the user.
		"""
		global start
		file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
		start.read_N(file)
		list_N.delete(1.0, END)
		list_N.insert(INSERT, start.N[:])


	global start
	start = Computations()

	root = Tk()

	root.title("Gps Leveling Application")
	root.geometry("1600x700")

	# Create three tabs in the GUI
	tabControl = ttk.Notebook(root)
	tab1 = Frame(tabControl, padx=200, pady=50)
	tabControl.add(tab1, text="Corrections Model Computation")
	tabControl.grid(row=0, column=0)

	tab2 = Frame(tabControl,  padx=200, pady=50)
	tabControl.add(tab2, text="Estimate Orthometric Heights")
	tabControl.grid(row=0, column=0)

	tab3 = Frame(tabControl,  padx=200, pady=50)
	tabControl.add(tab3, text="Variance Matrix Estimation")
	tabControl.grid(row=0, column=0)

	input_frame = Frame(tab1)
	input_frame.grid(row=0, column=0)

	results_frame = Frame(tab1)
	results_frame.grid(row=1, column=0, pady=30)


	# Button for importing the data
	import_data = Button(input_frame, text="Import φ,λ", command=import_fl)
	import_data.grid(row=1, column=0, ipadx=30, pady=10)

	info_label_fl = Label(input_frame, text="Format = Φ, Λ")
	info_label_fl.grid(row=2, column=0)

	list_fl = Text(input_frame, height=10, width=26)
	list_fl.grid(row=3, column=0, pady=10)


	# Button for importing the data
	import_data = Button(input_frame, text="Import H", command=import_H)
	import_data.grid(row=1, column=1, ipadx=30, pady=10)

	info_label_H = Label(input_frame, text="Format = H, σ")
	info_label_H.grid(row=2, column=1)

	list_H = Text(input_frame, height=10, width=30)
	list_H.grid(row=3, column=1, pady=10)

	# Button for importing the data
	import_data = Button(input_frame, text="Import h", command=import_h)
	import_data.grid(row=1, column=2, ipadx=30, pady=10)

	info_label_h = Label(input_frame, text="Format = h, σ")
	info_label_h.grid(row=2, column=2)

	list_h = Text(input_frame, height=10, width=30)
	list_h.grid(row=3, column=2, pady=10)

	# Button for importing the data
	import_data = Button(input_frame, text="Import N", command=import_N)
	import_data.grid(row=1, column=3, ipadx=30, pady=10)

	info_label_N = Label(input_frame, text="Format = N, σ")
	info_label_N.grid(row=2, column=3)

	list_N = Text(input_frame, height=10, width=20)
	list_N.grid(row=3, column=3, pady=10)

	info_label_cut_off = Label(input_frame, text="Input the cutoff error of the model")
	info_label_cut_off.grid(row=4, column=3)

	cut_off = Text(input_frame, height=1, width=10)
	cut_off.grid(row=5, column=3, padx=10)

	def calculate():
		"""
		Function that used the estimation.py module to compute the coefficients of the
		model based on Least Squares Estimation
		"""
		global start
		input_value = cut_off.get("1.0", END)
		try:
			input_value = float(input_value)
		except:
			pass
		results = start.estimation(v.get(), input_value)
		display.delete(1.0, END)
		display.insert(INSERT, results)
		start.create_map()
		start.plot()

		# 	messagebox.showerror("Error", "The data file were in wrong format")

	# Radio Button to choose the method - model of corrections
	v = IntVar()
	choose_method = Radiobutton(results_frame, text='Model with m, σΔH and σΔΝ', variable=v, value=1)
	choose_method.grid(row=1, column=0)
	choose_method = Radiobutton(results_frame, text='Model with m and σΔN ', variable=v, value=2)
	choose_method.grid(row=2, column=0)
	choose_method = Radiobutton(results_frame, text='Model with m and σΔH', variable=v, value=3)
	choose_method.grid(row=3, column=0)

	# #
	# # Dropdown Menu to choose which Gravity model to use
	# gravity = StringVar()
	# gravity.set("EGM08(260)")
	# option = OptionMenu(tab1, gravity, "EGM08(260)", "EGM08(2159)", "EIGEN6c2(260)", "EIGEN6c2(1949)", "NDIR-R4(260)")
	# option.grid(row=5, column=0, pady=5)

	# Button to run the calculation - estimation.py
	calculate = Button(results_frame, text="Calculate", command=calculate)
	calculate.grid(row=4, column=0, ipadx=30, pady=10)

	# The results Text Field area that will shows us the computed values
	display = Text(results_frame, height=10, width=25)
	display.grid(row=5, column=0)

	root.mainloop()


if __name__ == "__main__":
	main()
