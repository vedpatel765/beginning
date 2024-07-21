import tkinter as tk
window = tk.Tk()
window.title("Calculator")
window.configure(background="#34A2FE")
window.geometry("800x400")
x_var=tk.IntVar()
y_var=tk.IntVar()
result=tk.IntVar()

frame0=tk.Frame(window, borderwidth=3, bg='#34A2FE', padx=2, pady=2, highlightbackground="white",highlightthickness=3)
label_main = tk.Label(text="Calculator", 
                      background="#34A2FE",
                      foreground="white",
                      font=("Helvetica", 30,'bold'),
                      width=30,
                      height=2)

def add():
    x=int(x_var.get())
    y=int(y_var.get())
    result.set('Result: '+str(x+y))

def sub():
    x=x_var.get()
    y=y_var.get()
    result.set('Result: '+str(x-y))

def mul():
    x=x_var.get()
    y=y_var.get()
    result.set('Result: '+str(x*y))

def div():
    x=x_var.get()
    y=y_var.get()
    result.set('Result: '+str(x/y))

def remainder():
    x=x_var.get()
    y=y_var.get()
    result.set('Result: '+str(x%y))

def clear():
    x_var.set(0)
    y_var.set(0)
    result.set('Result: ')

frame1=tk.Frame(window, borderwidth=3, padx=5, pady=5, bg='#34A2FE')
frame2=tk.Frame(frame1, borderwidth=3, padx=5, pady=5, bg='#34A2FE')
entry1=tk.Entry(frame2, textvariable=x_var, font=("Helvetica", 14), justify="center")
frame3=tk.Frame(frame1, borderwidth=3, padx=5, pady=5, bg='#34A2FE')
entry2=tk.Entry(frame3, textvariable=y_var, font=("Helvetica", 14), justify="center")

button1=tk.Button(text="Add", font=("Helvetica", 11), command=add, bg="#98FF4E", borderwidth=5, relief="raised", master=frame0, padx=20)
button2=tk.Button(text="Subtract", font=("Helvetica", 11), command=sub, bg="#FF6E4E", borderwidth=5, relief="raised", master=frame0, padx=20)
button3=tk.Button(text="Multiply", font=("Helvetica", 11), command=mul, bg="#4EFFD4", borderwidth=5, relief="raised", master=frame0, padx=20)
button4=tk.Button(text="Divide", font=("Helvetica", 11), command=div, bg="#FA4EFF", borderwidth=5, relief="raised", master=frame0, padx=20)
button5=tk.Button(text="Remainder", font=("Helvetica", 11), command=remainder, bg="#4E4EFF", borderwidth=5, relief="raised", master=frame0, padx=20)

frame4=tk.Frame(window, padx=8, pady=6, bg='#34A2FE')
label_result=tk.Label(frame4, textvariable=result, font=("Helvetica", 20, 'bold'),fg='white', justify="center", bg='#34A2FE', padx=10, pady=10)
button6=tk.Button(text="Clear", font=("Helvetica", 11), command=clear, bg="#FF4E4E", borderwidth=5, relief="raised", master=frame4, padx=20)

label_main.pack()
frame2.pack()
frame3.pack()
frame1.pack()
entry1.pack()
entry2.pack()
frame0.pack()
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.LEFT)
button5.pack(side=tk.LEFT)
frame4.pack()
label_result.pack(side=tk.LEFT)
button6.pack(side=tk.LEFT)
window.mainloop()