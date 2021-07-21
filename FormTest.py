import tkinter as tk

listOfEntries = ["First Name:", "Last Name:", "Address Line 1:",
                 "Address Line 2:", "City:", "State/Province:",
                 "Postal Code:", "Country:"]

mainWindow = tk.Tk()
mainWindow.title("Address Entry Form")

for i in range(8):
    for j in range(2):
        frame = tk.Frame(master=mainWindow)
        if j == 1:
            frame.grid(row=i, column=j)
            textfield = tk.Entry(master=frame)
            textfield.pack()
        else:
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=listOfEntries[i])
            label.pack()

frame = tk.Frame(master=mainWindow, relief=tk.RAISED)
frame.grid(row=8, column=0, sticky="e")
frame.grid(row=8, column=1, sticky="e")

cleanButton = tk.Button(master=frame, text="Clean")
submitButton = tk.Button(master=frame, text="Submit")


cleanButton.pack(side=tk.RIGHT)
submitButton.pack(side=tk.TOP)


mainWindow.mainloop()
