#!/usr/bin/env python3
from tkinter import *

def addition():
    # x=int(input("How many numbers would you like to use\n:"))
    # numAdd = []
    # sum = 0
    # i=1
    # while i <= x :
    #     num = int(input("Enter a number: \n"))
    #     numAdd.append(num)
    #     sum+=num
    #     num = 0
    #     i+=1
    # print(sum)
    # print(numAdd)
    result_label.config(text="Addition button pressed")
def subtraction(x):
    # numSub = []
    # sum = 0
    # i=1
    # while i <= x :
    #     num = int(input("Enter a number: \n"))
    #     numSub.append(num)
    #     sum-=num
    #     num = 0
    #     i+=1
    # print(sum)
    # print(numSub)
    result_label.config(text="Subtraction button pressed")

def multiplication(x):
    # numMult = []
    # sum = 0
    # i=1
    # while i <= x :
    #     num = int(input("Enter a number: \n"))
    #     numMult.append(num)
    #     sum*=num
    #     num = 0
    #     i+=1
    # print(sum)
    # print(numMult)
    result_label.config(text="Multiplication button pressed")

def division(x):
    # numDiv = []
    # sum = 0
    # i=1
    # while i <= x :
    #     num = int(input("Enter a number: \n"))
    #     numDiv.append(num)
    #     sum/=num
    #     num = 0
    #     i+=1
    # print(sum)
    # print(numDiv)
    result_label.config(text="Division button pressed")


# print("Hello and welcome to QuantumQuizzle")
# choice = input("Choose a topic: +, - , /, *\n")
# if choice == '+':
#     much=input("How many numbers would you like to use\n:")
#     addition(int(much))
# elif choice == '-':
#     much=input("How many numbers would you like to use\n:")
#     subtraction(int(much))
# elif choice == '*':
#     much=input("How many numbers would you like to use\n:")
#     multiplication(int(much))
# elif choice == '/':
#     much=input("How many numbers would you like to use\n:")
#     division(int(much))
# else:
#     print("OOf that is not a option.")

window = Tk ()
window.geometry ("800x500")

ProgName = Label(window,font=('Times new roman', 20, 'bold'), text="QuantumQuizzle (^_^)", fg = "Purple")
ProgName.place(relx=.4,rely=.01)

chooseType = Label(window,font=('Times new roman',20, 'bold'), text="Choose between Addition, Subtraction, Multiplication, and Division", fg="Green")
chooseType.place(relx=.02,rely=.2)

optionAdd= Button(window ,font = ('Times new roman', 15, 'italic'), text="Addition", command=  addition)
optionAdd.place(relx=.01,rely=.4)
optionSub= Button(window ,font = ('Times new roman', 15, 'italic'), text="Subtraction", command=  subtraction)
optionSub.place(relx=.01,rely=.5)
optionMult= Button(window ,font = ('Times new roman', 15, 'italic'), text="Multiplication", command=  multiplication)
optionMult.place(relx=.01,rely=.6)
optionDiv= Button(window ,font = ('Times new roman', 15, 'italic'), text="Division", command=  division)
optionDiv.place(relx=.01,rely=.7)

result_label = Label(window, font=('Times new roman', 15, 'bold'), text="")
result_label.place(relx=.2, rely=.8)

enter = Entry(window)
enter.place(relx=.3,rely = .5)
window.mainloop()