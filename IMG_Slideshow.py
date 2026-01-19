from itertools import cycle
from PIL import Image,ImageTk
import tkinter as tk
import time

root=tk.Tk()
root.title("Image SlideShower")
#list of image paths
image_paths=[
    r'c:\Users\Affan laptop\OneDrive\Pictures\Camera Roll\img1.jpg',
    r'c:\Users\Affan laptop\OneDrive\Pictures\Camera Roll\img2.jpg',
    r'c:\Users\Affan laptop\OneDrive\Pictures\Camera Roll\img3.jpg',
    r'c:\Users\Affan laptop\OneDrive\Pictures\Camera Roll\img4.jpg',
    r'c:\Users\Affan laptop\OneDrive\Pictures\Camera Roll\img5.jpg',
    r'c:\Users\Affan laptop\OneDrive\Pictures\Camera Roll\img6.jpg',
    r'c:\Users\Affan laptop\OneDrive\Pictures\Camera Roll\img7.jpg'
]

#Resize all images to 1080x1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
#image to photo image object
photo_images=[ImageTk.PhotoImage(image) for image in images]
#label is a graphic element that helps to display images from text
#module of tkinter
label=tk.Label(root)
label.pack()

#config element helps to change attributes of label
def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)      #3sec pause

#cycle() helps to iterate list of images in infinite loop
#function of itertools

slideshow=cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button=tk.Button(root,text="Play SlideShow",command=start_slideshow)
play_button.pack()

root.mainloop()