import tkinter as tk
import math as m



mainWindow = tk.Tk()



frame = tk.Frame(master=mainWindow)
frame.pack()
label = tk.Entry(master=frame)


clearButton = tk.Button(master=frame, text="Clear")
numbersOnPad = 0

for i in range(3):
    for j in range(3):
        numbersOnPad += 1
        numPadFrame = tk.Frame(master=frame, relief=tk.RAISED, borderwidth=1)
        numPadFrame.grid(row=i, column=j)
        numButtons = tk.Button(master=numPadFrame, text=numbersOnPad)
        numButtons.pack(fill=tk.BOTH, expand=1)

arithmeticButtons = tk.Frame(master=frame)


label.grid()
clearButton.grid()
numPadFrame.grid()
arithmeticButtons.grid()




print(label.get())



mainWindow.mainloop()