from pytube import YouTube
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x300")
root.title("YouTube Downloader") 

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")

    yt = YouTube(INPUT)

    stream = yt.streams.get_highest_resolution()
    stream.download()
    yt = YouTube(INPUT)
    
    root.quit()

inputtxt = Text(root, height = 10, width = 30, bg = "light cyan")

Display = Button(root, height = 2, width = 20, text = "download", command = lambda:Take_input())


inputtxt.pack()
Display.pack()
mainloop()


