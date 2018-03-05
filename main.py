from tkinter import *
from tkinter import filedialog, StringVar, ttk, messagebox
from estimation import Computations


def import_fl():
	"""
	Function to import the data from a file. Returns the name of the file
	selected by the user.
	"""
	global start
	file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
	start.read_fl(file)
	print(start.fl)


def import_h():
	"""
	Function to import the data from a file. Returns the name of the file
	selected by the user.
	"""
	global start
	file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
	start.read_h(file)
	print(start.h)


def import_H():
	"""
	Function to import the data from a file. Returns the name of the file
	selected by the user.
	"""
	global start
	file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
	start.read_H(file)
	print(start.H)


def import_N():
	"""
	Function to import the data from a file. Returns the name of the file
	selected by the user.
	"""
	global start
	file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
	start.read_N(file)
	print(start.N)


def main():
	"""
	Main function that runs the GUI.
	"""
	global start
	start = Computations()

	root = Tk()

	root.title("Gps Leveling Application")
	root.geometry("1100x600")

	# Create three tabs in the GUI
	# tabControl = ttk.Notebook(root)
	tab1 = Frame(root)
	# tabControl.add(tab1, text="Corrections Model Computation")
	tab1.grid(row=0, column=0)

	results_frame = Frame(root)
	results_frame.grid(row=0, column=1)

	# tab2 = Frame(tabControl,  padx=200, pady=50)
	# tabControl.add(tab2, text="Estimate Orthometric Heights")
	# tabControl.grid(row=0, column=2)
	#
	# tab3 = Frame(tabControl,  padx=200, pady=50)
	# tabControl.add(tab3, text="Variance Matrix Estimation")
	# tabControl.grid(row=0, column=3)

	# Button for importing the data
	import_data = Button(tab1, text="Import φ,λ", command=import_fl)
	import_data.grid(row=1, column=0, ipadx=30, pady=10)

	list_fl = Listbox(tab1)
	list_fl.grid(row=2, column=0, pady=10)


	# Button for importing the data
	import_data = Button(tab1, text="Import H", command=import_H)
	import_data.grid(row=1, column=1, ipadx=30, pady=10)


	list_H = Listbox(tab1)
	list_H.grid(row=2, column=1, pady=10)

	# Button for importing the data
	import_data = Button(tab1, text="Import h", command=import_h)
	import_data.grid(row=1, column=2, ipadx=30, pady=10)



	list_h = Listbox(tab1)
	list_h.grid(row=2, column=2, pady=10)


	# Button for importing the data
	import_data = Button(tab1, text="Import N", command=import_N)
	import_data.grid(row=1, column=3, ipadx=30, pady=10)


	list_N = Listbox(tab1)
	list_N.grid(row=2, column=3, pady=10)

	cut_off = Text(tab1, height=1, width=10)
	cut_off.grid(row=3, column=3, padx=10)

	def calculate():
		"""
		Function that used the estimation.py module to compute the coefficients of the
		model based on Least Squares Estimation
		"""
		global start
		print(start.fl)
		print(start.H)
		print(start.h)
		print(start.N)
		# try:
		results = start.estimation(v.get())
		display.delete(1.0, END)
		display.insert(INSERT, results)
		start.create_map()
		# except:
		# 	messagebox.showerror("Error", "The data file were in wrong format")

	# Radio Button to choose the method - model of corrections
	v = IntVar()
	choose_method = Radiobutton(results_frame, text='Model with m, σΔH and σΔΝ', variable=v, value=1)
	choose_method.grid(row=0, column=0)
	choose_method = Radiobutton(results_frame, text='Model with m and σΔN ', variable=v, value=2)
	choose_method.grid(row=1, column=0)
	choose_method = Radiobutton(results_frame, text='Model with m and σΔH', variable=v, value=3)
	choose_method.grid(row=2, column=0)
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
	display.grid(row=4, column=2)

	root.mainloop()


if __name__ == "__main__":
	main()
