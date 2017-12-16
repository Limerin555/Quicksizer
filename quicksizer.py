import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageOps
from resizeimage import resizeimage

# GUI
window = Tk()
window.title("Quicksizer")
window.configure(bg = "#2E2E27")
window.resizable(width=False, height=False)
window.geometry('{}x{}'.format(800, 500))
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(8, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(6, weight=1)
current_dir = os.getcwd()

# Startup Info
messagebox.showinfo("Welcome to Quicksizer",
                  "This software was created to speed up your 4R image resizing process.\n"
                  "\n"
                  "You will be able to : \n"
                  "- Resize & crop your files into high quality 4R size (300 dpi)\n"
                  "- Save resized files to a new directory\n"
                  "\n"
                  "This software will only resize & crop JPEG files that are larger than 4R(1800px X 1200px),\n"
                  "so please make sure your file size is sufficient for this process.\n"
                  "\n"
                  "Quicksizer is still in development, future versions of it might be released."
                  )

def done_exporting():
    messagebox.showinfo("Files exported to Save Directory",
                      "Resizing & cropping process is done.\n"
                      )

# App Name
app_label = Label(window, text="Quicksizer App", fg = "white", bg = "#2E2E27", font = (None, 15, "bold"))
app_label.grid(row = 1, column = 3, padx = 5, pady = 5, ipady = 20, columnspan = 3, sticky = N)

# Input Title
input_dir_label = Label(window, text="Select a folder to resize", fg = "white", bg = "#2E2E27", font = ("Arial", 9))
input_dir_label.grid(row = 2, column = 3)


# Input Directory
def ask_for_input_path():
    global input_path
    input_path = filedialog.askdirectory(initialdir = current_dir, title = "Resize Directory")
    input_path = input_path + "/"
    input_path_name.delete(0, END)
    input_path_name.insert(0, input_path)
    return input_path


# Input Browse Button
input_path_name = Entry(window, width = 60 , bg = "white")
input_path_name.grid(row = 3, column = 3, padx = 10, pady = 10, ipady = 3)
browse_btn = Button(window, width = 10, text = "Browse", command = ask_for_input_path, fg = "white", font = ("Arial", 9, "bold"), bg = "#05AFF2")
browse_btn.grid(row = 3, column = 4)

# Save Title
save_dir_label = Label(window, text="Select a folder to save resized images", fg = "white", bg = "#2E2E27", font = ("Arial", 9))
save_dir_label.grid(row = 4, column = 3)


# Save Directory
def ask_for_save_path():
    global save_path
    save_path = filedialog.askdirectory(initialdir = current_dir, title = "Output Directory")
    save_path = str(save_path) + "/"
    save_path_name.delete(0, END)
    save_path_name.insert(0, save_path)
    return save_path


# Save Browse Button
save_path_name = Entry(window, width = 60 , bg = "white")
save_path_name.grid(row = 5, column = 3, padx = 10, pady = 10, ipady = 3)
browse_btn = Button(window, width = 10, text = "Browse", command = ask_for_save_path, fg = "white", font = ("Arial", 9, "bold"), bg = "#05AFF2")
browse_btn.grid(row = 5, column = 4)


# IMAGE RESIZE
def resize():
    # 4R
    landscape_4R = [1800, 1200] # pixels
    portrait_4R = [1200, 1800] # pixels
    hi_res = (300, 300) # dpi

    dirs = os.listdir(input_path)

    for item in dirs:
        if os.path.isfile(input_path + item):
            img = Image.open(input_path + item)
            ori, ext = os.path.splitext(save_path + item)
            width, height = img.size
            size_list = [width, height]

            # 4R if landscape & larger than crop size
            if width > height and size_list >= landscape_4R:
                resized = ImageOps.fit(img, landscape_4R, centering=(0.5, 0.5))
                x_file_name = ori + "_4R.jpg"
                resized.save(x_file_name, "JPEG", dpi = hi_res, quality = 90)
                resized.close()

            # 4R if portrait & larger than crop size
            elif height > width and size_list >= portrait_4R:
                resized = ImageOps.fit(img, portrait_4R, centering=(0.5, 0.5))
                x_file_name = ori + "_4R.jpg"
                resized.save(x_file_name, "JPEG", dpi = hi_res, quality = 90)
                resized.close()

            # If smaller than 4R size
            elif size_list < landscape_4R or size_list < portrait_4R:
                messagebox.showerror("File size too small", "'{}' is too small to be resized to 4R.".format(str(item)))
    done_exporting()

# Enter button
enter_btn = Button(window, text="Enter", fg = "white", font = ("Arial", 10, "bold"), bg = "#05AFF2", width = 13, height = 1, command = resize)
enter_btn.grid(row = 8, column = 3, padx = 5, pady = 5, ipady = 5, columnspan = 3)


# run main window
window.mainloop()
