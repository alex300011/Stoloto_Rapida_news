from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Stoloto Rapido')
frame = Frame(window)
listbox = Listbox(frame, height = 20, width = 30)
lst = [[17, 19, 1, 9, 10, 6, 12, 14],[10, 15, 19, 1, 9, 12, 14, 17],[19, 3, 2, 8, 9, 6, 16, 4],[13, 16, 1, 14, 11, 6, 17, 5]]
for i  in range(0,len(lst)):
    listbox.insert(i, str(lst[i]))


def dialog():
    box.showinfo('Selection', 'Your Choice: ' + listbox.get(listbox.curselection()))

btn = Button( frame, text = 'Choose' , command = dialog )

btn.pack( side = RIGHT , padx = 5 )
listbox.pack( side = LEFT )
frame.pack( padx = 30 , pady = 30 )

window.mainloop()
