# Img To ASCII
# Takes an image, gets brightness of each pixel, converts to ASCII accordingly
# Lightness can be measured in ASCII on a simple scale like: [char for char in ".,`\'\"/;[@#..."] density = brightness

# TODO:
#  Make TKInter selection menu:
#  start button
#  open folder
#  set destination
#  settings
#  finalize
#  documentation
#  exe

from select_file import select_file

import tkinter as tk
from tkinter import ttk


import subprocess as sp


def open_ascii_file():
    programName = "notepad.exe"
    fileName = "ascii.txt"
    sp.Popen([programName, fileName])


def toggle_inverse_shading():
    pass


def init_ASCII_TKInter():
    # TKInter settings
    root = tk.Tk()
    # root.geometry('680x340')
    # root.resizable(False, False)
    frame = tk.Frame(root)
    frame.pack()

    root.title('ASCII Converter')

    # Buttons
    select_button = tk.Button(
        root,
        text='Select file',
        compound=tk.LEFT,
        command=select_file,
        height=5,
        width=17,
    )

    open_button = tk.Button(
        root,
        text='Open ASCII',
        compound=tk.LEFT,
        command=open_ascii_file,
        height=5,
        width=17,
    )

    invert_button = tk.Button(
        root,
        text="Invert shading",
        command=toggle_inverse_shading(),
        height=5,
        width=17,
    )

    # Button style and init
    select_button.pack(side=tk.LEFT)
    open_button.pack(side=tk.LEFT)
    invert_button.pack()

    root.mainloop()



def main():
    init_ASCII_TKInter()
    print("Init complete")


if __name__ == "__main__":
    global ascii_object
    main()
