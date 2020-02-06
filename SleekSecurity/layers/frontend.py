from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import os 
import sys
import subprocess
root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
root.configure(bg="tomato2")
lab = Label(root , text ='FSociety' )
lab.pack()
sub = Toplevel(root)
sub.title("UFW Status")
sub.geometry("600x300")
bot = Button(sub , text = "Show Status" , command = subprocess.call(["/home/fsociety/Desktop/Sleek/level0/ufwstatus.sh"]))
bot.pack(side = LEFT , pady = 10 )
def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Shell Files', '*.sh')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
btn = Button(root, text ='Open File', command = lambda:open_file())
btn.pack(side = TOP, pady = 10)
btn1 = Button(root , text = 'Exit' , command = root.destroy)
btn1.pack(side = BOTTOM , pady = 10)
btn2 = Button(root , text = 'Features Yet To Be Added' , command= "New Features Coming")
btn2.pack(side = BOTTOM , pady = 10)
mainloop()
