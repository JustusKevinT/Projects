from tkinter import *
import platform
from tkinter.messagebox import *

def hostfilePath():
    system_os = platform.system()
    if system_os == 'Linux':
        path = '/etc/host'
    elif  system_os == 'Windows':
        path = 'C:\Windows\System32\drivers\etc\hosts'
    else:
        showinfo('Unidentified Operating System', message = 'Operating System in this device cannot be recognized')
    return path

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Website unblocker")
Label(root,text='Website unblocker',font='arial 20 bold').pack()
ip = '127.0.0.1'
Label(root,text='Enter one website to unblock',font='arial 13 bold').place(x=140,y=60)
blocked_website = Text(root,font='arial 10',height='2',width='45')
blocked_website.place(x=100,y=100)

def Unblocker():
    unblock_website_temp = blocked_website.get(1.0,END)
    unblock_website = unblock_website_temp.split(",")
    for i in range(len(unblock_website)):
        unblock_website[i] = ip + " " + unblock_website[i]

    with open (path,'r+') as host_file:
        content = host_file.readlines()
        host_file.seek(0)
        if unblock_website[0] not in content:
            showinfo('Website not found',message='Website not yet blocked')
        else:
            for line in content:
                if not any(website in line for website in unblock_website):
                  host_file.write(line)
            host_file.truncate()
            showinfo('Website unblocked',message='Website has been unblocked successfully')

unblock=Button(root,text='Unblock',font='arial 12 bold',pady=5,command=Unblocker,width=6,bg='#5DADE2',activebackground = 'sky blue')
unblock.place(x=230,y=150)

def runapp(path):
    root.mainloop()

if __name__ == '__main__':
    path = hostfilePath()
    runapp(path)
