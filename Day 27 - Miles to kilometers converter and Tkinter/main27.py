import tkinter

window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # This adds padding around the window


# Label

my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label['text'] = 'old text'
my_label.config(text='new text')
my_label.grid(column=0, row=0)  # If 'grid' is used, 'pack' cannot be used in the rest of the file
# my_label.place(x=0, y=0)
# my_label.pack()  # If 'place' is used, 'pack' is not necessary
my_label.config(padx=20, pady=20)  # This adds padding to this specific element

# Buttons
def button_click():
    my_label.config(text=input.get())


button = tkinter.Button(text='Click me', command=button_click)
button.grid(column=1, row=1)

button2 = tkinter.Button(text='New button')
button2.grid(column=2, row=0)

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)


# Entry







window.mainloop()
