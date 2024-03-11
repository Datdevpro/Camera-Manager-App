from tkinter import Tk, Label, Entry, Button, StringVar, ttk
import tkinter as tk
def user():
    root = tk.Tk()
    root.geometry("1000x350")
    root.title("User")
    def add_data():
        name = name_entry.get()
        position = position_entry.get()
        department = department_entry.get()  # Corrected line to get department value
        global n
        n=name
        global p
        p = position
        global d
        d=department
        lbd.config(text=f"{n} - {p} - {d}")
        get_data()
        # Clear entry fields for new input
        name_entry.delete(0, 'end')
        position_entry.delete(0, 'end')
        department_entry.delete(0, 'end')  # Clear department entry
            
        
    def get_data():
        #print(f'{n},{p},{d}')
        #return [n, p, d]  # get data
        return [n,p,d]
    def delelte_data():
        pass


    name_label = Label(root, text="Tên:",font=("Segoe UI", 10))
    name_label.grid(row=0, column=0 ,padx=15, pady=20)        
    position_label = Label(root, text="Chức Vụ:", font=("Segoe UI", 10))
    position_label.grid(row=1, column=0, padx=15, pady=10)
    department_label = Label(root, text="Vị Trí:", font=("Segoe UI", 10))
    department_label.grid(row=2, column=0,padx=15, pady=20)

    # create entry 
    name_entry = Entry(root, font=("Segoe UI", 10), width=30)
    name_entry.grid(row=0, column=1,padx=5, pady=10)

    position_entry = Entry(root,font=("Segoe UI", 10), width=30)
    position_entry.grid(row=1, column=1,padx=5, pady=10)

    department_entry = Entry(root, font=("Segoe UI", 10), width=30)
    department_entry.grid(row=2, column=1,padx=5, pady=10)

    add_button = Button(root, text="ADD", command=add_data)
    add_button.grid(row=3, column=0, pady=10, padx=30)

    delete_button = Button(root, text="DELETE", command=get_data)
    delete_button.grid(row=3, column=1, pady=10, padx=10)
    # Create a ttk.Treeview widget for the grid
    # data_grid = ttk.Treeview(root)
    # data_grid.grid(row=3, columnspan=3)
    lb = Label(root, text="User selected: ", font=("Segoe UI", 12))
    lb.grid(row = 4, column=0,pady=20, padx=15)
    lbd = Label(root, font=("Segoe UI", 11))
    lbd.grid(row=4, column=1)
    #lb.config(text=f"{n}, {p}, {d}")


    root.mainloop()
