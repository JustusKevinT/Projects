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
root.title("Website blocker")
Label(root,text='Website blocker',font='arial 20 bold').pack()
ip = '127.0.0.1'
Label(root,text='Enter Website :',font='arial 13 bold').place(x=5,y=60)
website = Text(root,font='arial 10',height='2',width='40')
website.place(x=140,y=60)

def Blocker():
    websiteList = website.get(1.0,END)
    blocked_website_list = list(websiteList.split(","))

    with open (path,'r+') as host_file:
        file_content = host_file.read()
        for web in blocked_website_list:
            if web in file_content:
                showinfo('Website already blocked',message='The entered website(s) are already blocked ')
                pass
            else:
                host_file.write(ip+ " " + web + '\n')
                showinfo('Website blocked',message='The entered website(s) are blocked successfully')

block=Button(root,text='Block',font='arial 12 bold',pady=5,command=Blocker,width=6,bg='#5DADE2',activebackground = 'sky blue')
block.place(x=230,y=150)

def runapp(path):
    root.mainloop()

if __name__ == '__main__':
    path = hostfilePath()
    runapp(path)
