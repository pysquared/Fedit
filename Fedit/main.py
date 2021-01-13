#!/usr/bin/python3

import tktools
from tktools import tk

version = '0.0.0.1'

print('Starting Fedit '+version)

root = tktools.Window('Fedit ('+str(version)+')').window_raw()

frame_maintextedit = tk.Frame(root)

widget_maintextedit = tktools.TextEditor(frame_maintextedit).widget_raw()
widget_maintextedit.pack(expand=1, fill='both')

frame_maintextedit.pack(expand=1, fill='both')

root.mainloop()
print('Exiting')