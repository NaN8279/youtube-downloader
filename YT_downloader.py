import tkinter as tk
import tkinter.messagebox as tkm
import pytube
import os

def locateurl():
    global vid
    try:
        vid = pytube.YouTube(vidurl.get())
        vidtil.configure(text="Video title: %s" % vid.title)
    except:
        vidtil.configure(text="Error: incorrect URL!")
        return
    downlbtn.configure(state='normal')

def downloadvid():
    if downtype.get() == 0:
        vidstrm = vid.streams.filter(only_audio=True).first()
    if downtype.get() == 1:
        vidstrm = vid.streams.filter(only_video=True).first()
    vidtil.configure(text="Downloading...")
    vidstrm.download(os.path.expanduser('~/downloads'))
    vidtil.configure(text="Done!")


root = tk.Tk()
downtype = tk.IntVar()
root.title("YouTube downloader")
urllabel = tk.Label(root, text="Enter the youtube url:")
urllabel.grid(column=0, row=0)
vidurl = tk.Entry(root,width=30)
vidurl.grid(column=0, row=1)
locbtn = tk.Button(root, text="Locate video", command=locateurl)
locbtn.grid(column=1, row=1)
vidtil = tk.Label(root)
vidtil.grid(column=0,row=2)
typelbl = tk.Label(root, text="Select the type of the download:")
typelbl.grid(column=0,row=3)
audio = tk.Radiobutton(root, text="Audio", variable=downtype,value=0)
video = tk.Radiobutton(root, text="Video", variable=downtype,value=1)
audio.grid(column=0,row=4)
video.grid(column=0,row=5)
downlbtn = tk.Button(root,text="Download video", state='disabled', command=downloadvid)
downlbtn.grid(column=0,row=6)
root.mainloop()