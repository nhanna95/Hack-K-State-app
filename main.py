from tkinter import *
from tkinter import ttk
import random
import math

def factor():
    def hint():
        hintText = Text(window, height = 1, background = '#dadde3', borderwidth = 0, font= ("Helvetica", 15))
        hintText.place(x = 250, y = 150)
        hintText.delete(1.0, "end")
        hintText.insert(1.0, "Hint: Think of what two numbers multiple to the constant")
        
    def search():
        userInput = entry.get()
        if (userInput == answer):
            print("yay")
            blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
            blankText.place(x=235,y=0)
            congratsText = Text(window, height = 1, background = '#dadde3', borderwidth=0, font = ("Helvetica", 20))
            congratsText.place(x = 250, y = 25)
            congratsText.delete(1.0, "end")
            congratsText.insert(1.0, "CONGRATS! You Got the Right Answer!")
            secondText = Text(window, height = 1, background='#dadde3', borderwidth=0, font = ("Helvetica", 15))
            secondText.place(x = 250, y = 70)
            secondText.delete(1.0, "end")
            secondText.insert(1.0, "Click the button below to go to the next question!")
            continueBtn = Button(window, text="Next Question", command = factor)
            continueBtn.place(x = 450, y = 200)
        else:
            hint()

    def showSolution():
        solutionText = Text(window, height = 1, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 15))
        solutionText.place(x = 250, y = 190)
        solutionText.delete(1.0, "end")
        solutionText.insert(1.0, "The solution is " + answer)

    

    blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
    blankText.place(x=235,y=0)
    sectionTitleText = Text(window, height = 1, width = 8, background='#dadde3', borderwidth = 0, font = ("Helvetica", 20))
    sectionTitleText.place(x=250,y=20)
    entry = Entry(window)
    entry.place(x = 550, y = 445)
    submitBtn = Button(window, text="Submit", command = search)
    submitBtn.place(x = 700, y = 440)
    sectionTitleText.delete(1.0, "end")
    sectionTitleText.insert(1.0, "Factoring")
    problemText = Text(window, height = 1,  background='#dadde3', borderwidth = 0, font = ("Helvetica", 12))
    problemText.place(x = 250, y = 60)
    problemText.delete(1.0, "end")
    problemText.insert(1.0, "Give the Factored Form of this Equation: ")
    explainText = Text(window, height = 1, background = '#dadde3', borderwidth = 0, font = ("Helvetica", 10))
    explainText.place(x = 250, y = 90)
    explainText.delete(1.0, "end")
    explainText.insert(1.0, "Enter your answer in form (ax+b)(cx+d) or use '-' if b or d is negative")
    hintBtn = Button(window, text = "Give me a hint", command = hint)
    hintBtn.place(x = 250, y = 400)
    skipBtn = Button(window, text = "Skip Question", command = factor)
    skipBtn.place(x = 700, y = 470)
    answer = "("

    firstNum = random.randint(1, 10)
    secondNum = random.randint(1, 10)
    if (random.randint(0,1) == 1):
        firstXCoefficient = random.randint(2, 5)
        answer = answer + str(firstXCoefficient) + "x"
    else:
        firstXCoefficient = 1
        answer = answer + "x"

    if (random.randint(0, 1) == 1):
        firstOperator = "+"
        answer = answer + "+" + str(firstNum) + ")("
    else:
        firstOperator = "-"
        answer = answer + "-" + str(firstNum) + ")("
        firstNum = firstNum * -1

    if (random.randint(0,1) == 1):
        secondXCoefficient = random.randint(2, 5)
        answer = answer + str(secondXCoefficient) + "x"
    else:
        secondXCoefficient = 1
        answer = answer + "x"
    
    if (random.randint(0,1) == 1):
        secondOperator = "+"
        answer = answer + "+" + str(secondNum) + ")"
    else:
        secondOperator = "-"
        answer = answer + "-" + str(secondNum) + ")"
        secondNum = secondNum * -1

    print(answer)
    firstTerm = firstXCoefficient * secondXCoefficient
    middleTerm = (firstXCoefficient * secondNum) + (secondXCoefficient * firstNum)
    lastTerm = firstNum * secondNum
    if (firstTerm != 1):
        question = str(firstTerm) + "x^2 "
    else: 
        question = "x^2 "
    if (middleTerm < 0):
        question = question + "- " + str(abs(middleTerm)) + "x "
    elif (middleTerm > 0):
        question = question + "+ " + str(middleTerm) + "x "
    if (lastTerm < 0):
        question = question + " - " + str(abs(lastTerm))
    else:
        question = question + " + " + str(lastTerm)

    print(question)
    
    question = question + " = 0"
    problemText.insert(2.0, question)

    solutionBtn = Button(window, text = "Give me the solution", command = showSolution)
    solutionBtn.place(x = 250, y = 440)


