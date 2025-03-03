import tkinter as tk
from cProfile import label
from modulefinder import Module
def onButtonClick():
    name = entryName.get()
    labelTitle.config(text="ПРИВЕТ ХУЕСОС!!!!!")
mainWindow = tk.Tk()
mainWindow.geometry("900x600")
mainWindow.title("SOSAL???")
labelTitle = tk.Label(mainWindow,font="Arial 20",bg="beige",fg="darkgreen",
                      text="SOSAL?")
labelTitle.place(relx=0,rely=0.01,relwidth=1,relheight=0.05)

entryName=tk.Entry(mainWindow,font="Arial 20",bg="beige",fg="darkgreen")
entryName.place(relx=0,rely=0.08,relwidth=1,relheight=0.05)

button=tk.Button(mainWindow,font="Arial 20",bg="beige",fg="darkgreen",
                      text="YES")
button.place(relx=0,rely=0.92,relwidth=1,relheight=0.08)
button=tk.Button(mainWindow,font="Arial 20",bg="beige",fg="darkgreen",
                      text="OF COURSE",command=onButtonClick)
button.place(relx=0,rely=0.82,relwidth=1,relheight=0.08)

labelQuest=tk.Label(mainWindow,font="Arial 20",bg="beige",fg="darkgreen",
                      text="ТОЧНО SOSAL?")
labelQuest.place(relx=0.35,rely=0.2,relwidth=0.4,relheight=0.08)

radio1=tk.Radiobutton(mainWindow,font="Arial 20",bg="beige",fg="darkgreen",text="YES")
radio1.place(relx=0.3,rely=0.3,relwidth=0.2,relheight=0.08)

radio2=tk.Radiobutton(mainWindow,font="Arial 20",bg="beige",fg="darkgreen",text="OF COURSE")
radio2.place(relx=0.3,rely=0.4,relwidth=0.2,relheight=0.08)

mainWindow.mainloop()
