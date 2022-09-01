from tkinter import *

gui = Tk()
gui.title('Simple Calculator')
gui.geometry('300x300')
gui.iconbitmap('D:\Downloads\img_521113.ico')

screen = Entry(gui,width=45)
screen.grid(row=0,column=0,columnspan=4)

#Functions
def pressNum(number):
    current = screen.get()
    screen.delete(0,END)
    screen.insert(0,str(current) + str(number))

def pressClear():
    screen.delete(0, END)

def pressOperator(which):
    global last_op
    global f_num

    if which == '+':
        first = screen.get()
        screen.delete(0, END)
        f_num = float(first)

    elif which == '-':
        first = screen.get()
        screen.delete(0, END)
        f_num = float(first)

    elif which == '*':
        first = screen.get()
        screen.delete(0, END)
        f_num = float(first)

    elif which == '/':
        first = screen.get()
        screen.delete(0, END)
        f_num = float(first)

    elif which == '=':
        second = screen.get()
        screen.delete(0, END)
        if last_op == '+':
            screen.insert(0, float(f_num) + int(second))
        elif last_op == '-':
            screen.insert(0, float(f_num) - int(second))
        elif last_op == '*':
            screen.insert(0, float(f_num) * int(second))
        elif last_op == '/':
            if second == '0':
                screen.insert(0,'Math Error: cant divide by zero.')
            else:
                screen.insert(0, float(f_num) / int(second))
        last_op = None
    last_op = which

#Buttons
one = Button(gui,font='arial 10 bold',text='1',height=3,width=5,command=lambda: pressNum(1)).grid(row=1,column=0)
two = Button(gui,font='arial 10 bold',text='2',height=3,width=5,command=lambda: pressNum(2)).grid(row=1,column=1)
three = Button(gui,font='arial 10 bold',text='3',height=3,width=5,command=lambda: pressNum(3)).grid(row=1,column=2)
four = Button(gui,font='arial 10 bold',text='4',height=3,width=5,command=lambda: pressNum(4)).grid(row=2,column=0)
five = Button(gui,font='arial 10 bold',text='5',height=3,width=5,command=lambda: pressNum(5)).grid(row=2,column=1)
six = Button(gui,font='arial 10 bold',text='6',height=3,width=5,command=lambda: pressNum(6)).grid(row=2,column=2)
seven = Button(gui,font='arial 10 bold',text='7',height=3,width=5,command=lambda: pressNum(7)).grid(row=3,column=0)
eight = Button(gui,font='arial 10 bold',text='8',height=3,width=5,command=lambda: pressNum(8)).grid(row=3,column=1)
nine = Button(gui,font='arial 10 bold',text='9',height=3,width=5,command=lambda: pressNum(9)).grid(row=3,column=2)
zero = Button(gui,font='arial 10 bold',text='0',height=3,width=5,command=lambda: pressNum(0)).grid(row=4,column=0)
add = Button(gui,font='arial 10 bold',text='+',height=3,width=5,command=lambda: pressOperator('+')).grid(row=1,column=3)
sub = Button(gui,font='arial 10 bold',text='-',height=3,width=5,command=lambda: pressOperator('-')).grid(row=2,column=3)
mul = Button(gui,font='arial 10 bold',text='*',height=3,width=5,command=lambda: pressOperator('*')).grid(row=3,column=3)
div = Button(gui,font='arial 10 bold',text='/',height=3,width=5,command=lambda: pressOperator('/')).grid(row=4,column=3)
AC = Button(gui,font='arial 10 bold',text='AC',height=3,width=5, command=pressClear).grid(row=4,column=1)
equal = Button(gui,font='arial 10 bold',text='=',height=3,width=5,command=lambda: pressOperator('=')).grid(row=4,column=2)
exit = Button(gui,font='arial 10 bold', text='Exit', command=gui.quit).grid(row=5,column=0)

gui.mainloop()