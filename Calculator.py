import tkinter as tk
import math as m



mainWindow = tk.Tk()



frame = tk.Frame(master=mainWindow)
frame.pack()
label = tk.Entry(master=frame)



#Step1 Get a grid of  6x4
#Step2 Get each of the buttons a label with the corresponding buttons
#Step 3 add events for each of the buttons
#Step 4 Add adjustments to the grid/buttons to make it look nice
#Step 5 Testing.
# container.columnconfigure(index, weight)
# container.rowconfigure(index, weight)

# frame.columnconfigure(0, 1)
# frame.rowconfigure(1, 2)

inputText = tk.Button(master=frame, text="")
clearButton = tk.Button(master=frame, text="Clear")
percentageButton = tk.Button(master=frame)
powerOfButton = tk.Button(master=frame)
divisionButton = tk.Button(master=frame)
multiplicationButton = tk.Button(master=frame)
additionButton = tk.Button(master=frame)
subtractionButton = tk.Button(master=frame)
decimalButton = tk.Button(master=frame)

num0 = tk.Button(master=frame, text="0")
num1 = tk.Button(master=frame, text="1")
num2 = tk.Button(master=frame, text="2")
num3 = tk.Button(master=frame, text="3")
num4 = tk.Button(master=frame, text="4")
num5 = tk.Button(master=frame, text="5")
num6 = tk.Button(master=frame, text="6")
num7 = tk.Button(master=frame, text="7")
num8 = tk.Button(master=frame, text="8")
num9 = tk.Button(master=frame, text="9")

numbersOnPad = 0



# for i in range(3):
#     for j in range(3):
#         numbersOnPad += 1
#         numPadFrame = tk.Frame(master=frame, relief=tk.RAISED, borderwidth=1)
#         numPadFrame.grid(row=i, column=j)
#         numButtons = tk.Button(master=numPadFrame, text=numbersOnPad)
#         numButtons.pack(fill=tk.BOTH, expand=1)

# arithmeticButtons = tk.Frame(master=frame)


# label.grid()
# clearButton.grid()
# numPadFrame.grid()
# arithmeticButtons.grid()




# print(label.get())



mainWindow.mainloop()