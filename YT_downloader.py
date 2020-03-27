#Made by 13 year old NaN8279
#1  33333
#1      3
#1      3
#1  33333
#1      3
#1      3
#1  33333

#Import the needed packages
import tkinter as tk
import tkinter.messagebox as tkm
import pytube
import os

#Define the function for the locating of the video
def locateurl():
    #Make the vid variable global
    global vid
    #Try to locate the video, if this gives a error, warn the user
    try:
        #Set the vid variable to the given YouTube video
        vid = pytube.YouTube(vidurl.get())
        #Give the user the title of the video
        vidtil.configure(text="Video title: %s" % vid.title)
    except:
        #Give the user a warning and return
        vidtil.configure(text="Error: incorrect URL!")
        return
    #Enable the download button
    downlbtn.configure(state='normal')

#Download the video to the download directory    
def downloadvid():
    #If the user selected audio, download the first audio file
    if downtype.get() == 0:
        vidstrm = vid.streams.filter(only_audio=True).first()
    #If the user selected video, download the first video file
    if downtype.get() == 1:
        vidstrm = vid.streams.filter(only_video=True).first()
    #Give the user the downloading message
    vidtil.configure(text="Downloading...")
    #Download the video to the users downloads directory
    vidstrm.download(os.path.expanduser('~/Downloads'))
    #Give the user the done message
    vidtil.configure(text="Done!")

#Make the window
root = tk.Tk()
#Define the downtype variable
downtype = tk.IntVar()
#Set the title to YouTube downloader
root.title("YouTube downloader")
#Make the urllabel
urllabel = tk.Label(root, text="Enter the youtube url:")
urllabel.grid(column=0, row=0)
#Make the entry for the video url
vidurl = tk.Entry(root,width=30)
vidurl.grid(column=0, row=1)
#Make the button to locate the video
locbtn = tk.Button(root, text="Locate video", command=locateurl)
locbtn.grid(column=1, row=1)
#Make the label for the video title
vidtil = tk.Label(root)
vidtil.grid(column=0,row=2)
#Make the label for the selecting of the download type
typelbl = tk.Label(root, text="Select the type of the download:")
typelbl.grid(column=0,row=3)
#Make the radio buttons for the download type
audio = tk.Radiobutton(root, text="Audio", variable=downtype,value=0)
video = tk.Radiobutton(root, text="Video", variable=downtype,value=1)
audio.grid(column=0,row=4)
video.grid(column=0,row=5)
#Make the download button
downlbtn = tk.Button(root,text="Download video", state='disabled', command=downloadvid)
downlbtn.grid(column=0,row=6)
#Start the window
root.mainloop()
