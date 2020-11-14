from tkinter import *
from tkinter import messagebox
from backend import Database

database = Database()
# pyinstaller --windowed --onefile frontent.py
class Window(object):
    def __init__(self,window):
        self.window = window
        
        self.window.wm_title('BookStore')

        self.window.configure(bg='#add8e6')

        messagebox.showwarning("warning","Do not delete the 'books.db' file or data will be lost")
        self.window.resizable(width=False, height=False)
        self.et1=Label(window,text="Title:",bg='#a9eab9')
        self.et1.grid(row=0,column=0)
        self.title_text=StringVar()
        self.t1 = Entry(window, textvariable=self.title_text,bg ='#eadaa9')
        self.t1.grid(row=0,column=1)

        self.et2=Label(window,text="Author:",bg='#a9eab9')
        self.et2.grid(row=0,column=2)
        self.author_text=StringVar()
        self.t2 = Entry(window, textvariable=self.author_text,bg ='#eadaa9')
        self.t2.grid(row=0,column=3)

        self.et3=Label(window,text="Year:",bg='#a9eab9')
        self.et3.grid(row=1,column=0)
        self.year_text=StringVar()
        self.t3 = Entry(window, textvariable=self.year_text,bg ='#eadaa9')
        self.t3.grid(row=1,column=1)

        self.et4=Label(window,text="ISBN:",bg='#a9eab9')
        self.et4.grid(row=1,column=2)
        self.isbn_text=StringVar()
        self.t4 = Entry(window, textvariable=self.isbn_text,bg ='#eadaa9')
        self.t4.grid(row=1,column=3)

        self.list1=Listbox(window, height=8,width=35,bg ='#eadaa9')
        self.list1.grid(row=2,column=0,rowspan=8,columnspan=2)
    
        sb1=Scrollbar(window,bg ='#eadaa9')
        sb1.grid(row=2,column=2,rowspan=8)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        b1 = Button(window,text="View All",width=12, command=self.view_com,bg ='#a9eab9',activebackground='#add8e6')
        b1.grid(row=3, column=3)
        b2 = Button(window,text="Search Entry",width=12,command=self.search_com,bg ='#a9eab9',activebackground='#add8e6')
        b2.grid(row=4, column=3)
        b3 = Button(window,text="Add Entry",width=12,command=self.add_com,bg ='#a9eab9',activebackground='#add8e6')
        b3.grid(row=5, column=3)
        b4 = Button(window,text="Update Entry",width=12,command=self.update_com,bg ='#a9eab9',activebackground='#add8e6')
        b4.grid(row=6, column=3)
        b5 = Button(window,text="Delete",width=12,command=self.delete_com,bg ='#eaa9ba',activebackground='#add8e6')
        b5.grid(row=7, column=3)
        b6 = Button(window,text="Close",width=12,command=window.destroy,bg ='#eaa9ba',activebackground='#add8e6')
        b6.grid(row=8, column=3)
        self.view_com()

    def get_selected_row(self,event):
        if self.list1.curselection():
            index=self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)
            self.t1.delete(0,END)
            self.t1.insert(END,self.selected_tuple[1])
            self.t2.delete(0,END)
            self.t2.insert(END,self.selected_tuple[2])
            self.t3.delete(0,END)
            self.t3.insert(END,self.selected_tuple[3])
            self.t4.delete(0,END)
            self.t4.insert(END,self.selected_tuple[4])


    def view_com(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
    def search_com(self):
        self.list1.delete(0,END)
        for row in database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
            self.list1.insert(END,row)
    def add_com(self):
        database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))
        self.view_com()
    def delete_com(self):
        database.delete(self.selected_tuple[0])
        self.view_com()
    def update_com(self):
        database.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.view_com()

        
window=Tk()
Window(window)
window.mainloop()
