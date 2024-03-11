import tkinter as tk
class ToggleMenu(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=150, height=300, bg='green')
        self.button_callback = None
        # Creating UI
        self.create_text(75, 150, text='Some content', anchor=tk.CENTER, font='TimesNewRoman 16')
        self.button = tk.Button(self, text='Desired button', command=lambda: self.button_callback())
        self.create_window(75, 180, window=self.button)
    def set_button_callback(self, callback):
        self.button_callback = callback
    def ui_start(self):
        self.place(x=0, y=0)
        
    def ui_stop(self):
        self.place_forget()
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("375x660")
        self.root.resizable(height=True, width= True)
        self.root.title("Calculator")
        # Parameters
        self.is_toggle_active: bool = False
        # Create UI
        self.__ui_create()
    def ui_start(self):
        self.root.mainloop()
        
    def __ui_create(self):
        self.label = tk.Label(self.root, text='This is your calculator', font='TimesNewRoman 16')
        self.label.pack()
        # ... other widgets of your calculator are created and packed\grided here
        # ...
        # ...
        # Should be created exact in this order, othwerwise widgets above will overlap toggle menu and button
        self.toggle_menu = ToggleMenu(self.root)
        self.toggle_menu.set_button_callback(self.__toggle_callback)
        self.button_toggle = tk.Button(self.root, text='Button', command=self.__button_toggle_handler)
        self.button_toggle.place(x=0, y=0)
        
    def __button_toggle_handler(self):
        if self.is_toggle_active:
            self.toggle_menu.ui_stop()
            self.is_toggle_active = False
        else:
            self.toggle_menu.ui_start()
            self.is_toggle_active = True
            
    def __toggle_callback(self):
        print('We succesfully connected togle menu and main window')
        # Do some stuff here
            
 
if __name__.__eq__('__main__'):
    app = App()
    app.ui_start()
