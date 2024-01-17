import tkinter as tk
from turtle import width
calculation=""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol) + ' '
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0,"error")

def clear_field():
    global calculation
    calculation= ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.title("S.Fiz's calculator")
root.geometry("400x500") 

style_font = ("Arial", 16)
style_padding = 5

text_result = tk.Text(root, height=4, width=22,font=("arial", 24))
text_result.grid(columnspan=5, pady=(20, 0))


bg_color= "#317773"
text_color=  "#ffffff"

root.configure(bg=bg_color)
text_result.configure(bg=bg_color, fg=text_color)

btn_1=tk.Button(root,text="1",command=lambda:add_to_calculation(1),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_1.grid(row=5,column=1)
btn_2=tk.Button(root,text="2",command=lambda:add_to_calculation(2),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_2.grid(row=5,column=2)
btn_3=tk.Button(root,text="3",command=lambda:add_to_calculation(3),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_3.grid(row=5,column=3)
btn_4=tk.Button(root,text="4",command=lambda:add_to_calculation(4),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_4.grid(row=4,column=1)
btn_5=tk.Button(root,text="5",command=lambda:add_to_calculation(5),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_5.grid(row=4,column=2)
btn_6=tk.Button(root,text="6",command=lambda:add_to_calculation(6),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_6.grid(row=4,column=3)
btn_7=tk.Button(root,text="7",command=lambda:add_to_calculation(7),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_7.grid(row=3,column=1)
btn_8=tk.Button(root,text="8",command=lambda:add_to_calculation(8),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_8.grid(row=3,column=2)
btn_9=tk.Button(root,text="9",command=lambda:add_to_calculation(9),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_9.grid(row=3,column=3)
btn_0=tk.Button(root,text="0",command=lambda:add_to_calculation(0),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_0.grid(row=6,column=1)
btn_plus=tk.Button(root,text="+",command=lambda:add_to_calculation("+"),height=5,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_plus.grid(row=5,column=4,rowspan=2)
btn_minus=tk.Button(root,text="-",command=lambda:add_to_calculation("-"),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_minus.grid(row=4,column=4)
btn_mul=tk.Button(root,text="x",command=lambda:add_to_calculation("*"),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_mul.grid(row=3,column=4)
btn_div=tk.Button(root,text="/",command=lambda:add_to_calculation("/"),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_div.grid(row=2,column=4)
btn_open=tk.Button(root,text="(",command=lambda:add_to_calculation("("),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_open.grid(row=2,column=2)
btn_close=tk.Button(root,text=")",command=lambda:add_to_calculation(")"),height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_close.grid(row=2,column=3)
btn_equal=tk.Button(root,text="=",command=evaluate_calculation,height=2,width=15, font=style_font, bg=bg_color, fg=text_color)
btn_equal.grid(row=6,column=2,columnspan=2)
btn_clear=tk.Button(root,text="Clear",command=clear_field,height=2,width=7, font=style_font, bg=bg_color, fg=text_color)
btn_clear.grid(row=2,column=1)
root.mainloop()