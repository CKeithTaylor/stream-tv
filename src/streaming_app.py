from tkinter import *
from PIL import Image, ImageTk
import os
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def image_resize(file):
    img = Image.open(file)
    resized_img = img.resize((150, 150))
    logo = ImageTk.PhotoImage(resized_img)
    return logo


def btn_click(url):
    try:
        ### Kill all running processes of the desired browser.  Without this step, the full screen
        ### functionality may not work correctly
        subprocess.call("TASKKILL /f /IM CHROME.EXE")

        ### Set the path to the desired web browser and switches to enable full screen display ###
        chrome_path = """"C:/Program Files/Google/Chrome/Application/chrome.exe" --chrome-frame --kiosk"""

        ### Construct the full text of the command to be executed with the subprocess method ###
        command_text = f"{chrome_path} {url}"
        subprocess.Popen(command_text)

    except Exception as e:

        subprocess.call("TASKKILL /f /IM CHROME.EXE")


root = Tk()
root.attributes("-fullscreen", True)
root.configure(bg="#303134")
root.title("Streaming Services")

################################################################################
### The next several sections are just creating the images and corresponding ###
### buttons for all of the streaming services.  This is done in two steps:   ###
### 1. create the image in the correct format (png) and size (150x150)       ###
### 2. Build the button using that image and pass the correct URL            ###
################################################################################

### Disney+ ###
dis_logo = image_resize(file="static/images/disney+.png")
disney_btn = Button(
    root,
    image=dis_logo,
    border=0,
    bd=0,
    padx=10,
    pady=10,
    command=lambda: btn_click(url="www.disneyplus.com"),
)
disney_btn.place(x=50, y=50)

### Netflix ###
net_logo = image_resize(file="static/images/netflix.png")
netflix_btn = Button(
    root,
    image=net_logo,
    border=0,
    borderwidth=0,
    padx=10,
    pady=10,
    command=lambda: btn_click(url="www.netflix.com"),
)
netflix_btn.place(x=200, y=200)

### Amazon Prime Video ###
amazon_logo = image_resize(file="static/images/amazon.png")
amazon_btn = Button(
    root,
    image=amazon_logo,
    border=0,
    borderwidth=0,
    padx=10,
    pady=10,
    command=lambda: btn_click(url="www.amazon.com/gp/video/storefront"),
)
amazon_btn.place(x=500, y=150)
# ### ESPN+ ###
# net_logo = image_resize(file="static/images/netflix.png")
# netflix_btn = Button(
#     root,
#     image=net_logo,
#     border=0,
#     borderwidth=0,
#     padx=10,
#     pady=10,
#     command=lambda: btn_click(url="www.netflix.com"),
# )
# netflix_btn.grid(row=3, column=2)
# ### Tubi ###
# net_logo = image_resize(file="static/images/netflix.png")
# netflix_btn = Button(
#     root,
#     image=net_logo,
#     border=0,
#     borderwidth=0,
#     padx=10,
#     pady=10,
#     command=lambda: btn_click(url="www.netflix.com"),
# )
# netflix_btn.grid(row=3, column=2)
# ### CrunchyRoll ###
# net_logo = image_resize(file="static/images/netflix.png")
# netflix_btn = Button(
#     root,
#     image=net_logo,
#     border=0,
#     borderwidth=0,
#     padx=10,
#     pady=10,
#     command=lambda: btn_click(url="www.netflix.com"),
# )
# netflix_btn.grid(row=3, column=2)
# ### Hulu ###
# net_logo = image_resize(file="static/images/netflix.png")
# netflix_btn = Button(
#     root,
#     image=net_logo,
#     border=0,
#     borderwidth=0,
#     padx=10,
#     pady=10,
#     command=lambda: btn_click(url="www.netflix.com"),
# )
# netflix_btn.grid(row=4, column=2)
# ### HBO Max ###
# net_logo = image_resize(file="static/images/netflix.png")
# netflix_btn = Button(
#     root,
#     image=net_logo,
#     border=0,
#     borderwidth=0,
#     padx=10,
#     pady=10,
#     command=lambda: btn_click(url="www.netflix.com"),
# )
# netflix_btn.grid(row=4, column=2)
# ### Sling TV ###
# net_logo = image_resize(file="static/images/netflix.png")
# netflix_btn = Button(
#     root,
#     image=net_logo,
#     border=0,
#     borderwidth=0,
#     padx=10,
#     pady=10,
#     command=lambda: btn_click(url="www.netflix.com"),
# )
# netflix_btn.grid(row=4, column=2)
# ### Shudder ###
# net_logo = image_resize(file="static/images/netflix.png")
# netflix_btn = Button(
#     root,
#     image=net_logo,
#     border=0,
#     borderwidth=0,
#     padx=10,
#     pady=10,
#     command=lambda: btn_click(url="www.netflix.com"),
# )
# netflix_btn.grid(row=5, column=2)
# ### Crackle ###
# net_logo = image_resize(file="static/images/netflix.png")
# netflix_btn = Button(
#     root,
#     image=net_logo,
#     border=0,
#     command=lambda: btn_click(url="www.netflix.com"),
# )
# netflix_btn.grid(row=5, column=2)
root.mainloop()
