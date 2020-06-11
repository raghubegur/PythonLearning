from tkinter import *
from PIL import Image, ImageTk  # for hanlding jpeg/png/etc type images

root = Tk()
root.title("Images Example")
root.iconbitmap('C:/Raghu/Python_WS/0_tkinter/Dog.ico')

img_1 = ImageTk.PhotoImage(Image.open('C:/Raghu/Personal/Home_Pictures/1.jpg'))
img_2 = ImageTk.PhotoImage(Image.open('C:/Raghu/Personal/Home_Pictures/2.jpg'))
img_3 = ImageTk.PhotoImage(Image.open('C:/Raghu/Personal/Home_Pictures/3.jpg'))

label_1 = Label(image=door_img)
label_1.pack()

button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()


root.mainloop()

