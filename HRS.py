from Tkinter import *
import pypyodbc as pyodbc


def show_entry_fields():
   e = Entry(master)
   e.pack()
   e.focus_set()
   print("USERNAME", x)
   e1.delete(0,END)
def callback():
    print e.get()
def unlockhrs():
    cnxn = pyodbc.connect('Trusted_Connection=yes;DRIVER={SQL Server};SERVER=blabla;DATABASE=xxx;UID=domain1\xxx;PWD=xxx')
    username = e
    cursor = cnxn.cursor()
    cursor.execute("update tbl_UserActivity set UserBlock = 0 where UserName = %s, username")
    cursor.commit()
    cursor.execute("select * from tbl_UserActivity where UserName = %s, username")

master = Tk()
master.title("HRS UNLOCK")
master.resizable(False, False)
master.minsize(width=300, height=50)
master.maxsize(width=300, height=50)
Label(master, text="USERNAME").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)


Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Unlock', command=lambda: unlockhrs).grid(row=3, column=2, sticky=W, pady=4)

mainloop( )
