import tkinter as tk 
from tkinter import Label, Button, Frame 
from .statistic_canhan import Statistic_cn
from .statistic_donvi import Statistic_dv
from .statistic_occur import Statistic_xh

def tkcanhan():
    canhan = Statistic_cn()
    canhan.call_function_statistic_cn()
def tkdonvi():
    donvi = Statistic_dv()
    donvi.call_function_statistic_dv()
def tkxuathien():
    xuathien = Statistic_xh()
    xuathien.call_function_statistic_xh()
def option():
    root = tk.Tk()
    root.geometry("750x100")
    root.title("Chọn loại thống kê")
    font = ("Segoe UI", 11)


    canhan = Button(root,
                    text="Thống kê theo cá nhân", 
                    font=font,
                    padx=10, 
                    overrelief="raised", 
                    cursor="hand2", 
                    bd=3,
                    command=tkcanhan)
    donvi = Button(root,
                    text="Thống kê theo đơn vị", 
                    font=font,
                    padx=10, 
                    overrelief="raised", 
                    cursor="hand2", 
                    bd=3, 
                    command=tkdonvi)
    
    xuathien = Button(root,
                    text="Thống kê lượng người ra vào tòa nhà", 
                    font=font,
                    padx=10, 
                    overrelief="raised", 
                    cursor="hand2", 
                    bd=3, 
                    command=tkxuathien)
    
    canhan.pack(side='left' , padx=20)
    donvi.pack(side='left', padx=20)
    xuathien.pack(side='left', padx=20)

    root.mainloop()
#option()