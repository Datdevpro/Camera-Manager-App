import tkinter as tk
from tkinter import Label, Entry, Button
from tkinter import ttk

class Statistic(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1400x610")
        self.title("Thống kê nhân sự")
        self.font = ("Segoe UI", 11)
        #self.call()

    def create_frames(self):

        #### left frame
        self.left_frame = tk.Frame(self, width=700, height=650, relief=tk.SUNKEN)
        self.left_frame.grid(row=0, column=0, sticky="nswe", pady=5)
        self.left_frame.grid_propagate(False)
        
        #### separator
        self.separator = ttk.Separator(self, orient='vertical')
        self.separator.grid(row=0, column=1, sticky="ns")
        self.separator.grid_propagate(False)

        #### right frame 
        self.right_frame = tk.LabelFrame(self, width=900, height=650, relief=tk.SUNKEN)
        self.right_frame.grid(row=0, column=2, sticky="nswe", pady=5)
        self.right_frame.grid_propagate(False)

        ###### SUB FRAMES  ######
        self.main_frame = ttk.Frame(self.left_frame, width=700, height=480)
        self.main_frame.pack(anchor='nw', pady=20)

        self.note_frame = tk.Frame(self.left_frame, width=700, height=170)
        self.note_frame.pack(side='bottom' ,anchor='sw')

        # self.output_frame = tk.LabelFrame(self.right_frame, width=800, height=650, relief=tk.SUNKEN)
        # self.output_frame.grid(row=0, column=0, sticky='nswe')

    def left_frame_content(self):

        ##### name ####
        self.name = Label(self.main_frame, text="Tên nhân sự:",font=self.font)
        self.name.grid(row=0, column=0 ,padx=5, pady=20)
        self.name_entry = Entry(self.main_frame, font=("Segoe UI", 10), width=30, bd=3)
        self.name_entry.grid(row=0, column=1,padx=5,pady=20)  


        ############### CHỌN ĐƠN VỊ ########################
        self.donvi = ["Option 1", "Option 2", "Option 3"]  # list đơn vị
        self.combolabel = Label(self.main_frame, text='Chọn đơn vị: ', font= self.font)
        self.combolabel.grid(row=1, column=0, padx=20)
        self.combobox = ttk.Combobox(self.main_frame, values= self.donvi, width=30)
        self.combobox['state'] = 'readonly'
        self.combobox.current()  # Giá trị mặc định
        self.combobox.grid(row=1, column=1, pady=20)
        # Thêm sự kiện khi chọn một giá trị
        self.combobox.bind("<<ComboboxSelected>>",  self.on_select)


        ########### LOẠI THỐNG KÊ ###################
        self.types = ["Trễ giờ", "Đúng Giờ"]
        self.thongke_label = Label(self.main_frame, text="Chọn loại thống kê: ", font=self.font)
        self.thongke_label.grid(row=2, column=0, pady=10)
        self.thongke_cbb = ttk.Combobox(self.main_frame, values=self.types, width=30)
        self.thongke_cbb['state'] = 'readonly'
        self.thongke_cbb.current()
        self.thongke_cbb.grid(row=2, column=1, pady=10)
        self.thongke_cbb.bind("<<ComboboxSelected>>", self.late_on)
        ########################################


        ################## CHỌN NGÀY #################
        self.startdate = Label(self.main_frame, text="Từ ngày: ", font= self.font)
        self.startdate.grid(row=3, column=0, padx=20, pady=15)
        self.sd_entry = Entry(self.main_frame, font=self.font, width=25, bd=3)
        self.sd_entry.grid(row=3, column=1, pady=15)
        self.enddate = Label(self.main_frame, text="Đến ngày: ", font=self.font)
        self.enddate.grid(row=4, column=0, pady=20)
        self.ed_entry = Entry(self.main_frame, font=self.font, width=25, bd=3)
        self.ed_entry.grid(row=4, column=1, pady=20)
        ##########################################


        ############# BUTTON #############
        self.btn_canhan = Button(self.main_frame,
                            text="Thống kê theo cá nhân", 
                            padx=10, 
                            overrelief="raised", 
                            cursor="hand2", 
                            bd = 3,
                            state='active',
                            command=self.add_newdata

                            )
        self.btn_canhan.grid(row=5, column=0, pady=30, padx=10)

        self.btn_donvi = Button(self.main_frame, 
                            text="Thống kê theo đơn vị", 
                            padx=10, 
                            overrelief="raised", 
                            cursor="hand2", 
                            bd=3)
        self.btn_donvi.grid(row=5, column=1, pady=30)

        ####################################################



        #############   GHI CHÚ   ###################
        self.note_title = Label(self.note_frame, text="*****Lưu ý*****", font=("Segoe UI", 14, 'bold'))
        self.note_title.pack(anchor='nw', padx = 10)
        self.note_content = Label(self.note_frame, text="-  Nhập tên viết liền không dấu không viết hoa", font=("Segoe UI", 12, 'italic'))
        self.note_content.pack(anchor='nw', padx=10)
        self.note_content1 = Label(self.note_frame, text="-  Để trống ô TÊN nếu muốn thống kê theo đơn vị", font=("Segoe UI", 12, 'italic'))
        self.note_content1.pack(anchor='nw', padx=10)
        self.note_content2 = Label(self.note_frame, text="-  Nhập định dạng ngày như ví dụ sau: 26_06_2024", font=("Segoe UI", 12, 'italic'))
        self.note_content2.pack(anchor='nw', padx=10)
        ##########################################

    
    def right_frame_content(self):
        
        self.tree = ttk.Treeview(self.right_frame, columns=("Name", "Time"), show="headings" )
        self.tree.heading("Name", text="Họ Tên")
        self.tree.heading("Time", text="Thời gian")
        self.tree.column("Name", width=450, anchor='center')
        self.tree.column("Time", width=450, anchor='center')


        self.tree.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.treescrolly = tk.Scrollbar(self.right_frame, orient="vertical", command=self.tree.yview) # command means update the yaxis view of the widget
        self.treescrollx = tk.Scrollbar(self.right_frame, orient="horizontal", command=self.tree.xview) # command means update the xaxis view of the widget

    def on_select(self, event):
        print(f"You selected: {self.combobox.get()}")

    def late_on(self, event):
        print(f"You selected: {self.thongke_cbb.get()}")
        print(self.types.index(self.thongke_cbb.get()))

    def cleartv(self):
        # self.tree.delete(*self.tree.get_children())
        # return None
        for item in self.tree.get_children():
            self.tree.delete(item)
    
    def add_newdata(self):
        self.cleartv()
        new_data = [("Tom", "1:00 PM"), ("Jerry", "2:00 PM"), ("Spike", "3:00 PM")]
        for name, time in new_data:
            self.tree.insert("", tk.END, values=(name, time))

    def call_function_statistic(self):
        self.create_frames()
        self.left_frame_content()
        self.right_frame_content()

if __name__ == "__main__":
    # Pass the instance to the ButtonApp
    statistic_app = Statistic()

    statistic_app.mainloop()