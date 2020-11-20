from tkinter import *
import tkinter.messagebox

#window
tkWindow = Tk()
tkWindow.geometry('500x250')
tkWindow.title('Exception Handling!')


#label and text entry box
lbl_amount = Label(tkWindow, text="Please enter amount in your account: ")
lbl_amount.grid(row=0, column=0)
amountEntry = Entry(tkWindow)
amountEntry.grid(row=0, column=1)

def click():
	try:
		amount=int(amountEntry.get())
		if amount<3000:
			raise ValueError(tkinter.messagebox.showinfo("Message","Please deposit more funds!"))
	except ValueError as e:
		print(e)
		amountEntry.delete(0,END)
	else:
		tkinter.messagebox.showinfo("STATUS FEEDBACK","Congratulations, You qualify to Malaysia")
		amountEntry.delete(0,END)
	finally:
		print("Transaction completed! ")
#login button
checkQualifications = Button(tkWindow, text="Check Qualifications", command=click)
checkQualifications.grid(row=4, column=0)


def exit():
	sure=tkinter.messagebox.askyesno(title="Alert",message="Are you sure you want to exit?")
	if sure==True:
		tkWindow.destroy()
	else:
		return None

exitBtn=Button(tkWindow,text="exit", command=exit)
exitBtn.grid(row=4,column=2)
tkWindow.mainloop()
