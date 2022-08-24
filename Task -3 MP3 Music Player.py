# Importing all the necessary modules
from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer        
import os
from tkinter import Tk

mixer.init()
mixer.music.set_volume(0.7)

# Setting features of the tkinter window
root = Tk()
root.geometry('500x470')
root.title('My Music Player')
root.resizable(False,False)

def Play(song_name: StringVar,songs_list: Listbox,status: StringVar):#Play Function to play your song
    song_name.set(songs_list.get(ACTIVE))
    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()
    status.set("PLAYING")

def Pause(status: StringVar):#Pause Function to pause your song
    mixer.music.pause()
    status.set("PAUSED")

def Resume(status: StringVar):#Resume Function to resume your song
    mixer.music.unpause()
    status.set("RESUMED")
    
def Stop(status: StringVar):#Stop Function to stop your song
    mixer.music.stop()
    status.set("STOPPED")

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Opens directory'))
    tracks = os.listdir()
    for track in tracks:
        listbox.insert(END,track)

song_frame = LabelFrame(root,text="Current Song", font=("Times New Roman",10,"bold"),bg='#ffb3b3', width=500, height=200)
song_frame.place(x=0, y=0)

button_frame = Label(root,font=("Times New Roman",10,"bold"), bg='#ffb3b3', width=500, height=120)
button_frame.place(x=50,y=80)

listbox_frame = LabelFrame(root,font=("Times New Roman",10,"bold"),text=' My Playlist', bg='#ffb3b3')
listbox_frame.place(x=0, y=200, height=250, width=500)

current_song = StringVar(root,value='Select song')
song_status = StringVar(root,value='Not Available')

playlist = Listbox(listbox_frame, font=("Times New Roman", 11,"bold"))
playlist.pack(fill=BOTH,padx=5,pady=10)

def Widgets():

 Label(root, text="MP3 Music Player",font=("Times New Roman",13,"bold"),bg="light blue").pack()

 Label(song_frame, text='Currently Playing:', bg='light yellow', font=("Times New Roman",12,"bold")).place(x=10, y=20)

 Label(song_frame, textvariable=current_song, bg='#F06246', font=("Times New Roman",12), width=25).place(x=150, y=20)

 Button(button_frame, text='Play', bg='#A7D6B3', font=("Times New Roman",13,"bold"), width=7,command=lambda: Play(current_song, playlist, song_status)).place(x=15, y=10) 
 
 Button(button_frame, text='Pause', bg='#D677A1', font=("Times New Roman",13,"bold"), width=7,command=lambda: Pause(song_status)).place(x=105, y=10) 

 Button(button_frame, text='Resume', bg='#A7D6B3', font=("Times New Roman",13,"bold"), width=7,command=lambda: Resume(song_status)).place(x=195, y=10) 

 Button(button_frame, text='Stop', bg='#D677A1', font=("Times New Roman",13,"bold"), width=7,command=lambda: Stop(song_status)).place(x=285, y=10)

 Button(button_frame, text='Select Playlist', bg='#88C7D6', font=("Times New Roman",13,"bold"), width=20, command=lambda: load(playlist)).place(x=90, y=75)

 Button(root, textvariable=song_status, bg='light grey', font=("Times New Roman",10,"bold")).pack(side=BOTTOM, fill=X)


Widgets()
root.mainloop()