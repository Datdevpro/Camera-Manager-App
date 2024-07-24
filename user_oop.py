# import json 
# f = open('test.json')
# data = json.load(f)

# print(data['children'][0]['firstName'])
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
#import pandas as pd 
import shutil
import ast
import requests
import json
class User(tk.Tk):
    def __init__(self):
        super().__init__()
        # Setting the main window properties
        self.title("Quản lý nhân sự")
        self.geometry("500x650")
        self.font = ("Segoe UI", 11)
        # Creating the main frames
        #self.call_function_user()
        self.path = "C:/Users/WelcomeCamera/Welcome-Camera/DUT-Welcome_and_Management_System/Camera_AI_Control/data/training_data"

    def create_frames(self):
        # Left frame
        self.left_frame = ttk.Frame(self, width=600, height=500)
        #self.left_frame.grid(row=0, column=0, sticky="nswe")
        self.left_frame.pack(side='top', anchor='nw', padx=10)
        #self.left_frame.grid_propagate(False)
        #self.left_frame.grid_propagate(False)
        
        # # Separator
        # self.separator = ttk.Separator(self, orient='vertical')
        # self.separator.grid(row=0, column=1, sticky="ns")

        # # Right frame
        # self.right_frame = tk.LabelFrame(self, width=1000, height=600, relief=tk.SUNKEN)
        # self.right_frame.grid(row=0, column=2, sticky="nswe")
        # self.right_frame.grid_propagate(False)

        # # Configure grid weights
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(2, weight=30)
        # self.grid_rowconfigure(0, weight=1)
        
        ##### NOTES FRAME #######
        self.note_frame = ttk.Frame(self, width=600, height=150)
        self.note_frame.pack(side='left', padx=10, ipady=20)
    
    def left_content(self):
        ######### HO TEN ###########
        self.name = ttk.Label(self.left_frame, text="Tên nhân sự:",font=self.font)
        self.name.grid(row=0, column=0 ,padx=5, pady=30)
        self.name_entry = ttk.Entry(self.left_frame, font=self.font, width=30)
        self.name_entry.grid(row=0, column=1,padx=5,pady=30)
        
        ######## GIOI TINH ##########
        self.gender = ttk.Label(self.left_frame, text="Giới Tính:", font=self.font)
        self.gender.grid(row=1, column=0, padx=5, pady=10)
        self.gender_option = ttk.Combobox(self.left_frame, values=["Nam", "Nữ"], width=35)
        self.gender_option['state'] = 'readonly'
        self.gender_option.current()
        self.gender_option.grid(row=1, column=1, pady=10)
        self.gender_option.bind("<<ComboboxSelected>>", self.get_gender)
        

        ########## HOC HAM ########
        ####### CHUC VU ########## 
        self.hochamhocvi = ttk.Label(self.left_frame, text="Học hàm học vị  :",font=self.font)
        self.hochamhocvi.grid(row=2, column=0 ,padx=5, pady=30)
        self.hochamhocvi_entry = ttk.Entry(self.left_frame, font=self.font, width=30)
        self.hochamhocvi_entry.grid(row=2, column=1,padx=5,pady=30)



        ####### CHUC VU ########## 
        self.chucvu = ttk.Label(self.left_frame, text="Chức Vụ:",font=self.font)
        self.chucvu.grid(row=3, column=0 ,padx=5, pady=10)
        self.chucvu_entry = ttk.Entry(self.left_frame, font=self.font, width=30)
        self.chucvu_entry.grid(row=3, column=1,padx=5,pady=10)



        ############ DEPARTMENT ############
        self.position = ttk.Label(self.left_frame, text="Tên đơn vị:",font=self.font)
        self.position.grid(row=4, column=0 ,padx=5, pady=30)
        self.position_entry = ttk.Entry(self.left_frame, font=self.font, width=30)
        self.position_entry.grid(row=4, column=1,padx=5,pady=30)

        self.btn_add = ttk.Button(self.left_frame,
                                  text="Thêm",
                                  default='active',
                                  cursor='hand2',
                                  command=self.add
                                  )
        self.btn_add.grid(row=6, column=0, pady=20)

        self.btn_delete = ttk.Button(self.left_frame,
                                  text="Xóa",
                                  default='active',
                                  cursor='hand2',
                                  command=self.delete
                                  )
        self.btn_delete.grid(row=6, column=1, pady=20)

        self.nhanvien = ttk.Label(self.left_frame, text="Loại:", font=self.font)
        self.nhanvien.grid(row=5, column=0, padx=5, pady=10)
        self.nhanvien_option = ttk.Combobox(self.left_frame, values=[1, 0], width=35)
        self.nhanvien_option['state'] = 'readonly'
        self.nhanvien_option.current()
        self.nhanvien_option.grid(row=5, column=1, pady=10)
        self.nhanvien_option.bind("<<ComboboxSelected>>", self.get_gender)

        #############   GHI CHÚ   ###################
        self.note_title = tk.Label(self.note_frame, text="*****Lưu ý*****", font=("Segoe UI", 14, 'bold'))
        self.note_title.pack(anchor='nw', padx = 10)
        self.note_content = tk.Label(self.note_frame, text="-  Viết tên có dấu đầy đủ", font=("Segoe UI", 12, 'italic'))
        self.note_content.pack(anchor='nw', padx=10)
        # self.note_content1 = tk.Label(self.note_frame, text="-  Nhập tên viết liền không dấu không viết hoa", font=("Segoe UI", 12, 'italic'))
        # self.note_content1.pack(anchor='nw', padx=10)
        ##########################################

        # self.label_file = ttk.Label(self.left_frame, text="No file selected")
        # self.label_file.grid(row=4, column=0)

    def get_gender(self, event):
        return self.gender_option.get()
    # def get_hocvi(self, event):
    #     return self.hocvi_option.get()
    # def get_hocham(self, event):
    #     return self.hocham_option.get()

    #@staticmethod
    def add(self): # tạo folder

        add_response = requests.post(
            url='http://localhost:1234/add_new_personnel/',
            json={
                'id':'',
                'gioitinh':self.gender_option.get(),
                'hoten':self.name_entry.get(),
                'hochamhocvi':self.hochamhocvi_entry.get(),
                'chucvu':self.chucvu_entry.get(),
                'tendonvi':self.position_entry.get(),
                'nhanvien':self.nhanvien_option.get()
            }
        )

        mess = add_response.content
        dict_str = mess.decode("UTF-8")
        mess_dixt = ast.literal_eval(dict_str)
        print(mess_dixt['new_id'])

        # name_folder = f"{self.name_entry.get()}_{self.position_entry.get()}"
        name_folder = f"{mess_dixt['new_id']}"
        
        fullpath = os.path.join(self.path, name_folder)
        try:
            os.makedirs(fullpath)
            messagebox.showinfo("Thông báo" ,f"Tạo thư mục thành công !\nđường dẫn: {fullpath}")
        except FileExistsError:
            messagebox.showinfo('Thông báo' ,"Thư mục đã tồn tại !")
        except Exception as e:
            messagebox.showinfo("Thông báo", "Lỗi 404 !")
        #print(f'{self.name_entry.get()} - {self.gender_option.get()} - {self.hochamhocvi_entry.get()} - {self.chucvu_entry.get()} - {self.position_entry.get()} - {self.nhanvien_option.get()}')
        
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
        
    # def File_dialog(self):
        """This Function will open the file explorer and assign the chosen file path to label_file"""
        # filename = filedialog.askopenfilename(initialdir="/",
        #                                     title="Select A File",
        #                                     filetype=(("csv files", "*.csv"),("xlsx files", "*.xlsx"),("All Files", "*.*")))
        # self.label_file["text"] = filename
        # return None
    

    #     return None
    def call_function_user(self):
        self.create_frames()
        self.left_content()
if __name__ == "__main__":
    app = User()
    app.mainloop()
