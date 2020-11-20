from tkinter import *
from tkinter import messagebox

#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Tkinter Login Form')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name")
usernameLabel.grid(row=0, column=0)
usernameEntry = Entry(tkWindow)
usernameEntry.grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password")
passwordLabel.grid(row=1, column=0)
passwordEntry = Entry(tkWindow, show='*')
passwordEntry.grid(row=1, column=1)

def logIn():
	users={"Lelethu":"Ndidi", "Tamsyn":"Steed", "Zoe":"Engel", "Victor":"Nkuna"}
	usernames=usernameEntry.get()
	passwords=passwordEntry.get()
	if (usernames, passwords) in users.items():
		messagebox.showinfo("Login status","Successful")
		tkWindow.withdraw()
		import malaysia
		malaysia.click()
	else:
		messagebox.showinfo("Login status","Incorrect password or username")
		usernameEntry.delete(END,0)
		passwordEntry.delete(END,0)

#login button
loginButton = Button(tkWindow, text="Login", command=logIn)
loginButton.grid(row=4, column=0)

tkWindow.mainloop()