def quad():
    screenNum = 2
    def search():
        userInput = entry.get()
        if (userInput == (str(answerPlus) + ", " + str(answerMinus))):
            print("yay")
            blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
            blankText.place(x=235,y=0)
            congratsText = Text(window, height = 1, background = '#dadde3', borderwidth=0, font = ("Helvetica", 20))
            congratsText.place(x = 250, y = 25)
            congratsText.delete(1.0, "end")
            congratsText.insert(1.0, "CONGRATS! You Got the Right Answer!")
            secondText = Text(window, height = 1, background='#dadde3', borderwidth=0, font = ("Helvetica", 15))
            secondText.place(x = 250, y = 70)
            secondText.delete(1.0, "end")
            secondText.insert(1.0, "Click the button below to go to the next question!")
            continueBtn = Button(window, text="Next Question", command = quad)
            continueBtn.place(x = 450, y = 200)
        else:
            hint()

    def hint():
        if (screenNum == 2):
            hintText = Text(window, height = 1, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 15))
            hintText.place(x = 250, y = 150)
            hintText.delete(1.0, "end")
            hintText.insert(1.0, "Hint: Use the quadratic formula: (-b ?? sqrt(b^2 - 4ac))/2a")

    def showSolution():
        if (screenNum == 2):
            solutionText = Text(window, height = 1, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 15))
            solutionText.place(x = 250, y = 190)
            solutionText.delete(1.0, "end")
            solutionText.insert(1.0, "The solution is " + str(answerPlus) + ", " + str(answerMinus))

    blankText = Text(window, height = 400, background = '#dadde3', borderwidth = 0, font = ("Helvetica", 20))
    blankText.place(x = 235, y = 0)

    sectionTitleText = Text(window, height = 1, width = 8, background='#dadde3', borderwidth = 0, font = ("Helvetica", 20))
    sectionTitleText.place(x = 250,y = 20)

    entry = Entry(window)
    entry.place(x = 550, y = 445)
    submitBtn = Button(window, text = "Submit", command = search)
    submitBtn.place(x = 700, y = 440)
    skipBtn = Button(window, text = "Skip Question", command = quad)
    skipBtn.place(x = 700, y = 470)

    sectionTitleText.delete(1.0, "end")
    sectionTitleText.insert(1.0, "Quadratic Formula")
    problemText = Text(window, height = 4, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 12))
    problemText.place(x = 250, y = 60)
    problemText.delete(1.0, "end")
    problemText.insert(1.0, "Find the solutions to the equation, rounding your answer to the nearest three " + 
                            "\ndecimal points. If your answer is an integer, type .0 after the integer. If your "+
                            "\nanswer is a terminating decimal, enter your answer until the decimal terminates." +
                            "\nEnter the higher solution first. Equation: ")

    hintBtn = Button(window, text = "Give me a hint", command = hint)
    hintBtn.place(x = 250, y = 400)

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    while((b*b - 4*a*c) < 0):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
    
    if (a == 1 and b == 1):
        question = "x^2 + x + " + str(c)
    elif(a == 1 and b != 1):
        question = "x^2 + " + str(b) + "x + " + str(c)
    elif(a != 1 and b == 1):
        question = str(a) + "x^2 + x + " + str(c)
    else:
        question = str(a) + "x^2 + " + str(b) + "x + " + str(c)

    problemText.insert(6.0, question)

    answerPlus = round(((-b + math.sqrt(b*b - 4*a*c))/(2*a)), 3)
    answerMinus = round(((-b - math.sqrt(b*b - 4*a*c))/(2*a)), 3)
    print(str(answerPlus) + ", " + str(answerMinus))

    solutionBtn = Button(window, text = "Give me the solution", command = showSolution)
    solutionBtn.place(x = 250, y = 440)

