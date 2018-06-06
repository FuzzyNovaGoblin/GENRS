# Import everything from tkinter
from tkinter import filedialog
from tkinter import *

from GENRS import runprogram



def selectfilebuttpress():
    window.filename = filedialog.askopenfilename(initialdir="~", title="Select file")

def callrun():
    if window.filename != "":
        runprogram(window.filename, e1.get(), eord.get())
    # runprogram("/home/fuzzy/test/test", e1.get(), eord.get())

window = Tk()

window.filename = ""

l1 = Label(window, text="Key:")
l1.grid(row = 1, column=1)


e1 = Entry(window)
e1.grid(row = 1, column=3)

eord = StringVar()

rb1 = Radiobutton(window, text="Encrypt", variable=eord, value="e")
rb1.grid(row=4, column=1)
rb1.select()

rb2 = Radiobutton(window, text="Decrypt", variable=eord, value="d")
rb2.grid(row=4, column=3)



filebutt = Button(window, text="Select file", command=selectfilebuttpress)
filebutt.grid(row=5, column=2)

gobutt = Button(window, text="go", command=callrun)
gobutt.grid(row=6, column=2)


window.mainloop()