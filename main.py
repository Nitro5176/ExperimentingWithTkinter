import tkinter as tk

# trying to make a calculator as a project to play with tkinter

# the main window
mainWindow = tk.Tk()

# containers
frame = tk.Frame()
frame2 = tk.Frame()
frame3 = tk.Frame()
frame4 = tk.Frame()
# label
label = tk.Label(master=frame,
                 text="frame1",
                 foreground="black",
                 background="white")

label2 = tk.Label(master=frame2,
                  text="frame2",
                  foreground="black",
                  background="white")

label3 = tk.Label(master=frame3,
                  text="frame3",
                  foreground="black",
                  background="white")

label4 = tk.Label(master=frame4,
                  text="frame4",
                  foreground="black",
                  background="white")

# button
firstButton = tk.Button(text="Click me!",
                        foreground="black",
                        background="grey")

# user enter 1 line of text
textfield = tk.Entry()
# user enters multiple lines of text
longTextField = tk.Text()

# the size of the window will fit the text using pack
label.pack()
label2.pack()
label3.pack()
label4.pack()

frame.pack()
frame2.pack()
frame3.pack()
frame4.pack()

firstButton.pack()
textfield.pack()
longTextField.pack()

mainWindow.mainloop()
#second window
secondWindow = tk.Tk()


frame = tk.Frame(master=secondWindow, width=150, height=150)

frame.pack()

#positioning where the labels will be in the 150x150 grid
label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")

#position is top left
label1.place(x=0, y=0)


label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")

label2.place(x=75, y=75)


secondWindow.mainloop()

thirdWindow = tk.Tk()

#goes to each row and adds the columns
for row in range(3):
    for column in range(3):
        frame = tk.Frame(
            master=thirdWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
        #padx and pady makes space in the frames
        frame.grid(row=row, column=column, padx=5, pady=5)
        label = tk.Button(master=frame, text=f"Row {row}\nColumn {column}")
        label.pack(padx=10, pady=10)

thirdWindow.mainloop()

#showing where n, e ,s ,w areas for the labels
fourthWindow = tk.Tk()
fourthWindow.columnconfigure(0, minsize=250)
fourthWindow.rowconfigure([0, 1], minsize=100)
#without any directions, it would default to middle
label1 = tk.Label(text="A")
label1.grid(row=0, column=0)

label2 = tk.Label(text="B")
label2.grid(row=1, column=0)

fourthWindow.mainloop()

#when you add a direction for the labels

fifthWindow = tk.Tk()
fifthWindow.columnconfigure(0, minsize=250)
fifthWindow.rowconfigure([0, 1], minsize=100)

#now adding directions in the labels
label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="n")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="n")

fifthWindow.mainloop()

#showing the dimensions of the labels in the grid with directions
window = tk.Tk()

window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

#shows how much of the space its taken with the directions
label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")

window.mainloop()

