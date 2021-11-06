#Factoring
#Given a graph find the equation
#Quadratic formula
#Line of best fit
#Systems of Equations
#Solving single variable equations
#Inequalities
#Completing the Squre
#Sequences
#Exponetials
import tkinter as tk 
from tkinter import *
import matplotlib.pyplot as plt
from tkinter import ttk


def factor():
    print("hi")

def quad():
    print("hi")

def square():
    print("hi")

def solving():
    print("hi")

def system():
    print("hi")

def inequal():
    print("hi")

def graph():
    print("hi")

def best():
    print("hi")

def expon():
    print("hi")

def seq():
    print("hi")

def about():
    sectionTitleText = Text(window, height = 15, width = 61, background='#dadde3', borderwidth = 0, font = ("Helvetica", 15))
    sectionTitleText.place(x = 240, y = 25)
    sectionTitleText.delete(1.0, "end")
    sectionTitleText.insert(1.0, "About AlgeBRO:"+
                                "\n " +
                                "\nOur programs goals are to tutor students in the subject of Algebra. We offer a variety" + 
                                "\nof questions surrounding key ideas like solving equations, graphs, and multiple" + 
                                "\nfunctions and allow students to get tips if they got an answer wrong. We also have" + 
                                "\nour program translated into multiple languages so students from different countries" +  
                                "\ncan also get help in the universal language of math!" +
                                "\n " +
                                "\nHow To Use AlgeBRO:" +
                                "\n " +
                                "\n1. Select the skill you want to practice on the side bar menu" +
                                "\n2. Attempt to solve the problems given." +
                                "\n3. If you are unable to solve it or just need a nudge in the right direction, just click the hint button" +
                                "\n4. Enjoy learning and improving up on your math skills!")

#Our programs goals are to tutor students in the subject of Algebra. We offer a variety of questions surrounding key ideas like solving equations, graphs, and multiple functions. We offer multiple questions in each category and allow students to get tipes if they got an answer wrong. We also have our program translated into multiple languages so students from different countries can also get help in the universal language of math!

def english():
    print("hi")

def spanish():
    print("hi")

def chinese():
    print("hi")

def viet():
    print("hi")

def arabic():
    print("hi")

def russian():
    print("hi")




window = Tk()
window.geometry("800x500")
window.resizable(False, False)
window.configure(background = '#dadde3')
window.title('AlgeBRO')


factorBtn = Button(window, text = "Factoring", command = factor)
factorBtn.place(x = 25, y = 86)

quadBtn = Button(window, text = "Quadratic Formula", command = quad)
quadBtn.place(x = 25, y = 122)

squareBtn = Button(window, text = "Completing the Square", command = square)
squareBtn.place(x = 25, y = 159)

solvingBtn = Button(window, text = "Solving Single Variable Equations", command = solving)
solvingBtn.place(x = 25, y = 195)

systemBtn = Button(window, text = "System of Equations", command = system)
systemBtn.place(x = 25, y = 231)

inequalBtn = Button(window, text = "Inequalities", command = inequal)
inequalBtn.place(x = 25, y = 268)

graphBtn = Button(window, text = "Find the Equation of a Graph", command = graph)
graphBtn.place(x = 25, y = 304)

bestBtn = Button(window, text = "Line of Best Fit", command = best)
bestBtn.place(x = 25, y = 340)

exponBtn = Button(window, text = "Exponents", command = expon)
exponBtn.place(x = 25, y = 377)

seqBtn = Button(window, text = "Sequences", command = seq)
seqBtn.place(x = 25, y = 413)

aboutBtn = Button(window, text = "About", command = about)
aboutBtn.place(x = 25, y = 450)


englishBtn = Button(window, text = "English", command = english)
englishBtn.place(x = 503, y = 475)

spanishBtn = Button(window, text = "Español", command = spanish)
spanishBtn.place(x = 553, y = 475)

chineseBtn = Button(window, text = "中文", command = chinese)
chineseBtn.place(x = 605, y = 475)

vietBtn = Button(window, text = "Việt Nam", command = viet)
vietBtn.place(x = 640, y = 475)

arabicBtn = Button(window, text = "العربية", command = arabic)
arabicBtn.place(x = 700, y = 475)

russianBtn = Button(window, text = "русский", command = russian)
russianBtn.place(x = 745, y = 475)


separator = ttk.Separator(window, orient = 'vertical')
separator.place(relx = 0.29, rely = 0, relwidth = 0.001, relheight = 1)


window.mainloop()