def square():
    screenNum = 3
    def search():
        userInput = entry.get()
        if (userInput == answer):
            print("yay")
            blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
            blankText.place(x=235,y=0)
            congratsText = Text(window, height = 1, background = '#dadde3', borderwidth=0, font = ("Helvetica", 20))
            congratsText.place(x = 250, y = 25)
            congratsText.delete(1.0, "end")
            congratsText.insert(1.0, "CONGRATS! You Got the Right Answer!")
            secondText = Text(window, height = 1, background='#dadde3', borderwidth=0, font = ("Helvetica", 15))
            secondText.place(x = 250, y = 70)
            secondText.delete(1.0, "end")
            secondText.insert(1.0, "Click the button below to go to the next question!")
            continueBtn = Button(window, text="Next Question", command = quad)
            continueBtn.place(x = 450, y = 200)
        else:
            hint()

    def hint():
        if (screenNum == 3):
            hintText = Text(window, height = 2, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 15))
            hintText.place(x = 250, y = 150)
            hintText.delete(1.0, "end")
            hintText.insert(2.0, "Hint: add (b/2)^2 to both sides (right side is 0), factor \nthe left side, subtract the "+
                                 "right side from both sides.")

    def showSolution():
        if (screenNum == 3):
            solutionText = Text(window, height = 1, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 15))
            solutionText.place(x = 250, y = 200)
            solutionText.delete(1.0, "end")
            solutionText.insert(1.0, "The solution is " + answer)

    blankText = Text(window, height = 400, background = '#dadde3', borderwidth = 0, font = ("Helvetica", 20))
    blankText.place(x = 235, y = 0)

    sectionTitleText = Text(window, height = 1, background='#dadde3', borderwidth = 0, font = ("Helvetica", 20))
    sectionTitleText.place(x = 250,y = 20)

    entry = Entry(window)
    entry.place(x = 550, y = 445)
    submitBtn = Button(window, text = "Submit", command = search)
    submitBtn.place(x = 700, y = 440)
    skipBtn = Button(window, text = "Skip Question", command = quad)
    skipBtn.place(x = 700, y = 470)

    sectionTitleText.delete(1.0, "end")
    sectionTitleText.insert(1.0, "Completing the Square")
    problemText = Text(window, height = 4, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 12))
    problemText.place(x = 250, y = 60)
    problemText.delete(1.0, "end")
    problemText.insert(1.0, "Complete the square of the equation, rounding your answer to the nearest three " + 
                            "\ndecimal points. If your answer has an integer, type .0 after the integer. If your "+
                            "\nanswer is a terminating decimal, enter your answer until the decimal terminates." +
                            "\nEnter the higher solution first. Equation: ")

    hintBtn = Button(window, text = "Give me a hint", command = hint)
    hintBtn.place(x = 250, y = 400)

    a = 1
    b = (random.randint(1, 5))*2
    c = random.randint(1, 10)

    question = "x^2 + " + str(b) + "x + " + str(c)

    answer = "(x+" + str(b/2) + ")^2-" + str(c+((b/2)*(b/2)))
    print(answer)

    problemText.insert(5.0, question)

    solutionBtn = Button(window, text = "Give me the solution", command = showSolution)
    solutionBtn.place(x = 250, y = 440)

