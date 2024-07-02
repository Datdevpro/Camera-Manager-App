#### create and named folder as the name entry

from tkinter import Tk, Label, Entry, Button, StringVar, ttk, messagebox
import tkinter as tk 
import os 
import shutil
 
def user_manage():
    root = tk.Tk()
    root.title("Thêm / Xóa nhân sự")
    root.geometry("650x550")
    font = ("Segoe UI", 11)

    # direction = Label(root, text="Thư mục mặc định là: D://VScode//AI//tkin//user.py", font=font)
    # direction.grid(row=0)
    heading = Label(root, text="Thêm / Xóa nhân sự", font=("Segoe UI", 14))
    heading.pack(pady=10)

    main_frame = tk.Frame(root,width=600, height=400)
    main_frame.pack(anchor='center')


    name = Label(main_frame, text="Tên nhân sự:",font=font)
    name.grid(row=1, column=0 ,padx=5, pady=30)
    name_entry = Entry(main_frame, font=font, width=30)
    name_entry.grid(row=1, column=1,padx=5,pady=30)

    position = Label(main_frame, text="Đơn vị:",font=font)
    position.grid(row=2, column=0 ,padx=5, pady=30)
    position_entry = Entry(main_frame, font=font, width=30)
    position_entry.grid(row=2, column=1,padx=5,pady=30)

    global path   # khai báo một đường dẫn cố định
    path = "D:/VScode/AI/tkin"
    def add(): # tạo folder
        name_folder = f"{name_entry.get()}_{position_entry.get()}"
        
        fullpath = os.path.join(path, name_folder)
        try:
            os.makedirs(fullpath)
            messagebox.showinfo("Thông báo" ,f"Tạo thư mục thành công !\nđường dẫn: {fullpath}")
        except FileExistsError:
            messagebox.showinfo('Thông báo' ,"Thư mục đã tồn tại !")
        except Exception as e:
            messagebox.showinfo("Thông báo", "Lỗi 404 !")

    def delete(): # xóa folder
        name_folder = f"{name_entry.get()}_{position_entry.get()}"
        fullpath = os.path.join(path, name_folder)
        try:
            if os.path.exists(fullpath):
                shutil.rmtree(fullpath)
                messagebox.showinfo("Thành công", f"Thư mục '{fullpath}' đã được xóa thành công.")
            else:
                messagebox.showerror("Lỗi", f"Thư mục '{fullpath}' không tồn tại.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi xóa thư mục: {e}")
        


    btn_them = Button(main_frame,
                        text="Thêm", 
                        padx=10, 
                        overrelief="raised", 
                        cursor="hand2", 
                        bd = 3,
                        command=add)
    btn_them.grid(row=3, column=0, pady=40, padx=30)

    btn_xoa = Button(main_frame,
                        text="Xóa", 
                        padx=10, 
                        overrelief="raised", 
                        cursor="hand2", 
                        bd = 3,
                        command=delete)
    btn_xoa.grid(row=3, column=1, pady=40, padx=30)

    ############### lưu ý ################
    note_frame = tk.Frame(root, width=400, height=100)
    note_frame.pack(anchor = 'sw', side='bottom')
    note_title = Label(note_frame, text="*****Lưu ý*****", font=("Segoe UI", 14, 'bold'))
    note_title.pack(anchor='nw', padx = 10)
    note_content = Label(note_frame, text="-  Tên nhân sự và đơn vị phải nhập không dấu và dính liền nhau", font=("Segoe UI", 12, 'italic'))
    note_content.pack(anchor='nw', padx=10)
    # note_content1 = Label(note_frame, text="-  Để trống ô TÊN nếu muốn thống kê theo đơn vị và ngược lại", font=("Segoe UI", 12, 'italic'))
    # note_content1.pack(anchor='nw', padx=10)
    # note_content2 = Label(note_frame, text="-  Nhập định dạng ngày như ví dụ sau: 26_06_2024", font=("Segoe UI", 12, 'italic'))
    # note_content2.pack(anchor='nw', padx=10)
    root.mainloop()