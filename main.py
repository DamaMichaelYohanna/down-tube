import os
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mbox
#
from pytube import YouTube


window = tk.Tk()

##SAVE_PATH = tk.filedialog.askopen()

link="https://www.youtube.com/watch?v=S4E4yAktjug"
class MainWindow(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Down Tube")
        self.parent.resizable(0, 0)
        self.build_ui()

    def build_ui(self):
        main_frame = tk.Frame(self.parent,bg='white')
        main_frame.grid()
        #--------------------------
        head_frame = tk.Frame(main_frame, bg='white')
        head_frame.grid()
        tk.Label(head_frame, text='Down-Tube',
                 bg='white', ).grid(pady=20)
        #-------------------------
        body_frame = tk.Frame(main_frame, bg='white')
        body_frame.grid()
        tk.Label(body_frame, text='Download All Your Youtube Videos',
                 font='alef 19 bold', bg='white',
                 fg='purple').grid(pady=10, padx=100)
        tk.Label(body_frame, text="you are just one click away from your download",
                 bg='white', font='alef 12').grid(pady=2)
        tk.Label(body_frame, text="Drop the url below",
                 bg='white', font='alef 12').grid(pady=2)
        url_var = tk.StringVar()
        tk.Entry(body_frame, textvariable=url_var,
                 bg='white', font='matura 18').grid(pady=5, ipady=2)
        tk.Button(body_frame, text='Download Video',
                  bg='light green',
                  font='alef 12 bold').grid(ipadx=20, pady=10)
MainWindow(window)
window.mainloop()
#
# try:
# 	# object creation using YouTube
# 	# which was imported in the beginning
# 	print('about trying it out')
# 	yt = YouTube(link)
# 	print('done trying')
# except:
# 	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
print('about filtering')
YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
print('done filtering')

#to set the name of the file
# yt.set_filename('GeeksforGeeks Video')

# get the video with the extension and
# resolution passed in the get() function
# d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
# try:
# 	# downloading the video
# 	stream = yt.streams.get_by_itag(22)
# 	stream.download(SAVE_PATH)
# except:
# 	print("Some Error!")
# print('Task Completed!')
#
