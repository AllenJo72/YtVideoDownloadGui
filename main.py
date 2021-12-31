from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import threading


Folder_Name = ""


def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg = "green")

    else:
        locationError.config(text= "Please choose Folder!!", fg="red")

def DownloadVideo():
    global select
    choice = ytdchoices.get()
    url = ytdEntry.get()
    ytdError.config(text="your download has started")

    if (len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link Again", fg="red")

    select.download((Folder_Name))
    ytdError.config(text="Complete!")







root = Tk()
root.title("Youtube Video Downloader")
root.geometry("600x600")
root.columnconfigure(0, weight=1)
Label(root, text="Youtube", bg="red", width="300", height="1", font=("TechnicLite", 50)).grid()
Label(root, text="Video Downloader", bg="red", width="300", height="2", font=("TechnicLite", 50)).grid()
Label(root, text="").grid()
Label(root,font=("MV Boli", 10), text="The software will say not responding after you press \n download. It will only respond once the download is over. \n So dont close the software or the download will be cancelled").grid()
ytdLabel = Label(root, text = "Video URL", font=("MV Boli", 15))
ytdLabel.grid()

ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable=ytdEntryVar)
ytdEntry.grid()

ytdError = Label(root, text="CTRL + V to paste link", fg="purple", font=("MV Boli", 10))
ytdError.grid()

saveLabel= Label(root, text="Save Video File", font=("MV Boli", 15, "bold"))
saveLabel.grid()

saveEntry = Button(root, width = 10, bg = "cyan", text="Select Path", command=openLocation)
saveEntry.grid()


locationError = Label(root, text="Select a correct path", fg = "purple", font = ("MV Boli", 10))
locationError.grid()

ytdQuality = Label(root, text="Choose Quality", font=("MV Boli", 15))
ytdQuality.grid()

choices = ["720p", "144p", "Mp3"]
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.grid()
space = Label(text="").grid()
downloadbtn = Button(root, text="Download", width=10, bg="red",fg="white", command=DownloadVideo)
downloadbtn.grid()


developerlabel = Label(root, text="AnacondaSoft", font=("MV Boli", 15))
developerlabel.grid()




root.mainloop()
