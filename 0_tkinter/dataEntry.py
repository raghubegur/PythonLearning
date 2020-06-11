from tkinter import *

root = Tk()
e = Entry(root, width=50, borderwidth=5, bg='white')
e.pack()
e.insert(0,'Enter Member Alias Name')

def myClick():
    mbrName = e.get()
    myLabel = Label(root, text=mbrName)
    myLabel.pack()

myButton = Button(root, text='Member Alias Name', command=myClick, fg='blue', bg='white')
myButton.pack()

root.mainloop()

