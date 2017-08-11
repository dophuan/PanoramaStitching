from Browse import *
from Tkinter import *
from stich import *

PATH=""
master = Tk()

def LoadImage():
    global PATH
    path=OpenDialog()
    PATH=path
    Label(master, text=PATH).grid(row=0, column=1)

def ShowImage():
    ListImage = []

    ListImage=LoadFileinDialog(PATH)
    stich(ListImage)


def GUILoad():

    Label(master, text="Path to Image").grid(row=0)
    Button(master, text='Browse', command=LoadImage).grid(row=3, column=1, sticky=W, pady=4)
    Button(master, text='Show Panorama', command=ShowImage).grid(row=3, column=2, sticky=W, pady=4)
    Button(master, text='Quit', command=master.quit).grid(row=3, column=3, sticky=W, pady=4)

    mainloop()

if __name__=='__main__':
    GUILoad()

