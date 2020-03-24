from tkinter import *
import math

def leftClickButton(event):
    BMI = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(BMI)
    labelResult.configure(text=BMI)
    if BMI >= 30:
        showResultBMI.configure(text="Obesity")
    elif BMI >= 25 and BMI <= 29.9:
        showResultBMI.configure(text="Overweight")
    elif BMI >= 23 and BMI <= 24.9:
        showResultBMI.configure(text="Fat")
    elif BMI >= 18 and BMI <= 22.9:
        showResultBMI.configure(text="Normal weight")
    elif BMI <= 18.5:
        showResultBMI.configure(text="Underweight")

main= Tk()
labelHeight = Label(main,text="Height (cm)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(main,text="Weight (kg)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row=1,column=1)

calculatorButton = Button(main,text="Calculator")
calculatorButton.bind('<Button-1>',leftClickButton)
calculatorButton.grid(row=2,column=0)

labelResult = Label(main,text="Result")
labelResult.grid(row=2,column=1)

labelResultBMI = Label(main,text="Result BMI")
labelResultBMI.grid(row=3,column=0)

showResultBMI = Label(main,text="Show BMI")
showResultBMI.grid(row=3,column=1)

main.mainloop()