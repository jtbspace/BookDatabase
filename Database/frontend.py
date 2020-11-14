from tkinter import *
from tkinter import messagebox
import backend
# pyinstaller --windowed --onefile frontend.py
def get_sel_row(event):
    global slected_row
    try: 
        index = list1.curselection()[0] 
    except NameError:
        return
    except IndexError:
        return
    slected_row=list1.get(index)
    return slected_row
    t1.delete(0,END)
    t1.insert(END,slected_row[1])
    t2.delete(0,END)
    t2.insert(END,slected_row[2])
    t3.delete(0,END)
    t3.insert(END,slected_row[3])
    t4.delete(0,END)
    t4.insert(END,slected_row[4])

def view_com():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
def search_com():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)
def add_com():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
    view_com()
def delete_com():
    backend.delete(slected_row[0])
    view_com()
def update_com():
    backend.update(slected_row[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_com()
def switch():
    if ba["state"] == "normal" or bb["state"] == "normal":
        ba["state"] = "disabled"
        bb["state"] = "disabled"
    else:
        bb["state"] = "normal" 
        ba["state"] = "normal" 
def hide_me():
    btn.grid()
    btn2.grid()
    et0.grid()
def pas_me():
    if pass_word.get() =='password':
        btn2.grid_remove()
        btn.grid_remove()
        et0.grid_remove()
        switch()
    else:
        btn.grid()
        btn2.grid()
        et0.grid()

window=Tk()
window.wm_title('BookStore')

window.configure(bg='#add8e6')

messagebox.showwarning("Warning","Do not delete the 'books.db' file or data will be lost")
window.resizable(width=False, height=False)
et1=Label(window,text="Title:",bg='#a9eab9')
et1.grid(row=0,column=0)
title_text=StringVar()
t1 = Entry(window, textvariable=title_text,bg ='#eadaa9')
t1.grid(row=0,column=1)

et2=Label(window,text="Author:",bg='#a9eab9')
et2.grid(row=0,column=2)
author_text=StringVar()
t2 = Entry(window, textvariable=author_text,bg ='#eadaa9')
t2.grid(row=0,column=3)

et3=Label(window,text="Year:",bg='#a9eab9')
et3.grid(row=1,column=0)
year_text=StringVar()
t3 = Entry(window, textvariable=year_text,bg ='#eadaa9')
t3.grid(row=1,column=1)

et4=Label(window,text="ISBN:",bg='#a9eab9')
et4.grid(row=1,column=2)
isbn_text=StringVar()
t4 = Entry(window, textvariable=isbn_text,bg ='#eadaa9')
t4.grid(row=1,column=3)

list1=Listbox(window, height=8,width=35,bg ='#eadaa9')
list1.grid(row=2,column=0,rowspan=8,columnspan=2)

sb1=Scrollbar(window,bg ='#eadaa9')
sb1.grid(row=2,column=2,rowspan=8)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_sel_row)

b1 = Button(window,text="View All",width=12, command=view_com,bg ='#a9eab9',activebackground='#add8e6')
b1.grid(row=3, column=3)
b2 = Button(window,text="Search Entry",width=12,command=search_com,bg ='#a9eab9',activebackground='#add8e6')
b2.grid(row=4, column=3)
bb = Button(window,text="Add Entry",state="disabled",width=12,command=add_com,bg ='#a9eab9',activebackground='#add8e6')
bb.grid(row=5, column=3)
b4 = Button(window,text="Update Entry",width=12,command=update_com,bg ='#a9eab9',activebackground='#add8e6')
b4.grid(row=6, column=3)
ba = Button(window,text="Delete",state="disabled",width=12,command=delete_com,bg ='#eaa9ba',activebackground='#add8e6')
ba.grid(row=7, column=3)
b4 = Button(window,text="Close",width=12,command=window.destroy,bg ='#eaa9ba',activebackground='#add8e6')
b4.grid(row=8, column=3)
b5 = Button(window,text="Admin",width=12,command=hide_me,bg ='#eaa9ba',activebackground='#add8e6')
b5.grid(row=9, column=3)

et0=Label(window,text="Password:",bg='#a9eab9')
et0.grid(row=10,column=0)
btn=Button(window, text="Enter",command=pas_me,bg ='#a9eab9',activebackground='#add8e6')
btn.grid(row=10, column=2)
pass_word=StringVar()
btn2=Entry(window, textvariable=pass_word)
btn.grid_remove()    

btn2.grid(row=10, column=1)
btn2.grid_remove()
et0.grid_remove()

view_com()
window.mainloop()