def solving():
    def hint():
            hintText = Text(window, height = 1, background = '#dadde3', borderwidth=0, font= ("Helvetica", 15))
            hintText.place(x = 250, y = 150)
            hintText.delete(1.0, "end")
            hintText.insert(1.0, "Hint: Get all x's to one side and then divide")
        
    def search():
        userInput = entry.get()
        print(userInput)
        print(answer)
        if (str(userInput) == str(answer)):
            print("yay")
            blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
            blankText.place(x=235,y=0)
            congratsText = Text(window, height = 1, background = '#dadde3', borderwidth=0, font = ("Helvetica", 20))
            congratsText.place(x = 250, y = 25)
            congratsText.delete(1.0, "end")
            congratsText.insert(1.0, "CONGRATS! You Got the Right Answer!")
            secondText = Text(window, height = 1, background='#dadde3', borderwidth=0, font = ("Helvetica", 15))
            secondText.place(x = 250, y = 70)
            secondText.delete(1.0, "end")
            secondText.insert(1.0, "Click the button below to go to the next question!")
            continueBtn = Button(window, text="Next Question", command = solving)
            continueBtn.place(x = 450, y = 200)
        else:
            hint()

    def showSolution():
        solutionText = Text(window, height = 1, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 15))
        solutionText.place(x = 250, y = 190)
        solutionText.delete(1.0, "end")
        solutionText.insert(1.0, "The solution is " + str(answer))

    blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
    blankText.place(x=235,y=0)
    sectionTitleText = Text(window, height = 1, background='#dadde3', borderwidth = 0, font = ("Helvetica", 20))
    sectionTitleText.place(x=250,y=20)
    entry = Entry(window)
    entry.place(x = 550, y = 445)
    submitBtn = Button(window, text="Submit", command = search)
    submitBtn.place(x = 700, y = 440)
    sectionTitleText.delete(1.0, "end")
    sectionTitleText.insert(1.0, "Solving Single Variable Equations")
    problemText = Text(window, height = 1,  background='#dadde3', borderwidth = 0, font = ("Helvetica", 12))
    problemText.place(x = 250, y = 60)
    problemText.delete(1.0, "end")
    problemText.insert(1.0, "Solve for the value of x in this Equation: ")
    explainText = Text(window, height = 1, background = '#dadde3', borderwidth = 0, font = ("Helvetica", 10))
    explainText.place(x = 250, y = 90)
    explainText.delete(1.0, "end")
    explainText.insert(1.0, "Enter your answer to a maximum of three digits")
    hintBtn = Button(window, text = "Give me a hint", command = hint)
    hintBtn.place(x = 250, y = 400)
    solutionBtn = Button(window, text = "Give me the solution", command = showSolution)
    solutionBtn.place(x = 250, y = 440)
    skipBtn = Button(window, text = "Skip Question", command = solving)
    skipBtn.place(x = 700, y = 470)

    if (random.randint(0,1) == 1):
        a = random.randint(-10, -1)
    else:
        a = random.randint(1, 10)
    if (random.randint(0,1) == 1):
        b = random.randint(-10, -1)
    else:
        b = random.randint(-10, -1)
    if (random.randint(0,1) == 1):
        c = random.randint(-10, -1)
    else:
        c = random.randint(1, 10)
    if (random.randint(0,1) == 1):
        d = random.randint(-10, -1)
    else:
        d = random.randint(1, 10)

    while(a == c or b == d):
        if (random.randint(0,1) == 1):
            a = random.randint(-10, -1)
        else:
            a = random.randint(1, 10)
        if (random.randint(0,1) == 1):
            b = random.randint(-10, -1)
        else:
            b = random.randint(-10, -1)
        if (random.randint(0,1) == 1):
            c = random.randint(-10, -1)
        else:
            c = random.randint(1, 10)
        if (random.randint(0,1) == 1):
            d = random.randint(-10, -1)
        else:
            d = random.randint(1, 10)

    question = str(a) + "x "
    if (b < 0):
        question = question + "- " + str(abs(b)) + " = " + str(c) + "x "
    else:
        question = question + "+ " + str(b) + " = " + str(c) + "x "
    
    if (d < 0):
        question = question + "- " + str(abs(d))
    else:
        question = question + "+ " + str(d)

    print(question)
    answer = (d - b) / (a - c)
    answer = round(answer, 3)
    print(answer)

    problemText.insert(6.0, question)

