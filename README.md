# Quicksizer
Quicksizer is a 4R image resizer that helps speed up your photobooth printing processes.

## Getting Started
Quicksizer should be pretty straightforward,
simply select a folder of files where you wish to resize & an output path for the exported files to be saved in, & click "Enter".

Quicksizer is not an executable yet, you will need Python installed in your system & the terminal to launch the Python script.
Open up the terminal, change to the script directory, type 
```
python quicksizer.py
```
& Quicksizer should run just fine.

## Prerequisites
Currently, Quicksizer only works for JPEG formated images & was only tested on 64-bit Windows 10.
Make sure JPEG files are larger than 4R size, which is equivalent to 1800px X 1200px & vice versa.
To get the best result, images must be in 4:3 ratio.

## How It Looks Like
1. Input your desired directories for input & output image files.

![Example 1](screenshots/quick_1.jpg)

2. You will be notified when the process is done.

![Example 2](screenshots/quick_2.jpg)

3. Check your output directory to see your resized images.

![Example 3](screenshots/quick_3.jpg)


## Built With
Python 3.6

## Modules
os, tkinter, PIL, resizeimage

## Versioning
Quicksizer is nothing but a personal project & still in development, future version with more features may be released.

## Acknowledgement
You may replicate, modify or use the code from this open source project for your own project.

However, you may NOT use, modify or redistribute the images from this project without consent of this project's owner.
