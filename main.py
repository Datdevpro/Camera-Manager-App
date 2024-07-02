import tkinter as tk
from tkinter import Label, Button, Frame, W, E, S, N
from PIL import ImageTk, Image
from funcam import turn_cam
#from show_db import showdb
from statistic import statistic
from user import user_manage


# SET UP INITITAL ROOT
root = tk.Tk()
width = 1400
height = 720
root.geometry("%dx%d" % (width, height))
root.minsize(960, 540)
theme_dark = "#1b1e23"
bg_color = "#2c313c"
text_color = "#f5f6f9"
root['background']= bg_color
root.title("Ứng dụng quản lý")
root.resizable(False,False) # cho phép resize cửa sổ hay không
root.iconbitmap("building_ico.ico")


################################ end

# CREATE LEFT FRAME MENU
    # SET UP SOME PROPERTIES
min_w = 80 # Minimum width of the frame
max_w = 290 # Maximum width of the frame
cur_width = min_w # Increasing width of the frame
expanded = False # Check if it is completely exanded

#EXPAND MENU
def expand():
    global cur_width, expanded
    cur_width += 12 # Increase the width by 10
    rep = root.after(5,expand) # Repeat this func every 5 ms
    left_menu.config(width=cur_width) # Change the width to new increase width
    if cur_width >= max_w: # If width is greater than maximum width 
        expanded = True # Frame is expended
        root.after_cancel(rep) # Stop repeating the func
        fill()

def contract():  # co lại
    global cur_width, expanded
    cur_width -= 12 # Reduce the width by 10 
    rep = root.after(5,contract) # Call this func every 5 ms
    left_menu.config(width=cur_width) # Change the width to new reduced width
    if cur_width <= min_w: # If it is back to normal width
        expanded = False # Frame is not expanded
        root.after_cancel(rep) # Stop repeating the func
        fill()
def fill(): #show ra menu khi expand
    if expanded: # If the frame is exanded
        # Show a text, and remove the image
        viewcam_btn.config(text='   Xem Camera',image='',font=("Segoe UI", 17), fg="#ffffff", justify="center")
        showdtb_btn.config(text='   Thống kê dữ liệu',image='',font=("Segoe UI", 17), fg="#ffffff", justify="center")
        add_btn.config(text='  Thêm/xóa nhân sự',image='',font=("Segoe UI", 17), fg="#ffffff", justify="center")
        menu_lb.config(text='  Menu',image='',font=("Segoe UI", 20), fg="#ffffff", justify="center", bg=theme_dark)
    else:
        # Bring the image back
        viewcam_btn.config(image=funcam)
        showdtb_btn.config(image=showdtb,font=(0,15))
        add_btn.config(image=add,font=(0,15))
        menu_lb.config(image=menu, font=(0,15))

################ CREATE ICON FOR EACH BUTTON 
menu = ImageTk.PhotoImage(Image.open('menu.png').resize((70,70),Image.Resampling.LANCZOS))
funcam = ImageTk.PhotoImage(Image.open('cam.png').resize((80,80),Image.Resampling.LANCZOS))
showdtb = ImageTk.PhotoImage(Image.open('db.png').resize((60,60),Image.Resampling.LANCZOS))
add = ImageTk.PhotoImage(Image.open('user.png').resize((65,65),Image.Resampling.LANCZOS))
root.update()

# all_frame = tk.Frame(root, bg="white", width = 1400, height = 720)
# all_frame.grid()
left_menu = tk.Frame(root, bg=theme_dark, width=min_w, height=720, pady = 30)
#left_menu.place(x=0, y=0)
#left_menu.grid(row = 0, column = 0, padx = (6, 0), pady = (6, 6), sticky=tk.W)
left_menu.pack(side="left", expand=False, fill="y")
## CREATE BUTTON FOR 3 FUNCTION
viewcam_btn = Button(
        left_menu, 
        image = funcam, 
        bg = theme_dark, 
        relief='flat',
        activeforeground="green",
        cursor='hand2', 
        justify="center",
        command=turn_cam)

showdtb_btn = Button(
        left_menu, 
        image = showdtb, 
        bg = theme_dark, 
        relief='flat',
        activeforeground="green",
        cursor='hand2', 
        justify="center",
        command=statistic)
add_btn = Button(
        left_menu, 
        image = add, 
        bg = theme_dark, 
        relief='flat',
        activeforeground="green",
        cursor='hand2', 
        justify="center",
        command = user_manage)
menu_lb = Label(left_menu, image=menu)

menu_lb.grid(row = 0, column = 0, pady=40)
viewcam_btn.grid(row = 1, column = 0, pady=20)
showdtb_btn.grid(row = 2, column = 0, pady=50)
add_btn.grid(row = 3, column = 0, pady=20)

### SHOW OR HIDE THE MENU
left_menu.bind('<Enter>',lambda e: expand())
left_menu.bind('<Leave>',lambda e: contract())
left_menu.grid_propagate(False)
############# END

main_frame = Frame(root, bg=bg_color, width=900, height=720)
main_frame.pack(side="right", expand=False, fill="y")

top_lb = Label(main_frame, text='Ứng dụng quản lý hệ thống Welcome S-Building', width=130, font=("Segoe UI", 9), anchor=W, padx=30, bg="#3c4454", fg="#f5f6f9")
#top_lb.grid(row = 0, column = 1, sticky=tk.NW, pady = (6, 0))
top_lb.pack(side="top")

dev_lb = Label(main_frame, text='Phát triển bởi: LYDINC', width=130, font=("Segoe UI", 9), anchor=W, padx=30, bg="#3c4454", fg="#f5f6f9")
#dev_lb.grid(row = 0, column = 1, sticky=tk.SW, pady = (0, 6))
dev_lb.pack(side = "bottom")

dut = ImageTk.PhotoImage(Image.open('DUT.png').resize((250,250),Image.Resampling.LANCZOS))
dut_label = Label(main_frame, image=dut)
#dut_label.pack(side="top", expand=True, fill=None)
dut_label.place(relx=0.362, rely=0.25)
text_label = Label(main_frame, text="Trường Đại học Bách khoa - Đại học Đà Nẵng\nQuản lý hệ thống Welcome S-Building", font=("Segoe UI", 17), fg=text_color, bg=bg_color)
#text_label.pack(side="bottom",anchor="center")
text_label.place(relx=0.225, rely=0.62)












































root.mainloop()








