from tkinter import *
from tkinter import filedialog, StringVar, ttk, messagebox
from estimation import Computations


def import_file():
	"""
	Function to import the data from a file. Returns the name of the file
	selected by the user.
	"""
	global start
	file = filedialog.askopenfilename(initialdir="/Home", title="Select file")
	start = Computations(file)
	return start


def main():
	"""
	Main function that runs the GUI.
	"""
	root = Tk()

	root.title("Gps Leveling Application")
	root.geometry("800x600")

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

	# Button for importing the data
	import_data = Button(tab1, text="Import Data", command=import_file)
	import_data.grid(row=1, column=0, ipadx=30, pady=10)

	# The results Text Field area that will shows us the computed values
	display = Text(tab1, height=10, width=25)
	display.grid(row=7, column=0)

	def calculate():
		"""
		Function that used the estimation.py module to compute the coefficients of the
		model based on Least Squares Estimation
		"""
		global start
		if gravity.get() == "EGM08(260)":
			gravity_number = 5
		elif gravity.get() == "EGM08(2159)":
			gravity_number = 6
		elif gravity.get() == "EIGEN6c2(260)":
			gravity_number = 7
		elif gravity.get() == "EIGEN6c2(1949)":
			gravity_number = 8
		else:
			gravity_number = 9

		try:
			results = start.estimation(gravity_number, v.get())
			display.delete(1.0, END)
			display.insert(INSERT, results)

			start.create_map()
		except:
			messagebox.showerror("Error", "The data file were in wrong format")

	# Radio Button to choose the method - model of corrections
	v = IntVar()
	choose_method = Radiobutton(tab1, text='Model with m, σΔH and σΔΝ', variable=v, value=1)
	choose_method.grid(row=2, column=0)
	choose_method = Radiobutton(tab1, text='Model with m and σΔN ', variable=v, value=2)
	choose_method.grid(row=3, column=0)
	choose_method = Radiobutton(tab1, text='Model with m and σΔH', variable=v, value=3)
	choose_method.grid(row=4, column=0)

	# Dropdown Menu to choose which Gravity model to use
	gravity = StringVar()
	gravity.set("EGM08(260)")
	option = OptionMenu(tab1, gravity, "EGM08(260)", "EGM08(2159)", "EIGEN6c2(260)", "EIGEN6c2(1949)", "NDIR-R4(260)")
	option.grid(row=5, column=0, pady=5)

	# Button to run the calculation - estimation.py
	calculate = Button(tab1, text="Calculate", command=calculate)
	calculate.grid(row=6, column=0, ipadx=30, pady=10)

	root.mainloop()


if __name__ == "__main__":
	main()
