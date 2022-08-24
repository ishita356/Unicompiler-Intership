import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox
from tkinter import filedialog

def Widgets():#Widgets function to create tkinter widgets

	Label(root, text="YouTube Video Downloader",font=("Times New Roman",25,"bold"),fg="red",relief=RAISED ).pack()
    
	Label(root,text=" Enter Your link :",font=("Times New Roman",20,"bold"),fg="blue",relief=RAISED ).place(x=20,y=100)

	root.linkText = Entry(root,width=50,textvariable=video_Link).place(x=300,y=110) 
    
	Label(root,text="Select Path :",font=("Times New Roman",20,"bold"),fg="blue",relief=RAISED ).place(x=20,y=200) 

	root.destinationText = Entry(root,width=50,textvariable=download_Path).place(x=300,y=210) 

	Button(root,text="Search",command=Search,width=20,font=("Times New Roman",13,"bold"),fg="green",relief=RAISED ).place(x=250,y=310) 

	Button(root,text="Download Video",command=Download,width=20,font=("Times New Roman",13,"bold"),fg="red",relief=RAISED ).place(x=250,y=380) 


def Search():#Search Function to Create Place to Save Your Downloaded Video
	download_Directory = filedialog.askdirectory(
		initialdir="Your Path", title="Save Video")
	download_Path.set(download_Directory)

def Download():# Download Function to Downloaded Your Video
	Youtube_link = video_Link.get()
	download_file = download_Path.get()
	Video = YouTube(Youtube_link)
	videoStream = Video.streams.first()
	videoStream.download(download_file)


	messagebox.showinfo("Congrats"," Video Downloaded")# Displaying the message To User 
      

# Setting features of the tkinter window
root = tk.Tk()
root.geometry("700x700")
root.title("YouTube Video Downloader")
root.config(background="light blue")
video_Link = StringVar()
download_Path = StringVar()

Widgets()

root.mainloop()