def system():
    def hint():
            hintText = Text(window, height = 2, background = '#dadde3', borderwidth=0, font= ("Helvetica", 15))
            hintText.place(x = 250, y = 150)
            hintText.delete(1.0, "end")
            hintText.insert(1.0, "Hint: Munipulate the Equations so you are \nable to cancel one of the variables")
        
    def search():
        userInput = entry.get()
        print(userInput)
        print(answer)
        if (str(userInput) == str(answer)):
            print("yay")
            blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
            blankText.place(x=235,y=0)
            congratsText = Text(window, height = 1, background = '#dadde3', borderwidth=0, font = ("Helvetica", 20))
            congratsText.place(x = 250, y = 25)
            congratsText.delete(1.0, "end")
            congratsText.insert(1.0, "CONGRATS! You Got the Right Answer!")
            secondText = Text(window, height = 1, background='#dadde3', borderwidth=0, font = ("Helvetica", 15))
            secondText.place(x = 250, y = 70)
            secondText.delete(1.0, "end")
            secondText.insert(1.0, "Click the button below to go to the next question!")
            continueBtn = Button(window, text="Next Question", command = system)
            continueBtn.place(x = 450, y = 200)
        else:
            hint()

    def showSolution():
        solutionText = Text(window, height = 1, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 15))
        solutionText.place(x = 250, y = 205)
        solutionText.delete(1.0, "end")
        solutionText.insert(1.0, "The solution is " + str(answer))

    blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
    blankText.place(x=235,y=0)
    sectionTitleText = Text(window, height = 1, background='#dadde3', borderwidth = 0, font = ("Helvetica", 20))
    sectionTitleText.place(x=250,y=20)
    entry = Entry(window)
    entry.place(x = 550, y = 445)
    submitBtn = Button(window, text="Submit", command = search)
    submitBtn.place(x = 700, y = 440)
    sectionTitleText.delete(1.0, "end")
    sectionTitleText.insert(1.0, "Solving a System of Equations")
    problemText = Text(window, height = 1,  background='#dadde3', borderwidth = 0, font = ("Helvetica", 12))
    problemText.place(x = 250, y = 60)
    problemText.delete(1.0, "end")
    problemText.insert(1.0, "Solve for the value of x and y in these equations: ")
    explainText = Text(window, height = 1, background = '#dadde3', borderwidth = 0, font = ("Helvetica", 10))
    explainText.place(x = 250, y = 90)
    explainText.delete(1.0, "end")
    explainText.insert(1.0, "Enter your answer in form x,y with rounded to a maximum of 3 digits")
    hintBtn = Button(window, text = "Give me a hint", command = hint)
    hintBtn.place(x = 250, y = 400)
    solutionBtn = Button(window, text = "Give me the solution", command = showSolution)
    solutionBtn.place(x = 250, y = 440)
    skipBtn = Button(window, text = "Skip Question", command = system)
    skipBtn.place(x = 700, y = 470)

    if (random.randint(0,1) == 1):
        a = random.randint(-10, -1)
    else:
        a = random.randint(1, 10)
    if (random.randint(0,1) == 1):
        b = random.randint(-10, -1)
    else:
        b = random.randint(-10, -1)
    if (random.randint(0,1) == 1):
        c = random.randint(-10, -1)
    else:
        c = random.randint(1, 10)
    if (random.randint(0,1) == 1):
        d = random.randint(-10, -1)
    else:
        d = random.randint(1, 10)
    if (random.randint(0,1) == 1):
        e = random.randint(-10, -1)
    else:
        e = random.randint(1, 10)
    if (random.randint(0,1) == 1):
        f = random.randint(-10, -1)
    else:
        f = random.randint(1, 10)

    while(a == d or b == e or c == f):
        if (random.randint(0,1) == 1):
            a = random.randint(-10, -1)
        else:
            a = random.randint(1, 10)
        if (random.randint(0,1) == 1):
            b = random.randint(-10, -1)
        else:
            b = random.randint(-10, -1)
        if (random.randint(0,1) == 1):
            c = random.randint(-10, -1)
        else:
            c = random.randint(1, 10)
        if (random.randint(0,1) == 1):
            d = random.randint(-10, -1)
        else:
            d = random.randint(1, 10)
        if (random.randint(0,1) == 1):
            e = random.randint(-10, -1)
        else:
            e = random.randint(1, 10)
        if (random.randint(0,1) == 1):
            f = random.randint(-10, -1)
        else:
            f = random.randint(1, 10)

    equationOne = str(a) + "x "
    if (b < 0):
        equationOne = equationOne + "- " + str(abs(b)) + "y = " + str(c)
    else:
        equationOne = equationOne + "+ " + str(b) + "y = " + str(c)

    equationTwo = str(d) + "x " 
    if (e < 0):
        equationTwo = equationTwo + "- " + str(abs(e)) + "y = " + str(f)
    else:
        equationTwo = equationTwo + "+ " + str(e) + "y = " + str(f)

    problemText.insert(6.0, equationOne + ", " + equationTwo)

    print(equationOne)
    print(equationTwo)


    x = (e * c - b * f) / (a * e - b * d)
    y = (d * c - a * f) / (b * d - a * e)
    x = round(x, 3)
    y = round(y, 3)
    answer = str(x) + ", " + str(y)
    print(answer)

