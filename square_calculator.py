from tkinter import *
import customtkinter as ctk

root = Tk()
root.geometry('460x700+200+100')
root.title("Calculator")
root.configure(background='#111')
root.resizable(False, False)



## commands
def cut_one():
    current = input_display.get()
    input_display.delete(0, END)
    input_display.insert(END, current[:-1])


def insert_mod():
    input_display.insert(END, '%')


def insert_pow():
    input_display.insert(END, '**')


def insert_div():
    input_display.insert(END, '/')


def insert_seven():
    input_display.insert(END, '7')


def insert_eight():
    input_display.insert(END, '8')


def insert_nine():
    input_display.insert(END, '9')


def insert_mul():
    input_display.insert(END, '*')


def insert_four():
    input_display.insert(END, '4')


def insert_five():
    input_display.insert(END, '5')


def insert_six():
    input_display.insert(END, '6')


def insert_sub():
    input_display.insert(END, '-')


def insert_one():
    input_display.insert(END, '1')


def insert_two():
    input_display.insert(END, '2')


def insert_three():
    input_display.insert(END, '3')


def insert_dot():
    input_display.insert(END, '.')


def insert_plus():
    input_display.insert(END, '+')


def insert_zero():
    input_display.insert(END, '0')


def clear_all():
    input_display.delete(0, END)


def result_output():
    content = input_display.get()
    
    try:
        result = eval(content)
        output_display.delete(0, END)
        output_display.insert(END, result)
    except:
        output_display.delete(0, END)
        output_display.insert(END, 'Expression Error')
        


### Display
output_display = ctk.CTkEntry(root, width=440, height=80,
                               fg_color='black',
                               bg_color='black',
                               corner_radius=0,
                               text_color='white',
                               border_width=1,
                               border_color='black',
                               font=('Arial', 26, 'bold'))
output_display.place(x=10, y=10)

input_display = ctk.CTkEntry(root, width=440, height=80,
                               fg_color='black',
                               bg_color='black',
                               corner_radius=0,
                               text_color='white',
                               border_color='black',
                               border_width=1,
                               font=('Arial', 36, 'bold'))
input_display.place(x=10, y=70)




### Make Buttons
clear = ctk.CTkButton(root, text='C',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='white',
                      fg_color='grey',
                      hover=False,
                      bg_color='#111',
                      command=cut_one)
clear.place(x=20, y=200)


modulus = ctk.CTkButton(root, text='%',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='white',
                      fg_color='grey',
                      hover=False,
                      bg_color='#111', 
                      command=insert_mod)
modulus.place(x=120, y=200)


power = ctk.CTkButton(root, text='^',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='white',
                      fg_color='grey',
                      hover=False,
                      bg_color='#111',
                      command=insert_pow)
power.place(x=220, y=200)


div = ctk.CTkButton(root, text='/',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='white',
                      fg_color='orange',
                      hover=False,
                      bg_color='#111',
                      command=insert_div)
div.place(x=320, y=200)


seven = ctk.CTkButton(root, text='7',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='skyblue',
                      hover=False,
                      bg_color='#111',
                      command=insert_seven)
seven.place(x=20, y=300)


eight = ctk.CTkButton(root, text='8',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='skyblue',
                      hover=False,
                      bg_color='#111',
                      command=insert_eight)
eight.place(x=120, y=300)


nine = ctk.CTkButton(root, text='9',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='skyblue',
                      hover=False,
                      bg_color='#111',
                      command=insert_nine)
nine.place(x=220, y=300)


mul = ctk.CTkButton(root, text='*',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='white',
                      fg_color='orange',
                      hover=False,
                      bg_color='#111',
                      command=insert_mul)
mul.place(x=320, y=300)


four = ctk.CTkButton(root, text='4',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='skyblue',
                      hover=False,
                      bg_color='#111',
                      command=insert_four)
four.place(x=20, y=400)


five = ctk.CTkButton(root, text='5',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='skyblue',
                      hover=False,
                      bg_color='#111',
                      command=insert_five)
five.place(x=120, y=400)


six = ctk.CTkButton(root, text='6',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='skyblue',
                      hover=False,
                      bg_color='#111', 
                      command=insert_six)
six.place(x=220, y=400)


sub = ctk.CTkButton(root, text='-',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='white',
                      fg_color='orange',
                      hover=False,
                      bg_color='#111',
                      command=insert_sub)
sub.place(x=320, y=400)


one = ctk.CTkButton(root, text='1',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='skyblue',
                      hover=False,
                      bg_color='#111',
                      command=insert_one)
one.place(x=20, y=500)


two = ctk.CTkButton(root, text='2',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='skyblue',
                      hover=False,
                      bg_color='#111',
                      command=insert_two)
two.place(x=120, y=500)


three = ctk.CTkButton(root, text='3',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='skyblue',
                      hover=False,
                      bg_color='#111',
                      command=insert_three)
three.place(x=220, y=500)


plus = ctk.CTkButton(root, text='+',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='white',
                      fg_color='orange',
                      hover=False,
                      bg_color='#111',
                      command=insert_plus)
plus.place(x=320, y=500)


all_clear = ctk.CTkButton(root, text='AC',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='red',
                      hover=False,
                      bg_color='#111',
                      command=clear_all)
all_clear.place(x=20, y=600)


zero = ctk.CTkButton(root, text='0',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='skyblue',
                      hover=False,
                      bg_color='#111',
                      command=insert_zero)
zero.place(x=120, y=600)


dot = ctk.CTkButton(root, text='.',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='black',
                      fg_color='skyblue',
                      hover=False,
                      bg_color='#111',
                      command=insert_dot)
dot.place(x=220, y=600)


equal = ctk.CTkButton(root, text='=',
                      font=('Roboto', 26, 'bold'),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='white',
                      fg_color='orange',
                      hover=False,
                      bg_color='#111', 
                      command=result_output)
equal.place(x=320, y=600)




root.mainloop()
