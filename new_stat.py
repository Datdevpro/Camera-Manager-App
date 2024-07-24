# import json 
# f = open('test.json')
# data = json.load(f)

# print(data['children'][0]['firstName'])
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import os
import pandas as pd 
import shutil
class User(tk.Tk):
    def __init__(self):
        super().__init__()
        # Setting the main window properties
        self.title("Tkinter OOP Example")
        self.geometry("1400x600")
        self.font = ("Segoe UI", 11)
        # Creating the main frames
        #self.call_function_user()
        self.path = "D:/VScode/AI/tkin"
        
        
    def create_frames(self):
        # Left frame
        self.left_frame = ttk.Frame(self, width=700, height=600, relief=tk.SUNKEN)
        self.left_frame.grid(row=0, column=0, sticky="nswe")
        self.left_frame.grid_propagate(False)
        
        # Separator
        self.separator = ttk.Separator(self, orient='vertical')
        self.separator.grid(row=0, column=1, sticky="ns")

        # Right frame
        self.right_frame = tk.LabelFrame(self, width=700, height=600, relief=tk.SUNKEN)
        self.right_frame.grid(row=0, column=2, sticky="nswe")
        self.right_frame.grid_propagate(False)

        # Configure grid weights
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=10)
        self.grid_rowconfigure(0, weight=1)
    
    def left_content(self):
        self.name = ttk.Label(self.left_frame, text="Tên nhân sự:",font=self.font)
        self.name.grid(row=1, column=0 ,padx=5, pady=30)
        self.name_entry = ttk.Entry(self.left_frame, font=self.font, width=30)
        self.name_entry.grid(row=1, column=1,padx=5,pady=30)
        
        self.position = ttk.Label(self.left_frame, text="Tên đơn vị:",font=self.font)
        self.position.grid(row=2, column=0 ,padx=5, pady=30)
        self.position_entry = ttk.Entry(self.left_frame, font=self.font, width=30)
        self.position_entry.grid(row=2, column=1,padx=5,pady=30)

        self.btn_add = ttk.Button(self.left_frame,
                                  text="Thêm",
                                  default='active',
                                  cursor='hand2',
                                  command=self.add
                                  )
        self.btn_add.grid(row=3, column=0)

        self.btn_delete = ttk.Button(self.left_frame,
                                  text="Xóa",
                                  default='active',
                                  cursor='hand2',
                                  command=self.delete
                                  )
        self.btn_delete.grid(row=3, column=1)


        # self.label_file = ttk.Label(self.left_frame, text="No file selected")
        # self.label_file.grid(row=4, column=0)

    #@staticmetho
    def add(self): # tạo folder
        
        name_folder = f"{self.name_entry.get()}_{self.position_entry.get()}"
        
        fullpath = os.path.join(self.path, name_folder)
        try:
            os.makedirs(fullpath)
            messagebox.showinfo("Thông báo" ,f"Tạo thư mục thành công !\nđường dẫn: {fullpath}")
        except FileExistsError:
            messagebox.showinfo('Thông báo' ,"Thư mục đã tồn tại !")
        except Exception as e:
            messagebox.showinfo("Thông báo", "Lỗi 404 !")
        
    def delete(self):
        name_folder = f"{self.name_entry.get()}_{self.position_entry.get()}"
        fullpath = os.path.join(self.path, name_folder)
        try:
            if os.path.exists(fullpath):
                shutil.rmtree(fullpath)
                messagebox.showinfo("Thành công", f"Thư mục '{fullpath}' đã được xóa thành công.")
            else:
                messagebox.showerror("Lỗi", f"Thư mục '{fullpath}' không tồn tại.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi xóa thư mục: {e}")
        
    def File_dialog(self):
        """This Function will open the file explorer and assign the chosen file path to label_file"""
        filename = filedialog.askopenfilename(initialdir="/",
                                            title="Select A File",
                                            filetype=(("csv files", "*.csv"),("xlsx files", "*.xlsx"),("All Files", "*.*")))
        self.label_file["text"] = filename
        return None
    
    def Load_excel_data(self):
        """If the file selected is valid this will load the file into the Treeview"""
        file_path = self.label_file["text"]
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)

        except ValueError:
            tk.messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        self.clear_data()    
        self.tv["column"] = list(df.columns)
        self.tv["show"] = "headings"
        for column in self.tv["columns"]:
            self.tv.heading(column, text=column) # let the column heading = column name
            max_length = max(df[column].astype(str).map(len).max(), len(column))
            self.tv.column(column, width=max_length * 10)
        df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
        for row in df_rows:
            self.tv.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        return None


    
    def right_content(self):
        self.tv = ttk.Treeview(self.right_frame)
        self.tv.place(relheight=1, relwidth=1)

        self.treescrolly = tk.Scrollbar(self.right_frame, orient="vertical", command=self.tv.yview) # command means update the yaxis view of the widget
        self.treescrollx = tk.Scrollbar(self.right_frame, orient="horizontal", command=self.tv.xview) # command means update the xaxis view of the widget
        self.tv.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set) # assign the scrollbars to the Treeview Widget
        self.treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
        self.treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget
    
    def right_content2(self):
        self.tree = ttk.Treeview(self.right_frame, columns=("Name", "Date Time"), show="headings" )
        self.tree.heading("Name", text="Tên")
        self.tree.heading("Time", text="Thời gian")
        self.tree.heading("Age", text="Tuổi")
        self.tree.column("Name", width=200, anchor=tk.W)
        self.tree.column("Time", width=200, anchor=tk.W)
        self.tree.column("Age", width=100, anchor=tk.W)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.treescrolly = tk.Scrollbar(self.right_frame, orient="vertical", command=self.tree.yview) # command means update the yaxis view of the widget
        self.treescrollx = tk.Scrollbar(self.right_frame, orient="horizontal", command=self.tree.xview) # command means update the xaxis view of the widget
    
    def insert_data(self):
        pass


    def clear_data(self):
        self.tv.delete(*self.tv.get_children())
        return None


    def call_function_user(self):
        self.create_frames()
        self.left_content()
        self.right_content()
# if __name__ == "__main__":
#     app = User()
#     app.mainloop()
