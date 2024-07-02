
# submit_button = ttk.Button(left_frame, text="Submit", command=process_input)
# submit_button.pack(pady=5)

# Add output widgets to the right frame
# output_label = ttk.Label(right_frame, text="Output will be displayed here")
# output_label.pack(pady=5)
# late_decision = False
# def lateon():
#     if latebool.get()==1 & onbool.get()==0:
#         late_decision=True
#         print("trễ")
#     elif latebool.get()==0 & onbool.get()==0:
#         pass 
#     elif latebool.get()==1 & onbool.get()==1:
#         pass
#     #return late_decision

def statistic():


    import tkinter as tk
    from tkinter import Label, Entry, Button
    from tkinter import ttk

    # Function to handle user input and display output
    # def process_input():
    #     user_input = entry.get()
    #     output_label.config(text=f"Output: {user_input}")



        #return var.get()
    # Create the main application window
    root = tk.Tk()
    root.title("Thống kê nhân sự")
    root.geometry("650x550")
    font =("Segoe UI", 11)

    ####### INIT #####################
    heading = Label(root, text="Điền các trường thông tin muốn thống kê", font=("Segoe UI", 14))
    heading.pack(pady=10)
    inputframe = tk.Frame(root,width=600, height=480)
    inputframe.pack(anchor='nw')



    ########## CÁ NHÂN #############
    name = Label(inputframe, text="Tên nhân sự:",font=font)
    name.grid(row=0, column=0 ,padx=5, pady=20)
    name_entry = Entry(inputframe, font=("Segoe UI", 10), width=30, bd=3)
    name_entry.grid(row=0, column=1,padx=5,pady=20)  
    ##############################




    ######### CHỌN ĐƠN VỊ #################
    def on_select(event):
        print(f"You selected: {combobox.get()}")
        #combobox.configure(background='white')
    donvi = ["Option 1", "Option 2", "Option 3"]  # list đơn vị
    combolabel = Label(inputframe, text='Chọn đơn vị: ', font=font)
    combolabel.grid(row=2, column=0, padx=10)
    combobox = ttk.Combobox(inputframe, values=donvi, width=30)
    combobox['state'] = 'readonly'
    combobox.current()  # Giá trị mặc định
    combobox.grid(row=2, column=1)
    # Thêm sự kiện khi chọn một giá trị
    combobox.bind("<<ComboboxSelected>>", on_select)
    #########################################





    ######### TICK BOX OPTION ###############
    def show_status():
        print(f"Checkbox is {'checked' if var.get() else 'unchecked'}")
        late_bool = True if var.get() else False 
        print(late_bool)
    var = tk.IntVar()
    global late_bool
    late_bool = False
    late = tk.Checkbutton(inputframe, text='Đi trễ', variable=var, font=font, command=show_status)
    late.grid(row=0, column=2, padx=20, pady=10)
    ################################





    # ontime = tk.Checkbutton(inputframe, text='đúng giờ', variable=onbool, font=font, command=lateon)
    # ontime.grid(row=1, column=1, padx=10, pady=10)

    ################## CHỌN NGÀY #################
    startdate = Label(inputframe, text="Từ ngày: ", font=font)
    startdate.grid(row=3, column=0, padx=20, pady=20)
    sd_entry = Entry(inputframe, font=font, width=20, bd=3)
    sd_entry.grid(row=3, column=1)
    enddate = Label(inputframe, text="Đến ngày: ", font=font)
    enddate.grid(row=4, column=0)
    ed_entry = Entry(inputframe, font=font, width=20, bd=3)
    ed_entry.grid(row=4, column=1)
    ##########################################



    ############# BUTTON #############
    btn_canhan = Button(inputframe,
                        text="Thống kê theo cá nhân", 
                        padx=10, 
                        overrelief="raised", 
                        cursor="hand2", 
                        bd = 3)
    btn_canhan.grid(row=6, column=0, pady=40, padx=20)

    btn_donvi = Button(inputframe, 
                    text="Thống kê theo đơn vị", 
                        padx=10, 
                        overrelief="raised", 
                        cursor="hand2", 
                        bd=3)
    btn_donvi.grid(row=6, column=1)



    ############# GHI CHÚ ###################
    note_frame = tk.Frame(root, width=400, height=100)
    note_frame.pack(anchor = 'sw', side='bottom')
    note_title = Label(note_frame, text="*****Lưu ý*****", font=("Segoe UI", 14, 'bold'))
    note_title.pack(anchor='nw', padx = 10)
    note_content = Label(note_frame, text="-  Để trống ô ĐI TRỄ nếu muốn thống kê người đi đúng giờ", font=("Segoe UI", 12, 'italic'))
    note_content.pack(anchor='nw', padx=10)
    note_content1 = Label(note_frame, text="-  Để trống ô TÊN nếu muốn thống kê theo đơn vị và ngược lại", font=("Segoe UI", 12, 'italic'))
    note_content1.pack(anchor='nw', padx=10)
    note_content2 = Label(note_frame, text="-  Nhập định dạng ngày như ví dụ sau: 26_06_2024", font=("Segoe UI", 12, 'italic'))
    note_content2.pack(anchor='nw', padx=10)
    ##########################################






    # Run the application
    root.mainloop()
