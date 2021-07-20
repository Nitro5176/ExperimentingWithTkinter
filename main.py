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

label1.place(x=0, y=0)


label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")

label2.place(x=75, y=75)


secondWindow.mainloop()
