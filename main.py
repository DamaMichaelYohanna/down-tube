import os
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mbox
#
from pytube import YouTube


window = tk.Tk()

window.mainloop()

SAVE_PATH = tk.filedialog.askopen()

link="https://www.youtube.com/watch?v=S4E4yAktjug"

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