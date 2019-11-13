##########################################
#  Description: This script display an image a background and displays
#               othere images as slides on top of the image in background.
#               This would be a good script for having a themed image in the
#               background and display your pictures on top.
##########################################  
import tkinter as tk 
from PIL import Image, ImageTk
import glob

class App(tk.Tk):
    def __init__(self, image_files, sx, sy, delay):
        tk.Tk.__init__(self)
        self.overrideredirect(1) 
        # Here the values '10' as the x and y co-ordinates where the background image would start from on the screen.
        self.geometry("%dx%d+10+10" % (sx, sy)) 
        self.delay = delay
        self.pictures = []
        self.track_img_ndex = 0
        for img in image_files:
            self.pictures.append(img)
        self.picture_display = tk.Label(self)
        self.picture_display.pack(expand=True, fill="both")            
        print("Initalized")
                
    def show_slides(self):
        global bg_img
        if self.track_img_ndex < len(self.pictures):
            original_image = Image.open(self.pictures[self.track_img_ndex])
            self.track_img_ndex +=1    
            resized = original_image.resize((500, 500),Image.ANTIALIAS)
            bg_img.paste(resized, (20, 60))
            new_img = ImageTk.PhotoImage(bg_img)
            self.picture_display.config(image=new_img)
            self.picture_display.image = new_img
            self.after(self.delay, self.show_slides)
        else:
            print("End of list!")
            self.track_img_ndex = 0
            app.show_slides()

def middle_click(event):
    exit()
            

# Adjust the value of delay between display of images.
delay = 1500
# The value of sx and sx determine the size of screen to be used to place the background image.
sx = 1200
sy = 600

# path to list of images to be displayed on the background image
path = "C:\\Users\\shullur\\Pictures\\images\\*.jpg"

bg_img = Image.open("C:\\Users\\shullur\\Pictures\\Diwali.jpg").convert("RGBA")
# Uncomment the following two lines to change the size of background image
#size = (2030,1354)
#bg_img = bg_img.resize(size,Image.ANTIALIAS)

# declare a list to hold the images
image_files = []
for file in glob.glob(path):
    image_files.append(file)
    
app = App(image_files, sx, sy, delay)
app.bind("<Button-2>", middle_click)
app.show_slides()
app.mainloop()
