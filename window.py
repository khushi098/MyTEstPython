import tkinter as tk
from tkinter import *
from tkinter import ttk


# 1. Create the Main window

win = tk.Tk() # Tk is a class of Tkinter
win.title('                                                                                     Visual Studio Code')
win.state('zoomed')
win.geometry('300x200')
style = ttk.Style()
style.theme_use('classic')
pw = ttk.PanedWindow(orient=tk.HORIZONTAL)

left_list = tk.Listbox(win)
left_list.pack(side=tk.LEFT)
pw.add(left_list)
right_list = tk.Listbox(win)
right_list.pack(side=tk.LEFT)
pw.add(right_list)

pw.pack(fill=tk.BOTH,expand=True)

try:
  win.iconbitmap('vsicon.ico')
except:
    pass

menubar = Menu() # Menu is a Class of Tkinter Library
file = Menu(menubar, tearoff = False)
edit = Menu(menubar, tearoff = False)
selection = Menu(menubar, tearoff = False)
view = Menu(menubar, tearoff = False)
go = Menu(menubar, tearoff = False)
run = Menu(menubar, tearoff = False)
terminal = Menu(menubar, tearoff = False)
help = Menu(menubar, tearoff = False)
'''
toolbar = Frame(win.master, bd=1, relief=RAISED)

win.img = Image.open("p.png")
eimg = ImageTk.PhotoImage(win.img)

exitButton = Button(toolbar, image=eimg, relief=FLAT, command=win.quit)
exitButton.image = eimg
exitButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)
#win.master.config(menu=menubar)
win.pack()'''












menubar.add_cascade(label='File',menu =file)
menubar.add_cascade(label='Edit',menu =edit)
menubar.add_cascade(label='Selection',menu =selection)
menubar.add_cascade(label='View',menu =view)
menubar.add_cascade(label='Go',menu =go)
menubar.add_cascade(label='Run',menu =run)
menubar.add_cascade(label='Terminal',menu =terminal)
menubar.add_cascade(label='Help',menu =help)

file.add_command(label="New File")
file.add_command(label="New Window")
file.add_command(label="New File...")
file.add_separator()
file.add_command(label="Open File")
file.add_command(label="Open File", accelerator="ctrl+O")
file.add_command(label="Open Folder", accelerator="altr+O")
file.add_command(label="Open workspace from File")
file.add_command(label="Open Recent")
file.add_separator()
file.add_command(label="Add Folder to Workspace")
file.add_command(label="Save Workspace as")
file.add_command(label="Duplicate Workspace")
file.add_separator()
file.add_command(label="Save", accelerator="ctrl+S")
file.add_command(label="Save as", accelerator="ctrl+shift+S")
file.add_command(label="Save all", accelerator="ctrl+K")
file.add_separator()
file.add_command(label="Auto Save")

sub_menu = Menu(file)
  #add submenu to preference
sub_menu.add_command(label="color theme",accelerator="ctrl+k+ctrl+t")
sub_menu.add_separator()
sub_menu.add_command(label="setting",accelerator="ctrl+st")
sub_menu.add_command(label="extension",accelerator="ctrl+x+ctrl+e") 

file.add_command(label="Preferences")
file.add_cascade(label="Preferances",menu=sub_menu)
sub_menu.config(bg="cyan",font=12)
file.add_separator()
file.add_command(label="Revert File")
file.add_command(label="Close Editor", accelerator="ctrl+F4")
file.add_command(label="Close Folder", accelerator="ctrl+F")
file.add_command(label="Close Window", accelerator="altr+F4")
file.add_separator()
file.add_command(label="Exit File",command=exit, accelerator="altr+X")



file.config(bg="pink",fg="black",activebackground="blue",activeforeground="red",activeborderwidth=2)
file.config(font="calbri")
win.config(menu = menubar)
#win.config(menu = submenu)
#2. Run the mainloop

#win.quit()
win.mainloop()