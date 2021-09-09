from tkinter import *
from tkinter import messagebox
from tkmacosx import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
from pathlib import Path


def program_exit_warning():
    if messagebox.askokcancel('Closing the program...', 'Are you sure you want to close the program?', default="cancel",
                              icon="warning"):
        root.destroy()


def save_data():
    file = open(f'data/{checker_earnings_expenses}.txt', 'w')
    file.writelines("\n".join(listbox.get(0, END)))
    file.writelines('\n' + str(counter['text']))
    file.close()


def return_main():
    child_of_root.destroy()
    return main()


def delete_row():
    selected_string = list(listbox.curselection())
    selected_string.reverse()
    temp = listbox.get(list(listbox.curselection()))
    for index_of_selected_string in selected_string:
        listbox.delete(index_of_selected_string)

    counter['text'] -= int(temp[temp.rfind(' ') + 1::])

    save_data()


def insert_row():
    if type(float_field.get()) != 'str' and len(string_field.get()) < 16 and len(float_field.get()) < 8:
        listbox.insert(END, string_field.get() + (
                ' ' * (34 - len(float_field.get()) - len(string_field.get()))) + float_field.get())
        listbox.pack(side=BOTTOM, ipadx=70)
        listbox.place(x=202, y=300)

        counter['text'] += int(float_field.get())

        save_data()


def earnings():
    global child_of_root
    global string_field
    global float_field
    global listbox
    global counter
    global checker_earnings_expenses
    checker_earnings_expenses = 'earnings'

    root.destroy()
    child_of_root = Tk()
    child_of_root['bg'] = 'black'
    child_of_root.title('Financial Control: EARNINGS')
    child_of_root.geometry('800x600')
    child_of_root.resizable(width=False, height=False)

    child_text1 = Label(child_of_root, text='ENTER YOUR EARNINGS', font=('Classic Console', 60), bg='black',
                        fg='gray')
    child_text2 = Label(child_of_root, text='EARNING', font=('Classic Console', 30),
                        bg='black', fg='gray')
    child_text3 = Label(child_of_root, text='SUM', font=('Classic Console', 30),
                        bg='black', fg='gray')
    child_text4 = Label(child_of_root, text='LIST / TOTAL SUM:', font=('Classic Console', 30),
                        bg='black', fg='gray')
    child_text1.pack()
    child_text2.place(x=200, y=60)
    child_text3.place(x=500, y=60)
    child_text4.place(x=200, y=250)

    counter = Label(child_of_root, text=0, font=('Classic Console', 30),
                    bg='black', fg='gray')
    counter.place(x=420, y=250)

    string_field = Entry(child_of_root, font=('Classic Console', 30), bg='black', fg='white')
    float_field = Entry(child_of_root, font=('Classic Console', 30), bg='black', fg='white')
    string_field.place(x=200, y=100)
    float_field.place(x=500, y=100, width=100)

    insert_button = Button(child_of_root, text='INSERT', font=('Classic Console', 30), fg='lawn green', bg='black',
                           borderless=1, activebackground='black', activeforeground='gray',
                           command=insert_row)
    delete_button = Button(child_of_root, text='DELETE', font=('Classic Console', 30), fg='red',
                           bg='black',
                           borderless=1, activebackground='black', activeforeground='gray',
                           command=delete_row)
    return_button = Button(child_of_root, text='MAIN MENU', font=('Classic Console', 30), fg='white',
                           bg='black',
                           borderless=1, activebackground='black', activeforeground='gray',
                           command=return_main)
    insert_button.place(x=200, y=150, width=100)
    delete_button.place(x=500, y=150, width=100)
    return_button.place(x=640, y=560, width=150)

    listbox = Listbox(child_of_root, font=('Classic Console', 30), bg='black', fg='gray', width=50)
    with open('data/earnings.txt', 'r') as file:
        read_file = file.readlines()
    for element in read_file:
        if element == read_file[-1]:
            counter['text'] = int(element)
        elif element != '\n':
            listbox.insert(END, element)
    listbox.pack(side=BOTTOM, ipadx=70)
    listbox.place(x=202, y=300)


def expenses():
    global child_of_root
    global string_field
    global float_field
    global listbox
    global counter
    global checker_earnings_expenses
    checker_earnings_expenses = 'expenses'

    root.destroy()
    child_of_root = Tk()
    child_of_root['bg'] = 'black'
    child_of_root.title('Financial Control: EXPENSES')
    child_of_root.geometry('800x600')
    child_of_root.resizable(width=False, height=False)

    child_text1 = Label(child_of_root, text='ENTER YOUR EXPENSES', font=('Classic Console', 60), bg='black',
                        fg='gray')
    child_text2 = Label(child_of_root, text='EXPENSES', font=('Classic Console', 30),
                        bg='black', fg='gray')
    child_text3 = Label(child_of_root, text='COST', font=('Classic Console', 30),
                        bg='black', fg='gray')
    child_text4 = Label(child_of_root, text='LIST / TOTAL COST:', font=('Classic Console', 30),
                        bg='black', fg='gray')
    child_text1.pack()
    child_text2.place(x=200, y=60)
    child_text3.place(x=500, y=60)
    child_text4.place(x=200, y=250)

    counter = Label(child_of_root, text=0, font=('Classic Console', 30),
                    bg='black', fg='gray')
    counter.place(x=420, y=250)

    string_field = Entry(child_of_root, font=('Classic Console', 30), bg='black', fg='white')
    float_field = Entry(child_of_root, font=('Classic Console', 30), bg='black', fg='white')
    string_field.place(x=200, y=100)
    float_field.place(x=500, y=100, width=100)

    insert_button = Button(child_of_root, text='INSERT', font=('Classic Console', 30), fg='lawn green', bg='black',
                           borderless=1, activebackground='black', activeforeground='gray',
                           command=insert_row)
    delete_button = Button(child_of_root, text='DELETE', font=('Classic Console', 30), fg='red',
                           bg='black',
                           borderless=1, activebackground='black', activeforeground='gray',
                           command=delete_row)
    return_button = Button(child_of_root, text='MAIN MENU', font=('Classic Console', 30), fg='white',
                           bg='black',
                           borderless=1, activebackground='black', activeforeground='gray',
                           command=return_main)
    insert_button.place(x=200, y=150, width=100)
    delete_button.place(x=500, y=150, width=100)
    return_button.place(x=640, y=560, width=150)

    listbox = Listbox(child_of_root, font=('Classic Console', 30), bg='black', fg='gray', width=50)
    with open('data/expenses.txt', 'r') as file:
        read_file = file.readlines()
    for element in read_file:
        if element == read_file[-1]:
            counter['text'] = int(element)
        elif element != '\n':
            listbox.insert(END, element)
    listbox.pack(side=BOTTOM, ipadx=70)
    listbox.place(x=202, y=300)


