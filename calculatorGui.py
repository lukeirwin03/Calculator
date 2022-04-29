from curses import window
from tkinter import *
from tkinter import ttk
import csv

class GUI:

    pos = 0
    expression = ''

    def __init__(self, window):
        self.window = window
        self.style = ttk.Style(window)
        #self.style.theme_use()


        frameTop = Frame(window, width=200)
        frameTop.grid(columnspan=1)

        equation = StringVar()

        numFrame = Frame(window, width=100)
        numFrame.grid(columnspan=2)

        self.entryBox = Entry(numFrame,textvariable=equation, width=26) 
        self.entryBox.grid(padx=4,pady=4,columnspan=4)

        self.clearButton = Button(numFrame, text = 'C', fg = 'red', width = 10, command = lambda: self.clear())
        self.clearButton.grid(row=1,column=0, columnspan=2)
        self.backButton = Button(numFrame, text='<-', width=10, command = lambda: self.backspace())
        self.backButton.grid(row=1, column=2, columnspan=2)

        self.one = Button(numFrame, text = '1', width = 3, command = lambda: self.clicked(1))
        self.one.grid(row=4,column=2)
        self.two = Button(numFrame, text = '2', width = 3, command = lambda: self.clicked(2))
        self.two.grid(row=4,column=1)
        self.three = Button(numFrame, text = '3', width = 3, command = lambda: self.clicked(3))
        self.three.grid(row=4,column=0)
        self.four = Button(numFrame, text = '4', width = 3, command = lambda: self.clicked(4))
        self.four.grid(row=3,column=2)
        self.five = Button(numFrame, text = '5', width = 3, command = lambda: self.clicked(5))
        self.five.grid(row=3,column=1)
        self.six = Button(numFrame, text = '6', width = 3, command = lambda: self.clicked(6))
        self.six.grid(row=3,column=0)
        self.seven = Button(numFrame, text = '7', width = 3, command = lambda: self.clicked(7))
        self.seven.grid(row=2,column=2)
        self.eight = Button(numFrame, text = '8', width = 3, command = lambda: self.clicked(8))
        self.eight.grid(row=2,column=1)
        self.nine = Button(numFrame, text = '9', width = 3, command = lambda: self.clicked(9))
        self.nine.grid(row=2,column=0)
        self.zero = Button(numFrame, text = '0\t', width = 10, command = lambda: self.clicked(0))
        self.zero.grid(row=5,column=0, columnspan=2)

        self.add = Button(numFrame, text = '/', width = 3, command = lambda: self.clicked('/'))
        self.add.grid(row=2,column=3)
        self.sub = Button(numFrame, text = '*', width = 3, command = lambda: self.clicked('*'))
        self.sub.grid(row=3,column=3)
        self.mult = Button(numFrame, text = '+', width = 3, command = lambda: self.clicked('+'))
        self.mult.grid(row=4,column=3)
        self.div = Button(numFrame, text = '-', width = 3, command = lambda: self.clicked('-'))
        self.div.grid(row=5,column=3)
        
        self.dec = Button(numFrame, text='.', width=3, command = lambda: self.clicked('.'))
        self.dec.grid(row=5, column=2)
        self.calculate_button = Button(numFrame, text="=", width=3, command=self.calculate)
        self.calculate_button.grid(row=6, column=3)
        self.history_button = Button(numFrame, text='History', width = 3, command= self.createHistoryWin)
        self.history_button.grid(row=6, column = 2)

    def clicked(self, val):
        self.entryBox.insert(END, f'{val}')
        self.expression = self.entryBox.get()

    def clear(self):
        self.expression = ''
        self.entryBox.delete(0, END)

    def backspace(self):
        self.expression = self.expression[:len(self.expression)-1]
        self.entryBox.delete(0,END)
        self.entryBox.insert(END, self.expression)
        

    def calculate(self):
        self.answer = str(self.expression)
        self.entryBox.delete(0,END)
        self.entryBox.insert(END, 'ERROR')
        self.answer = eval(self.answer)
        self.store()
        self.entryBox.delete(0,END)
        self.entryBox.insert(0,str(self.answer))

    def store(self):
        with open('history.csv', 'a+', newline='') as outfile:
            appender = csv.writer(outfile, delimiter=',')
            appender.writerow([self.expression, self.answer])

    def createHistoryWin(self):
        historyWin = Toplevel()
        historyWin.title('Calculation History')
        outline = Frame(historyWin, highlightbackground='blue', highlightthickness=2)
        outline.grid(padx=3,pady=3, ipadx=3,ipady=3)
        with open('history.csv', 'r', newline='') as outfile:
            rowcount = 0
            box = Listbox(outline)
            for line in outfile:
                line = line.split(',')
                box.insert(rowcount, f'{line[0]} = {line[1]}')
                rowcount += 1
            box.grid(row=1, column=0)
        historyWin.geometry('220x220')
        
