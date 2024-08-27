import tkinter as tk
from tkinter import Label, Entry, Button
from tkinter import ttk
import requests 
import json

class Statistic_cn(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1300x530")
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
        self.donvi = ["P.TCHC", "KHCN&HTQT", "KT&ĐBCL", "TTPC", "Tổ CNTT", "Viện KHCN&BKĐN"]  # list đơn vị
        self.combolabel = Label(self.main_frame, text='Chọn đơn vị: ', font= self.font)
        self.combolabel.grid(row=1, column=0, padx=20)
        self.combobox = ttk.Combobox(self.main_frame, values= self.donvi, width=30)
        self.combobox['state'] = 'readonly'
        self.combobox.current()  # Giá trị mặc định
        self.combobox.grid(row=1, column=1, pady=20)
        # Thêm sự kiện khi chọn một giá trị
        self.combobox.bind("<<ComboboxSelected>>",  self.on_select)


        ########### LOẠI THỐNG KÊ ###################
        self.types = ["Trễ giờ"]
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
                            text="Thống kê", 
                            padx=10, 
                            overrelief="raised", 
                            cursor="hand2", 
                            bd = 3,
                            state='active',
                            command=self.tk_canhan

                            )
        self.btn_canhan.grid(row=5, column=0, pady=30, padx=10, columnspan=2)



        ####################################################



        #############   GHI CHÚ   ###################
        self.note_title = Label(self.note_frame, text="*****Lưu ý*****", font=("Segoe UI", 14, 'bold'))
        self.note_title.pack(anchor='nw', padx = 10)
        self.note_content = Label(self.note_frame, text="-  Nhập tên viết liền không dấu không viết hoa", font=("Segoe UI", 12, 'italic'))
        self.note_content.pack(anchor='nw', padx=10)
        # self.note_content1 = Label(self.note_frame, text="-  Để trống ô TÊN nếu muốn thống kê theo đơn vị", font=("Segoe UI", 12, 'italic'))
        # self.note_content1.pack(anchor='nw', padx=10)
        self.note_content2 = Label(self.note_frame, text="-  Nhập định dạng ngày như ví dụ sau: 26_06_24", font=("Segoe UI", 12, 'italic'))
        self.note_content2.pack(anchor='nw', padx=10)
        ##########################################

    
    def right_frame_content(self):
        
        self.treescrolly = tk.Scrollbar(self.right_frame, orient="vertical") # command means update the yaxis view of the widget
        self.treescrollx = tk.Scrollbar(self.right_frame, orient="horizontal") # command means update the xaxis view of the widget

        self.treescrolly.pack(side='right', fill='y')
        #self.treescrollx.pack(side='bottom', fill=x)

        self.tree = ttk.Treeview(self.right_frame, columns=("Name", "Donvi", "Time"), show="headings", yscrollcommand=self.treescrolly.set)
        self.tree.heading("Name", text="Họ tên")
        self.tree.heading("Time", text="Thời gian")
        self.tree.heading("Donvi", text="Đơn vị")
        self.tree.column("Name", width=300, anchor='center')
        self.tree.column("Donvi", width=300, anchor='center')
        self.tree.column("Time", width=300, anchor='center')


        self.tree.pack(side='left', fill=tk.BOTH, expand=True)

        self.treescrolly.config(command=self.tree.yview)

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
    
    def tk_canhan(self):
        # if len(self.name_entry.get() != 0):
        self.cleartv()
        response = requests.get(
            url='http://localhost:1234/list_late/', # url de gui get request
            params={ # dict chua cac parameters cua request
                'query_type':'hoten',
                'query_val':[self.name_entry.get()], # lay so lan di tre cua id 2 va 13
                'start_date': self.sd_entry.get(), # ngay bat dau kiem tra 
                'end_date':  self.ed_entry.get() #'06_20_24' # ngay ket thuc kiem tra
            }
        )
        response.encoding = response.apparent_encoding
        list_di_tre = json.loads(response.json())
        for person in list_di_tre:
            #id_di_tre = person['id']
            hoten_di_tre = person['hoten']
            thoigian_di_tre= person['thoigian']
            donvi = person['tendonvi']
            self.tree.insert("", tk.END, values=(hoten_di_tre, donvi, thoigian_di_tre))
            #print(f'{id_di_tre}\t{hoten_di_tre} \t{thoigian_di_tre}')

    def call_function_statistic_cn(self):
        self.create_frames()
        self.left_frame_content()
        self.right_frame_content()

# if __name__ == "__main__":
#     # Pass the instance to the ButtonApp
#     statistic_app = Statistic_cn()
#     statistic_app.call_function_statistic()
#     statistic_app.mainloop()