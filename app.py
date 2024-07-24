import tkinter as tk
from tkinter import Label, Button, Frame, W
from PIL import ImageTk, Image
from funcam import turn_cam
#from show_db import showdb
# from statistic import statistic
# from user import user_manage
from statistic_oop import Statistic
from user_oop import User


class App:
    def __init__(self, root):
        ###### INITIAL SOME PROPERTIES OF APP AND FRAMES
        self.root = root
        self.width = 1400
        self.height = 720
        self.root.geometry("%dx%d" % (self.width, self.height))
        self.root.minsize(960, 540)
        self.theme_dark = "#1b1e23"
        self.bg_color = "#2c313c"
        self.text_color = "#f5f6f9"
        self.root['background']= self.bg_color
        self.root.title("Ứng dụng quản lý")
        self.root.resizable(False,False) # cho phép resize cửa sổ hay không
        self.root.iconbitmap("building_ico.ico")
        self.expanded = False  # Check if it is completely exanded
        self.min_w = 90 # Minimum width of the frame
        self.max_w = 290 # Maximum width of the frame
        self.cur_width = self.min_w # Increasing width of the frame
        
        ###### CALL FUNCTION ##########
        self.left_frame()

        self.display_frame()
        
    # MAIN FUNCTION WITH FRAMES
    def left_frame(self):


        ################ CREATE ICON FOR EACH BUTTON 
        self.menu = ImageTk.PhotoImage(Image.open('menu.png').resize((70,70),Image.Resampling.LANCZOS))
        self.cam = ImageTk.PhotoImage(Image.open('cam.png').resize((80,80),Image.Resampling.LANCZOS))
        self.showdtb = ImageTk.PhotoImage(Image.open('db.png').resize((60,60),Image.Resampling.LANCZOS))
        self.add = ImageTk.PhotoImage(Image.open('user.png').resize((65,65),Image.Resampling.LANCZOS))
        #self.root.update()

        self.left_menu = tk.Frame(self.root, bg=self.theme_dark, width=self.min_w, height=720, pady = 30)
        self.left_menu.pack(side='left', expand=False, fill="y")

        ############ BUTTON ##################
        self.viewcam_btn = Button(
                self.left_menu, 
                image = self.cam, 
                bg = self.theme_dark, 
                relief='flat',
                activeforeground="green",
                cursor='hand2', 
                justify="center",
                command=turn_cam
            )

        self.showdtb_btn = Button(
                self.left_menu, 
                image = self.showdtb, 
                bg = self.theme_dark, 
                relief='flat',
                activeforeground="green",
                cursor='hand2', 
                justify="center",
                command=self.statistic
            )

        self.add_btn = Button(
                self.left_menu, 
                image = self.add, 
                bg = self.theme_dark, 
                relief='flat',
                activeforeground="green",
                cursor='hand2', 
                justify="center",
                command = self.user
                )
        #######################################

        ############## LAY OUT ###########################
        self.menu_lb = Label(self.left_menu, image=self.menu)

        self.menu_lb.grid(row = 0, column = 0, pady=40)
        self.viewcam_btn.grid(row = 1, column = 0, pady=20)
        self.showdtb_btn.grid(row = 2, column = 0, pady=50)
        self.add_btn.grid(row = 3, column = 0, pady=20)

        self.left_menu.bind('<Enter>',lambda e: self.expand())
        self.left_menu.bind('<Leave>',lambda e: self.contract())
        self.left_menu.grid_propagate(False)    
        ###################################################
    def display_frame(self):
        self.main_frame = Frame(self.root, bg=self.bg_color, width=900, height=720)
        self.main_frame.pack(side="right", expand=False, fill="y")

        self.top_lb = Label(self.main_frame, text='Ứng dụng quản lý hệ thống Welcome S-Building', width=130, font=("Segoe UI", 9), anchor=W, padx=30, bg="#3c4454", fg="#f5f6f9")
        #top_lb.grid(row = 0, column = 1, sticky=tk.NW, pady = (6, 0))
        self.top_lb.pack(side="top")

        self.dev_lb = Label(self.main_frame, text='Phát triển bởi: LYDINC', width=130, font=("Segoe UI", 9), anchor=W, padx=30, bg="#3c4454", fg="#f5f6f9")
        #dev_lb.grid(row = 0, column = 1, sticky=tk.SW, pady = (0, 6))
        self.dev_lb.pack(side = "bottom")

        self.dut = ImageTk.PhotoImage(Image.open('DUT.png').resize((250,250),Image.Resampling.LANCZOS))
        self.dut_label = Label(self.main_frame, image=self.dut)
        #dut_label.pack(side="top", expand=True, fill=None)
        self.dut_label.place(relx=0.362, rely=0.25)
        self.text_label = Label(self.main_frame, text="Trường Đại học Bách khoa - Đại học Đà Nẵng\nQuản lý hệ thống Welcome S-Building", font=("Segoe UI", 17), fg=self.text_color, bg=self.bg_color)
        #text_label.pack(side="bottom",anchor="center")
        self.text_label.place(relx=0.225, rely=0.62)
    ##########

    #  SUB FUNCTION
    def expand(self):
        self.cur_width += 12 # Increase the width by 10
        self.rep = self.root.after(5,self.expand) # Repeat this func every 5 ms
        self.left_menu.config(width=self.cur_width) # Change the width to new increase width
        if self.cur_width >= self.max_w: # If width is greater than maximum width 
            self.expanded = True # Frame is expended
            self.root.after_cancel(self.rep) # Stop repeating the func
            self.fill()

    def contract(self):
        #global cur_width, expanded
        self.cur_width -= 12 # Reduce the width by 10 
        self.rep = self.root.after(5,self.contract) # Call this func every 5 ms
        self.left_menu.config(width=self.cur_width) # Change the width to new reduced width
        if self.cur_width <= self.min_w: # If it is back to normal width
            self.expanded = False # Frame is not expanded
            self.root.after_cancel(self.rep) # Stop repeating the func
            self.fill()

    def fill(self):
        if self.expanded: # If the frame is exanded
        # Show a text, and remove the image
            self.viewcam_btn.config(text='   Xem Camera',image='',font=("Segoe UI", 17), fg="#ffffff", justify="center")
            self.showdtb_btn.config(text='   Thống kê dữ liệu',image='',font=("Segoe UI", 17), fg="#ffffff", justify="center")
            self.add_btn.config(text='  Thêm/xóa nhân sự',image='',font=("Segoe UI", 17), fg="#ffffff", justify="center")
            self.menu_lb.config(text='  Menu',image='',font=("Segoe UI", 20), fg="#ffffff", justify="center", bg=self.theme_dark)
        else:
            # Bring the image back
            self.viewcam_btn.config(image=self.cam)
            self.showdtb_btn.config(image=self.showdtb,font=(0,15))
            self.add_btn.config(image=self.add,font=(0,15))
            self.menu_lb.config(image=self.menu, font=(0,15))   
    ##########

    def user(self):
        user = User()
        user.call_function_user()
    def statistic(self):
        stat = Statistic()
        stat.call_function_statistic()



if __name__ == '__main__':
    root = tk.Tk()

    app = App(root)
    root.mainloop()
    
