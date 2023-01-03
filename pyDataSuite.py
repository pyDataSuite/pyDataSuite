import sys
import os
from pathlib import Path

f_dir = Path(__file__)
ttkdir = f_dir.parent/"ttkbootstrap-python3.6"
print(ttkdir)

sys.path.append(str(ttkdir))

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def buttonClick(butt: ttk.Button):
    butt.place(x=300, y=300)

root = ttk.Window(themename="superhero")

b1 = ttk.Button(root, text="Submit", bootstyle="success")
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Submit", bootstyle="info-outline", command=lambda: buttonClick(b2))
b2.place(x=0, y=0)

root.mainloop()