def analyse():
    global child_of_root

    root.destroy()
    child_of_root = Tk()
    child_of_root['bg'] = 'black'
    child_of_root.title('Financial Control: STAT')
    child_of_root.geometry('800x600')
    child_of_root.resizable(width=False, height=False)

    figure_font = {'fontname': 'Classic Console'}
    figure = plt.Figure(figsize=(6, 10), dpi=80)
    ax_earnings = figure.add_subplot(211)
    ax_expenses = figure.add_subplot(212)
    FigureCanvasTkAgg(figure, child_of_root).get_tk_widget().pack(ipadx=200, ipady=350)
    figure.subplots_adjust(wspace=0.2, hspace=0.2)
    ax_earnings.set_title('EARNINGS STATISTIC', **figure_font, size=30, color='gray')
    ax_expenses.set_title('EXPENSES STATISTIC', **figure_font, size=30, color='gray')
    ax_earnings.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax_expenses.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax_earnings.xaxis.set_major_locator(MultipleLocator(base=1))
    ax_expenses.xaxis.set_major_locator(MultipleLocator(base=1))
    figure.patch.set_facecolor('xkcd:black', **figure_font)
    ax_earnings.tick_params(axis='x', colors='white')
    ax_earnings.tick_params(axis='y', colors='white')
    ax_expenses.tick_params(axis='x', colors='white')
    ax_expenses.tick_params(axis='y', colors='white')
    ax_earnings.patch.set_facecolor('black')
    ax_expenses.patch.set_facecolor('black')

    try:
        with open('data/earnings.txt', 'r') as file:
            read_file = file.readlines()
        y_earnings_list = list()
        for element in read_file:
            if element != read_file[-1] and element != '\n':
                y_earnings_list.append(int(element[element.rfind(' ') + 1::]))
        ax_earnings.plot(y_earnings_list, 'or-')
    except IOError:
        Path('data/earnings.txt').touch()

    try:
        with open('data/expenses.txt', 'r') as file:
            read_file = file.readlines()
        y_expenses_list = list()
        for element in read_file:
            if element != read_file[-1] and element != '\n':
                y_expenses_list.append(int(element[element.rfind(' ') + 1::]))
        ax_expenses.plot(y_expenses_list, 'or-')
    except IOError:
        Path('data/expenses.txt').touch()

    return_button = Button(child_of_root, text='MAIN MENU', font=('Classic Console', 30), fg='white',
                           bg='black',
                           borderless=1, activebackground='black', activeforeground='gray',
                           command=return_main)
    return_button.place(x=640, y=560, width=150)


def main():
    global root

    root = Tk()
    root['bg'] = 'black'
    root.title('Financial Control')
    root.geometry('800x600')
    root.resizable(width=False, height=False)
    root.protocol('WM_DELETE_WINDOW', program_exit_warning)

    root_text1 = Label(root, text='WELCOME TO', font=('Classic Console', 60), bg='black', fg='gray')
    root_text2 = Label(root, text='FINANCIAL CONTROL APPLICATION', font=('Classic Console', 60), bg='black',
                       fg='gray')
    root_text3 = Label(root, text='', bg='black')
    root_text4 = Label(root, text='SELECT A SECTION', font=('Classic Console', 60), bg='black', fg='white')
    root_text1.pack()
    root_text2.pack()
    root_text3.pack()
    root_text4.pack()

    earnings_frame = Frame(root, bg='black')
    earnings_frame.pack(side=LEFT)
    expenses_frame = Frame(root, bg='black')
    expenses_frame.pack(side=RIGHT)
    bottom_frame = Frame(root, bg='black')
    bottom_frame.pack(side=BOTTOM)

    earnings_button = Button(earnings_frame, text='EARNINGS', font=('Classic Console', 60), fg='lawn green', bg='black',
                             borderless=1, activebackground='black', activeforeground='gray', command=earnings)
    expenses_button = Button(expenses_frame, text='EXPENSES', font=('Classic Console', 60), fg='red', bg='black',
                             borderless=1, activebackground='black', activeforeground='gray', command=expenses)
    analyse_button = Button(bottom_frame, text='STAT', font=('Classic Console', 60), fg='white', bg='black',
                            borderless=1,
                            activebackground='black', activeforeground='gray', command=analyse)
    earnings_button.pack(padx=50)
    expenses_button.pack(padx=50)
    analyse_button.pack(pady=50)

    root.mainloop()


main()
