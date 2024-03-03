import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3
import mutagen.id3._util

root = Tk()
root.minsize(300, 300)

listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root, textvariable=v, width=35)
folderlabel = Label(root, text="Selected Folder: ", anchor=W, justify=LEFT, padx=10)

index = 0

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)
    folderlabel.config(text=f"Selected Folder: {directory}")

    for filename_bytes in os.listdir(directory.encode()):
        try:
            filename = filename_bytes.decode('utf-8')
            if filename.endswith(".mp3"):
                realdir = os.path.join(directory, filename)
                audio = ID3(realdir)
                realnames.append(audio.get('TIT2', ["Unknown"])[0])
                listofsongs.append(filename)
        except (mutagen.id3._util.ID3NoHeaderError, Exception) as e:
            print(f"Warning: {filename} {e}, skipping.")

    if listofsongs:
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(directory, listofsongs[0]))
        pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    audio = ID3(os.path.join(os.getcwd(), listofsongs[index]))
    v.set(audio.get('TIT2', ["Unknown"])[0])

def nextsong(event):
    global index
    if index < len(listofsongs) - 1:
        index += 1
    else:
        index = 0
    pygame.mixer.music.load(os.path.join(os.getcwd(), listofsongs[index]))
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    if index > 0:
        index -= 1
    else:
        index = len(listofsongs) - 1
    pygame.mixer.music.load(os.path.join(os.getcwd(), listofsongs[index]))
    pygame.mixer.music.play()
    updatelabel()

def unpausesong(event):
    pygame.mixer.music.unpause()
    v.set("Song Unpaused")

def pausesong(event):
    pygame.mixer.music.pause()
    v.set("Song Paused")

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

label = Label(root, text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

for items in realnames:
    listbox.insert(0, items)

nextbutton = Button(root, text='Next Song')
nextbutton.pack()

previousbutton = Button(root, text='Previous Song')
previousbutton.pack()

pausebutton = Button(root, text='Pause Song')
pausebutton.pack()

unpausebutton = Button(root, text='Unpause Song')
unpausebutton.pack()

stopbutton = Button(root, text='Stop Music')
stopbutton.pack()

nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>", prevsong)
pausebutton.bind("<Button-1>", pausesong)
unpausebutton.bind("<Button-1>", unpausesong)
stopbutton.bind("<Button-1>", stopsong)

songlabel.pack()
folderlabel.pack(anchor=W, padx=10)
root.mainloop()