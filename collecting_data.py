from tkinter import *
import random

class Data:
	def __init__(self):
		self.data = []

	def input(self, name, age, mobile_q):
		new_data = {"name": name, "age": age, "mobile_q": mobile_q}
		self.data.append(new_data)
		print(len(self.data))

	def view(self):
		return self.data

userData = Data()

class GUI1:
	def __init__(self, parent):
		self.parent = parent
		f1 = Frame(parent)

		#Create User Database
		self.userData = userData

		#Header
		self.collecting_data_label = Label(f1, text="Collect Data")
		self.collecting_data_label.grid(row=0, column=0)

		Button(f1, text="Show Data", command=self.view_data).grid(row=0, column=1)

		#First Name
		self.first_name_label = Label(f1, text="First Name: ")
		self.first_name_label.grid(row=1, column=0)

		self.first_name_entry = Entry(f1)
		self.first_name_entry.grid(row=1, column=1)

		#Age 
		self.age_label = Label(f1, text="Age: ")
		self.age_label.grid(row=2, column=0)

		self.age_entry = Entry(f1)
		self.age_entry.grid(row=2, column=1)

		#Mobile Phone Question
		self.mobile_phone_label_1 = Label(f1, text="Do you have a")
		self.mobile_phone_label_1.grid(row=3, column=0)
		self.mobile_phone_label_2 = Label(f1, text="mobile phone?: ")
		self.mobile_phone_label_2.grid(row=4, column=0)

		self.var = StringVar()
		self.yes_rb = Radiobutton(f1, text="Yes", variable=self.var, value="Yes").grid(row=3, column=1)
		self.no_rb = Radiobutton(f1, text="No", variable=self.var, value="No").grid(row=4, column=1)

		#Enter Data
		Button(f1, text="Enter Data", command=self.enter_data).grid(row=5, column=1)

		f1.pack()

	#Input Data
	def enter_data(self):
		self.userData.input(self.first_name_entry.get(), self.age_entry.get(), self.var.get())
		print(self.userData.view())

	def view_data(self):
		self.new_window = Toplevel(self.parent)
		self.app = GUI2(self.new_window)

class GUI2:
	def __init__(self, parent):
		f1 = Frame(parent)

		self.index = 0

		self.UD = userData.view()

		#Labels
		self.collecting_data_label = Label(f1, text="Display Data")
		self.collecting_data_label.grid(row=0, column=0)

		self.collecting_data_label = Label(f1, text="Name: ")
		self.collecting_data_label.grid(row=1, column=0)

		self.collecting_data_label = Label(f1, text="Age: ")
		self.collecting_data_label.grid(row=2, column=0)

		self.collecting_data_label = Label(f1, text="Mobile Phone: ")
		self.collecting_data_label.grid(row=3, column=0)

		#Result
		self.name_result = Label(f1, text="")
		self.name_result.grid(row=1, column=1)

		self.age_result = Label(f1, text="")
		self.age_result.grid(row=2, column=1)

		self.mobile_phone_result = Label(f1, text="")
		self.mobile_phone_result.grid(row=3, column=1)

		#Cofigure
		self.name_result.configure(text=self.UD[0]["name"])
		self.age_result.configure(text=self.UD[0]["age"])
		self.mobile_phone_result.configure(text=self.UD[0]["mobile_q"])

		#Button
		Button(f1, text="Previous", command=self.previous).grid(row=4, column=0)
		Button(f1, text="Next", command=self.next).grid(row=4, column=1)

		f1.pack()

	def next(self):
		self.index +=1
		self.name_result.configure(text=self.UD[self.index]["name"])
		self.age_result.configure(text=self.UD[self.index]["age"])
		self.mobile_phone_result.configure(text=self.UD[self.index]["mobile_q"])

	def previous(self):
		self.index -=1
		self.name_result.configure(text=self.UD[self.index]["name"])
		self.age_result.configure(text=self.UD[self.index]["age"])
		self.mobile_phone_result.configure(text=self.UD[self.index]["mobile_q"])

	
if __name__ == "__main__":
	root = Tk()
	buttons = GUI1(root)
	root.mainloop()