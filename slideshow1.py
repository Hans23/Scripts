##########################################
#  Description: This script display an image a background and displays
#               othere images as slides on top of the image in background.
#               This would be a good script for having a themed image in the
#               background and display your pictures on top.
##########################################

import tkinter as tk
from PIL import ImageTk, Image
import glob

path = "C:\\Users\\shullur\\Pictures\\images\\*.jpg"
idx = 0 

class App(tk.Tk):
    def __init__(self,delay):
        tk.Tk.__init__(self)       
        self.delay = delay
        self.panel1 = tk.Label(self)
        self.overrideredirect(1)
        self.panel1.pack(expand=True, fill="both")
        print("Initalized")
        
    def iterate(self):
        global idx 
        idx += 1
        if idx < len(images):
            self.show(idx)
        else:
            idx = 0
            self.show(idx)      
        return 
     
    def show(self,ind):
        global images
        fg_img = Image.open(images[ind]).convert("RGBA")
        p = fg_img.resize((550,500),Image.ANTIALIAS)
        bg_img.paste(p, (20, 40))
        tkimage = ImageTk.PhotoImage(bg_img)
        self.panel1.config(image=tkimage)
        self.panel1.image = tkimage
        self.after(self.delay,self.iterate)
  
def middle_click(event):
    exit()

delay = 2500

# Background image
bg_img = Image.open("C:\\Users\\shullur\\Pictures\\space.jpg").convert("RGBA")

images =[]
for img in glob.glob(path):
    img = img.replace("\\","\\\\") # to replace '\' with '\\' in the name of the file
    images.append(img)
    
window = App(delay)
window.bind("<Button-2>", middle_click)
window.show(idx)
window.mainloop()
