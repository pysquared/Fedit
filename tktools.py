import tkinter as tk
from tkinter import filedialog as tkfd
import os

root_window = False
class Window:
    def __init__(self, title):
        global root_window
        self.title = title
        if root_window == False:
            self.win = tk.Tk()
        else:
            self.win = tk.Toplevel()
        self.win.title(self.title)
        
    def window_raw(self):
        return self.win


def verify_f_name(f_name):
    if f_name in [None, (), '']:
        return False
    return True

class TextEditor:
    def __init__(self, parent):
        self.parent = parent
        self.widget = tk.Text(self.parent)
        self.ftypes = [
            ('All files', '*'),
            ('Python code files', '*.py'), 
            ('Perl code files', '*.pl;*.pm'),  # semicolon trick
            ('Java code files', '*.java'), 
            ('C++ code files', '*.cpp;*.h'),   # semicolon trick
            ('Text files', '*.txt'),  
        ]
        self.initial_dir = os.path.expanduser('~')
    def widget_raw(self):
        return self.widget
    def pack(self, *args, **kwargs):
        self.widget.pack(kwargs)
    def grid(self, *args, **kwargs):
        self.widget.grid(kwargs)
    def clear_text(self, *args, **kwargs):
        self.widget.delete(*args, **kwargs)
    def set_text(self, text, *args, **kwargs):
        self.clear_text(0.0)
        self.widget.insert(0.0, text, args, kwargs)
    def get_text(self, *args, **kwargs):
        text = self.widget.get(*args, **kwargs)
        return text
    def open_file(self, *args, **kwargs):
        #args and kwargs to this function are thrown away
        global initial_dir
        f_name = tkfd.askopenfilename(filetypes=self.ftypes, initialdir=self.initial_dir)
        if not verify_f_name(f_name):
            return
        print('Opening', f_name)
        self.initial_dir = os.path.dirname(f_name)
        f_text = open(f_name, 'r').read()
        self.set_text(text=f_text)
    def save_file(self, *args, **kwargs):
        #args and kwargs to this function are thrown away
        global initial_dir
        f_name = tkfd.asksaveasfilename(filetypes=self.ftypes, initialdir=self.initial_dir)
        if not verify_f_name(f_name):
            return
        print('Saving', f_name)
        self.initial_dir = os.path.dirname(f_name)
        text = self.get_text(0.0)
        f_obj = open(f_name, 'w')
        f_obj.write(text)
        f_obj.close()

class MenuBar:
    def __init__(self, parent):
        self.parent = parent
        self.buttons = {}
    def add_button(self, button_name, command, text):
        button = tk.Button(self.parent, text=text, command=command)
        self.buttons[button_name] = {'cmd': command, 'text': text, 'raw': button}
    def pack_button(self, button_name, *args, **kwargs):
        self.buttons[button_name]['raw'].pack(args, kwargs)
    def grid_button(self, button_name, *args, **kwargs):
        self.buttons[button_name]['raw'].grid(kwargs)
    def raw_button(self, button_name):
        return self.buttons[button_name]['raw']

        
if __name__=='__main__':
    print('Run main.py instead of this!')