from tkinter import *

window = Tk()
window.title('Mile to km converter')
window.minsize(200, 120)
window.config(padx=15, pady=15)


def convert():
    result_label.config(text=round(float(entry.get()) * 1.609, 2))


# entry
entry = Entry(width=10)
entry.grid(row=0, column=1)

# labels
mile_label = Label(text='Miles')
mile_label.grid(row=0, column=2)

equal_label = Label(text='is equal to')
equal_label.grid(row=1, column=0)

km_label = Label(text='Km')
km_label.grid(row=1, column=2)

# result label
result_label = Label(text=0)
result_label.grid(row=1, column=1)

# button
calculate_button = Button(text='Calculate', command=convert)
calculate_button.grid(row=2, column=1)

window.mainloop()
