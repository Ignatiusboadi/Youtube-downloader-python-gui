from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pytube

root = Tk()
root.resizable(0, 0)
root.title('Youtube Downloader')
app_width = 555
app_height = 180
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord = screen_width//2 - app_width//2
y_coord = screen_height//2 - app_height//2
root.geometry(f'{app_width}x{app_height}+{x_coord}+{y_coord}')

def download():
    try:
        link = url_input.get()
        streams = pytube.YouTube(link)
        streams.streams.filter(progressive=True).order_by('resolution').desc().first().download()
        messagebox.showinfo(title='Sucessful', 
                            message=f'Download Complete!\n{streams.title} saved in {os.getcwd()}')
    except:
        messagebox.showwarning(title='Warning!', 
        message='An Error was encountered, kindly check your\ninternet connection or the link entered.')


def download_playlist():
    try:
        link = playlist_url.get()
        playlist = pytube.Playlist(link)
        videos = playlist.videos
        for video in videos:
            video.streams.filter(progressive=True).order_by('resolution').desc().first().download()
    except:
        messagebox.showwarning(title='Warning!', 
        message='An Error was encountered, kindly check your\ninternet connection or the link entered.')


single_video = LabelFrame(root, text='Single Video Download', padx=5, pady=5, bg='mistyrose')
url_label = Label(single_video, text='Enter url: ', relief='groove')
url_label.grid(row=0, column=0, sticky='we')
url_input = Entry(single_video, bd=2)
url_input.config(width=80)
url_input.grid(row=0, column=1, sticky='we')
video_download = Button(single_video, text='Download', command=download, background='green')
video_download.grid(row=1, column=0, columnspan=2, sticky='we')
single_video.grid(row=0, column=0, sticky='we')

playlist_download = LabelFrame(root, text='Playlist Download',padx=5, pady=5, background='lavender')
playlist_label = Label(playlist_download, text='Enter url: ', relief='groove')
playlist_label.grid(row=0, column=0, sticky='we')
playlist_url = Entry(playlist_download, bd=2)
playlist_url.config(width=80)
playlist_url.grid(row=0, column=1, sticky='we')
playlist_download_button = Button(playlist_download, text='Download', bg='green', command=download_playlist)
playlist_download_button.grid(row=1, column=0, columnspan=2, sticky='we')
playlist_download.grid(row=1, column=0, sticky='we')
Button(root, text='Exit', bg='red', command=root.destroy).grid(row=2, column=0, columnspan=2, sticky='we')
root.mainloop()