def expon():
    screenNum = 9
    def search():
        userInput = entry.get()
        if (userInput == answer):
            print("yay")
            blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
            blankText.place(x=235,y=0)
            congratsText = Text(window, height = 1, background = '#dadde3', borderwidth=0, font = ("Helvetica", 20))
            congratsText.place(x = 250, y = 25)
            congratsText.delete(1.0, "end")
            congratsText.insert(1.0, "CONGRATS! You Got the Right Answer!")
            secondText = Text(window, height = 1, background='#dadde3', borderwidth=0, font = ("Helvetica", 15))
            secondText.place(x = 250, y = 70)
            secondText.delete(1.0, "end")
            secondText.insert(1.0, "Click the button below to go to the next question!")
            continueBtn = Button(window, text="Next Question", command = quad)
            continueBtn.place(x = 450, y = 200)
        else:
            hint()
    
    def hint():
        if (screenNum == 9):
            hintText = Text(window, height = 3, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 15))
            hintText.place(x = 250, y = 150)
            hintText.delete(1.0, "end")
            hintText.insert(1.0, "If you have to multiply, add the exponents, if you have to\ndivide, subtract the exponents."+
                                 "If you have the power to the \npower, multiply the exponents")

    def showSolution():
        if (screenNum == 9):
            solutionText = Text(window, height = 1, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 15))
            solutionText.place(x = 250, y = 220)
            solutionText.delete(1.0, "end")
            solutionText.insert(1.0, "The solution is " + answer)

    blankText = Text(window, height = 400, background = '#dadde3', borderwidth = 0, font = ("Helvetica", 20))
    blankText.place(x = 235, y = 0)

    sectionTitleText = Text(window, height = 1, width = 8, background='#dadde3', borderwidth = 0, font = ("Helvetica", 20))
    sectionTitleText.place(x = 250,y = 20)

    entry = Entry(window)
    entry.place(x = 550, y = 445)
    submitBtn = Button(window, text = "Submit", command = search)
    submitBtn.place(x = 700, y = 440)

    sectionTitleText.delete(1.0, "end")
    sectionTitleText.insert(1.0, "Exponent Practice")
    problemText = Text(window, height = 4, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 12))
    problemText.place(x = 250, y = 60)
    problemText.delete(1.0, "end")
    problemText.insert(1.0, "You will be given either a multiplication of exponents with the same base, " +
                            "\ndivision of exponents with the same base, or a power to a power. Your task " +
                            "\nis to solve it and show the equation in the simplest form your equation is: "+
                            "\n")

    hintBtn = Button(window, text = "Give me a hint", command = hint)
    hintBtn.place(x = 250, y = 400)

    decideOperation = random.randint(1, 3)
    firstExponent = random.randint(1, 10)
    secondExponent = random.randint(1, 10)

    question = " "
    answer = " "

    if (decideOperation == 1):
        question = "x^" + str(firstExponent) + "*x^" + str(secondExponent)
        answer = "x^" + str((firstExponent + secondExponent))
        print(answer)
    elif (decideOperation == 2):
        question = "x^" + str(firstExponent) + "/x^" + str(secondExponent)
        answer = "x^" + str((firstExponent - secondExponent))
        print(answer)
    else:
        question = "(x^" + str(firstExponent) + ")^" + str(secondExponent)
        answer = "x^" + str((firstExponent * secondExponent))
        print(answer)

    problemText.insert(4.0, question)

    solutionBtn = Button(window, text = "Give me the solution", command = showSolution)
    solutionBtn.place(x = 250, y = 440)

