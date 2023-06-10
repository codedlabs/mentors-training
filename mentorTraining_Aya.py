from tkinter import *
from tkinter import messagebox
import re
from datetime import date

# Validating Email using regular expressions
def checkEmail(email):
    pat = "^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pat, email)

# Calculating age from civil ID
def dateOfBirth(cid):
    YY = cid[0:2]
    MM = cid[2:4]
    DD = cid[4:6]
    if int(YY) > 23:
        YY = "19" + YY
    else:
        YY = "20" + YY

    d = date(int(YY), int(MM), int(DD))
    today = date.today()
    return today.year - d.year -((today.month, today.day) < (d.month, d.day))

# Processing the form's data
def click():
    gender = g.get()
    emailEntry = email.get()
    cid = civilID.get()
    age = dateOfBirth(cid[1:7])
    emailFlag = True
    ageFlag = True

    if not checkEmail(emailEntry):
        messagebox.showerror("Error", "Invalid email address")
        emailFlag = False
    
    if age < 13:
        messagebox.showerror("Error", "Sorry kid, maybe next time!")
        ageFlag = False
    elif age > 18:
        messagebox.showerror("Error", "It's for kids only!")
        ageFlag = False

    if gender == 1 and ageFlag and emailFlag:
        endPrompt = Label(root, text="Thank you 💕")
        endPrompt.pack()
    elif gender == 2 and ageFlag and emailFlag:
        endPrompt = Label(root, text="Thank you 💙")
        endPrompt.pack()

# Reseting the form
def delete():
    name.delete(0, END)
    email.delete(0, END)
    civilID.delete(0, END)

# Creating the form

root = Tk(className="Kuwait Codes Regestration Form")

greetings = Label(root, text="Registration for Kuwait Codes Summer 2023!", bg="blue", fg="white")
greetings.pack()

# Asking for Name
namePromt = Label(root, text="Enter your name: ")
namePromt.pack()
name = Entry(root, width=50, borderwidth=5)
name.pack()

# Asking for Email
emailPromt = Label(root, text="Enter your email: ")
emailPromt.pack()
email = Entry(root, width=50, borderwidth=5)
email.pack()

# Asking for Civil ID
civilIDPromt = Label(root, text="Enter your civil ID: ")
civilIDPromt.pack()
civilID = Entry(root, width=50, borderwidth=5)
civilID.pack()

# Asking for Gender
genderPromt = Label(root, text="Choose your gender: " )
genderPromt.pack()
g = IntVar()
femaleButton = Radiobutton(root, text="Female", variable=g, value=1)
femaleButton.pack()
maleButton = Radiobutton(root, text="Male", variable=g, value=2)
maleButton.pack()

# Submit Button
submitButton = Button(root, text="Submit Form", command=click)
submitButton.pack()

# Form reset button
deleteButton = Button(root, text="Reset Form", command=delete)
deleteButton.pack()

root.mainloop()