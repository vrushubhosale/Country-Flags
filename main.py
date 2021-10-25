from tkinter import *

root = Tk()
root.title("TRY ERROR")
root.configure("royal blue")
root.geometry("600x400")

list_name = ["Mickey", "Elsa", "Anna" , "Donald"]
dict_student = {"name" : "Shinchan" ,
                "age" : "5" }
try:
    print(list_name[5])
    
    print(dict_student["mom"])

except IndexError :
    messagebox.showinfo("Error", "This index value does not exist")
except KeyError :
    messagebox.showinfo("Error","This key value does not exist")
    
    root.mainloop()