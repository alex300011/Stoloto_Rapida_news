from tkinter import *
import tkinter.messagebox as box
'''Основной интерфейс на стадии разработки'''

def dialog():
    box.showinfo('Selection', 'Your Choice: ' + listbox.get(listbox.curselection()))

window = Tk()
window.title('Stoloto Rapido')
frame = Frame(master=window, height = 15, width = 15)
frame.pack()

btn = Button(master=window, text = 'Choose' , command = dialog )
btn.place(x=5, y=0)


listbox = Listbox(master=window, height = 10, width = 30)
listbox.place(x = 5 , y = 15)


lst = [[17, 19, 1, 9, 10, 6, 12, 14],[10, 15, 19, 1, 9, 12, 14, 17],[19, 3, 2, 8, 9, 6, 16, 4],[13, 16, 1, 14, 11, 6, 17, 5]]
for i in range(0,len(lst)):
    listbox.insert(i, str(lst[i]))






#btn.pack( side = TOP , padx = 5 )
listbox.pack( side = LEFT )
frame.pack( padx = 30 , pady = 30 )

window.mainloop()
