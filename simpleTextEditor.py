from tkinter import *
import tkinter.messagebox

root = Tk()
charList = []
letterList = []
digitList = []
chars = 0
letters = 0
digits = 0

def countChars(*args):
    global charsList, letterList, digitList, chars, letters, digits, ch, lt, dg
    textInput = textBox.get("1.0","end-1c")
    # for characters
    for i in textInput:
        charList.append(i)
    chars = len(charList)
    ch.set("Characters: " + str(chars))
    
    # for letters
    for i in charList:
        if i.isalpha():
            letterList.append(i)
    letters = len(letterList)
    lt.set("Letters: " + str(letters))
    
    # for digits
    for i in charList:
        if i.isdigit():
            digitList.append(i)
    digits = len(digitList)
    dg.set("Digits: " + str(digits))
    
    charList.clear()
    letterList.clear()
    digitList.clear()


ch = StringVar()
lt = StringVar()
dg = StringVar()


# creating and positioning widgets

textBox = Text(root, height=10, width=45)
textBox.grid(row=0, column=0, columnspan=3)
textBox.bind("<KeyRelease>", countChars)

entryChars = Entry(root, width=20, textvariable=ch)
entryChars.grid(row=1, column=0)
entryChars.insert(10, "Znaków: 0")
entryChars.config(state='readonly')

entryLetters = Entry(root, width=20, textvariable=lt)
entryLetters.grid(row=1, column=1)
entryLetters.insert(10, "Liter: 0")
entryLetters.config(state='readonly')

entryDigits = Entry(root, width=20, textvariable=dg)
entryDigits.grid(row=1, column=2)
entryDigits.insert(10, "Cyfr: 0")
entryDigits.config(state='readonly')



root.mainloop()