def seq():
    def search():
        userInput = entry.get()
        if (int(userInput) == commonChange):
            print("yay")
            blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
            blankText.place(x=235,y=0)
            congratsText = Text(window, height = 1, background = '#dadde3', borderwidth=0, font = ("Helvetica", 20))
            congratsText.place(x = 250, y = 25)
            congratsText.delete(1.0, "end")
            congratsText.insert(1.0, "CONGRATS! You Got the Right Answer!")
            secondText = Text(window, height = 1, background='#dadde3', borderwidth=0, font = ("Helvetica", 15))
            secondText.place(x = 250, y = 70)
            secondText.delete(1.0, "end")
            secondText.insert(1.0, "Click the button below to go to the next question!")
            continueBtn = Button(window, text="Next Question", command = seq)
            continueBtn.place(x = 450, y = 200)
        else:
            hint()
    
    def hint():
        hintText = Text(window, height = 5, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 15))
        hintText.place(x = 250, y = 130)
        hintText.delete(1.0, "end")
        hintText.insert(1.0, "First, figure out if the sequence is geometric or arithmetic. If \nit's geometric, the numbers will multiply by a common number."+
                                "\nIf the sequence is arithmetic, it will grow by adding the \nsame number")

    def showSolution():
        solutionText = Text(window, height = 1, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 15))
        solutionText.place(x = 250, y = 225)
        solutionText.delete(1.0, "end")
        solutionText.insert(1.0, "The solution is " + str(commonChange))

    blankText = Text(window, height = 400, background = '#dadde3', borderwidth = 0, font = ("Helvetica", 20))
    blankText.place(x = 235, y = 0)

    sectionTitleText = Text(window, height = 1, background='#dadde3', borderwidth = 0, font = ("Helvetica", 20))
    sectionTitleText.place(x = 250, y = 20)

    entry = Entry(window)
    entry.place(x = 550, y = 445)
    submitBtn = Button(window, text = "Submit", command = search)
    submitBtn.place(x = 700, y = 440)

    sectionTitleText.delete(1.0, "end")
    sectionTitleText.insert(1.0, "Sequences")
    problemText = Text(window, height = 3, background = "#dadde3", borderwidth = 0, font = ("Helvetica", 12))
    problemText.place(x = 250, y = 60)
    problemText.delete(1.0, "end")
    problemText.insert(1.0, "You will be given a set of three numbers. If the sequence is geometric, provide \nthe common ratio." +
                            "If the sequence is arithmetic provide the common difference. \nYour sequence is:"+
                            "\n")

    hintBtn = Button(window, text = "Give me a hint", command = hint)
    hintBtn.place(x = 250, y = 400)

    decideSequence = random.randint(1, 2)
    commonChange = random.randint(1, 10)
    firstTerm = random.randint(1, 10)

    question = " "

    if (decideSequence == 1):
        question = str(firstTerm) + ", " + str((firstTerm+commonChange)) + ", " + str((firstTerm+commonChange+commonChange))
        print(commonChange)
    else:
        question = str(firstTerm) + ", " + str((firstTerm*commonChange)) + ", " + str((firstTerm*commonChange*commonChange))
        print(commonChange)

    problemText.insert(5.0, question)

    solutionBtn = Button(window, text = "Give me the solution", command = showSolution)
    solutionBtn.place(x = 250, y = 440)

