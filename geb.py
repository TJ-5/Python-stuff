from PIL import Image
import time
import keyboard
from tkinter import *
import tkinter as tk 

root = tk.Tk()
root.title('Regel') 

def weiter():
   img = Image.open('XWord Rätsel.png')
   img.show()
   
   while True:
        try:
            if keyboard.is_pressed('q'):
                img = Image.open('Nele (1).png')
                img.show() 
                break
        except:
            break

 
label = tk.Label(root, text="Das Rätsel muss gelöst werden\nbevor das Geschenk geöffnet werden kann", font=('arial', 28)).pack()

Button = tk.Button(root, text="weiter",font=('arial', 28), command=weiter).pack()

root.mainloop()



