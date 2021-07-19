import tkinter as tk

#trying to make a calculator as a project to play with tkinter

#the main window
mainWindow = tk.Tk()

#containers
frame = tk.Frame()
frame2 = tk.Frame()
frame3 = tk.Frame()
frame4 = tk.Frame()
#label
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


#button
firstButton = tk.Button(text="Click me!",
                        foreground="black",
                        background="grey")

#borderaffects
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE
}
#user enter 1 line of text
textfield = tk.Entry()
#user enters multiple lines of text
longTextField = tk.Text()


#testing the border_effects
#going through each of the items in the dictionary
for relief_name, relief in border_effects.items():
    #creating a frame and a lavel for each item in the dictionary
    frame = tk.Frame(master=mainWindow, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()


#making boxes:
box1 = tk.Frame(master=mainWindow, height=100, width=100, bg="red")
box2 = tk.Frame(master=mainWindow, height=50, width=50, bg="blue")
box3 = tk.Frame(master=mainWindow, height=25, width=25, bg="yellow")

box1.pack()
box2.pack()
box3.pack()

#making boxes fill the x axis
fillBox1 = tk.Frame(master=mainWindow, height=100, bg="red")
fillBox2 = tk.Frame(master=mainWindow, height=50, bg="blue")
fillBox3 = tk.Frame(master=mainWindow, height=25, bg="yellow")

fillBox1.pack(fill=tk.X)
fillBox2.pack(fill=tk.X)
fillBox3.pack(fill=tk.X)

#making boxes fill the Y axis and move them to the left side (in progress of making it work flawlessly

leftBox1 = tk.Frame(master=mainWindow, height=100, bg="green")
leftBox2 = tk.Frame(master=mainWindow, height=50, bg="purple")
leftBox3 = tk.Frame(master=mainWindow, height=25, bg="grey")

leftBox1.pack(fill=tk.Y, side=tk.LEFT)# expand = true makes it expand and fill responsively
leftBox2.pack(fill=tk.Y, side=tk.LEFT)
leftBox3.pack(fill=tk.Y, side=tk.LEFT)


#the size of the window will fit the text using pack
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