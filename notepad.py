from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
import os
from tkinter.messagebox import showinfo


def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents", ".txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        file1 = open(file, "r")
        text.insert(1.0, file1.read())
        file1.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfile(initialfile="untitled.txt", defaultextension=".txt",
                             filetypes=[("All Files", "*.*"), ("Text Documents", ".txt")])

        if file == "":
            file = None
        else:
            file1 = open(file, 'w')
            file1.write(text.get(1.0, END))
            file1.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        file1 = open(file, 'w')
        file1.write(text.get(1.0, END))
        file1.close()


def quitapp():
    root.destroy()


def cutfile():
    text.event_generate("<<Cut>>")


def copyfile():
    text.event_generate("<<Copy>>")


def pastefile():
    text.event_generate("<<Paste>>")


def about():
    showinfo("Notepad", "Notepad developed by Somdev Behera under PROGRAMMER FOUNDATION")


root = Tk()
root.iconbitmap(r'C:\Users\hello\Downloads\favicon_io\favicon.ico')
root.title("Notepad by Programmer Foundation")
root.geometry("600x600")

text = Text(root, bg="Wheat2", font="ariel")
text.pack(expand=True, fill=BOTH)
file = None

Menubar = Menu(root)
filemenu = Menu(Menubar, tearoff=0)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="open", command=openfile)
filemenu.add_command(label="save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="exit", command=quitapp)
Menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(Menubar, tearoff=0)
editmenu.add_command(label="cut", command=cutfile)
editmenu.add_command(label="copy", command=copyfile)
editmenu.add_command(label="paste", command=pastefile)

Menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(Menubar, tearoff=0)
helpmenu.add_command(label="About Notepad", command=about)

Menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=Menubar)

scroll = Scrollbar(text, width=10)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

root.mainloop()