def about():
    blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
    blankText.place(x=235,y=0)
    sectionTitleText = Text(window, height = 15, width = 61, background='#dadde3', borderwidth = 0, font = ("Helvetica", 12))
    sectionTitleText.place(x = 240, y = 25)
    sectionTitleText.delete(1.0, "end")
    sectionTitleText.insert(1.0, "About AlgeBRO:"+
                                "\n " +
                                "\nOur programs goals are to tutor students in the subject of Algebra. We offer a " + 
                                "\nvariety of questions surrounding key ideas like solving equations, graphs, and " + 
                                "\nmultiple functions and allow students to get tips if they got an answer wrong. " + 
                                "\nWe also have our program translated into multiple languages so students from " +
                                "\ndifferent countries can also get help in the universal language of math!" +
                                "\n " +
                                "\nHow To Use AlgeBRO:" +
                                "\n " +
                                "\n1. Select the skill you want to practice on the side bar menu" +
                                "\n2. Attempt to solve the problems given." +
                                "\n3. If you are unable to solve it or just need a nudge in the right direction, just click the hint button" +
                                "\n4. Enjoy learning and improving up on your math skills!")



window = Tk()
window.geometry("800x500")
window.resizable(False, False)
window.configure(background='#dadde3')
window.title('AlgeBRO')


factorBtn = Button(window, text="Factoring", command=factor)
factorBtn.place(x = 25, y = 86)

quadBtn = Button(window, text="Quadratic Formula", command=quad)
quadBtn.place(x = 25, y = 122)

squareBtn = Button(window, text="Completing the Square", command=square)
squareBtn.place(x = 25, y = 159)

solvingBtn = Button(window, text="Solving Single Variable Equations", command=solving)
solvingBtn.place(x = 25, y = 195)

systemBtn = Button(window, text="System of Equations", command=system)
systemBtn.place(x = 25, y = 231)

exponBtn = Button(window, text="Exponents", command=expon)
exponBtn.place(x = 25, y = 268)

seqBtn = Button(window, text="Sequences", command=seq)
seqBtn.place(x = 25, y = 304)

aboutBtn = Button(window, text="About", command=about)
aboutBtn.place(x = 25, y = 450)


separator = ttk.Separator(window, orient='vertical')
separator.place(relx=0.29, rely=0, relwidth=0.001, relheight=1)

blankText = Text(window, height = 40, background='#dadde3', borderwidth=0, font = ("Helvetica", 20))
blankText.place(x=235,y=0)
sectionTitleText = Text(window, height = 15, width = 61, background='#dadde3', borderwidth = 0, font = ("Helvetica", 12))
sectionTitleText.place(x = 240, y = 25)
sectionTitleText.delete(1.0, "end")
sectionTitleText.insert(1.0, "About AlgeBRO:"+
                            "\n " +
                            "\nOur programs goals are to tutor students in the subject of Algebra. We offer a " + 
                            "\nvariety of questions surrounding key ideas like solving equations, graphs, and " + 
                            "\nmultiple functions and allow students to get tips if they got an answer wrong. " + 
                            "\n " +
                            "\nHow To Use AlgeBRO:" +
                            "\n " +
                            "\n1. Select the skill you want to practice on the side bar menu" +
                            "\n2. Attempt to solve the problems given." +
                            "\n3. If you are unable to solve it or just need a nudge in the right direction, just click the hint button" +
                            "\n4. Enjoy learning and improving up on your math skills!")

logoText = Text(window, height = 1, width = 7, background = '#dadde3', borderwidth=0, font = ("Helvetica", 20), fg='#2f91b5')
logoText.place(x = 10, y = 10)
logoText.delete(1.0, "end")
logoText.insert(1.0, "AlgeBRO")

window.mainloop()

