import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk



# 1. Create the Main window

win = tk.Tk() # Tk is a class of Tkinter
win.title('                                                                                                                                                                                                     \t \t\t\t\t\t\t\tVisual Studio Code')
win.state('zoomed')
win.geometry('400x200') #size of window
style = ttk.Style() # style for sash and handle 
style.theme_use('classic')
#for panewindow
pw = ttk.PanedWindow(orient=tk.HORIZONTAL)

left_list = tk.Listbox(win)
left_list.pack(side=tk.LEFT)
pw.add(left_list )
left_list.config(bg = "lightcyan4")

right_list = tk.Listbox(win)
right_list.pack(side=tk.LEFT)
pw.add(right_list)
right_list.config(bg = "lightpink")

pw.pack(fill=tk.BOTH,expand=True)
#for icon
try: #set icon for window
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
#for toolbar
toolbar = Frame (win.master, bd= 2, relief=RAISED)

win.img = Image.open("p.png")
eimg = ImageTk.PhotoImage(win.img)

exitButton = Button(toolbar, image=eimg, relief=FLAT, command=win.quit)
exitButton.image = eimg
exitButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=LEFT, fill=Y)
#toolbar.config(height = 30)
#toolbar.pack() '''


#to create scroll bar
sb = Scrollbar(win,bd ="20" , width ="25")
sb.pack(side = RIGHT,fill = Y)
#mylist=Listbox(win,xscrollcommand=sb.set)
#for line in range(100): 
    #mylist.insert(END,"khushi jain")
#mylist.pack(side = LEFT, fill = BOTH)
#sb.config(command=mylist.xview)



#create menu
menubar.add_cascade(label='File',menu =file)
menubar.add_cascade(label='Edit',menu =edit)
menubar.add_cascade(label='Selection',menu =selection)
menubar.add_cascade(label='View',menu =view)
menubar.add_cascade(label='Go',menu =go)
menubar.add_cascade(label='Run',menu =run)
menubar.add_cascade(label='Terminal',menu =terminal)
menubar.add_cascade(label='Help',menu =help)

#file menu

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
 
 #add submenu to preference
sub_menu = Menu(file)
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

#to set file menu theme
file.config(bg="pink",fg="black",activebackground="blue",activeforeground="red",activeborderwidth=2)
file.config(font="calbri")

win.config(menu = menubar)

win.mainloop()