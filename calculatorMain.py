from calculatorGui import *
from tkinter import *

def main():

    window = Tk()
    window.title('Calculator')
    window.geometry('255x210')
    window.resizable(False,False)

    widgets = GUI(window)

    window.mainloop()


if __name__ == '__main__':
    main()
