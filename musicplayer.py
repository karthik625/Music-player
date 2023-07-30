from tkinter import *
from pygame import mixer
import os
root=Tk()
root.resizable(0,0)
root.title('Music Player')
def play():
    currentsong=playlist.get(ACTIVE)
    mixer.music.load(currentsong)
    mixer.music.play()
def pause():
    mixer.music.pause()
def resume():
    mixer.music.unpause()
def stop():
    mixer.music.stop()
mixer.init()
playlist = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), width=30) 
playlist.grid(columnspan=4)
os.chdir = os.chdir(r"C:\Users\playlist")
songs = os.listdir()
for s in songs: 
    playlist.insert(END, s)
playbtn = Button(root, text="Play", command=play,bg='yellow',fg='blue')
playbtn.grid(row=1, column=0)

pausebtn = Button(root, text="Pause", command=pause,bg='yellow',fg='red')
pausebtn.grid(row=1, column=1)

Resumebtn = Button(root, text="Resume", command=resume,bg='yellow',fg='green')
Resumebtn.grid(row=1, column=2)

stopbtn = Button(root, text="Stop", command=stop,bg='red',fg='black')
stopbtn.grid(row=1, column=3)
mainloop()