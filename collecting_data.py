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

class GUI:
    def __init__(self, parent):
        f1 = Frame(parent)

        #Create User Database
        self.userData = Data()

        #Header
        self.collecting_data_label = Label(f1, text="Collect Data")
        self.collecting_data_label.grid(row=0, column=0)

        Button(f1, text="Show Data").grid(row=0, column=1)

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

        self.var = IntVar()
        self.yes_rb = Radiobutton(f1, text="Yes", variable=self.var, value=1).grid(row=3, column=1)
        self.no_rb = Radiobutton(f1, text="No", variable=self.var, value=0).grid(row=4, column=1)

        #Enter Data
        Button(f1, text="Enter Data", command=self.enter_data).grid(row=5, column=1)

        f1.pack()

    #Input Data
    def enter_data(self):
    	self.userData.input(self.first_name_entry.get(), self.age_entry.get(), self.var.get())
    	print(self.userData.view())
    
if __name__ == "__main__":
    root = Tk()
    buttons = GUI(root)
    root.mainloop()