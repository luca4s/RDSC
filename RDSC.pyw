import os
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import ffmpeg
Versions = "C:/Users/" + os.getlogin() + "/AppData/Local/Roblox/Versions/"
if os.path.exists(Versions):
    print("Roblox Folder found. Locating Version...")
    for dir in os.listdir(Versions):
        if os.path.isdir(Versions + dir) and os.path.exists(Versions + dir + "/RobloxPlayerBeta.exe"):
            print("Version Found.")
            Version = dir
    if "Version" in vars() and os.path.isdir(Versions + Version):
        Sounds = Versions + Version + "/content/sounds/"
        SelectedFile = fd.askopenfilename(title='Select a media file.', initialdir='', filetypes=(("Media Files", ("*.mp4", "*.mp3", "*.ogg", "*.wav", "*.m4a", "*.mov", "*.flv", "*.mkv", "*.ts", "*.m3u8")), ("All Files", "*.*")))
        if os.path.isfile(SelectedFile):
            if os.path.exists(Sounds + 'ouch.ogg'):
                os.remove(Sounds + 'ouch.ogg')
                print("Removed current death sound.")
            print("Starting to convert selected file...")
            file = ffmpeg.input(SelectedFile)
            file = ffmpeg.output(file, Sounds + 'ouch.ogg')
            ffmpeg.run(file)
            mb.showinfo("Roblox Death Sound Changer", "Successfully changed death sound!")
        else:
            mb.showerror("Roblox Death Sound Changer", "Selected file doesn't exist.")
    else:
        mb.showerror("Roblox Death Sound Changer", "Version folder not found.")
else:
    mb.showerror("Roblox Death Sound Changer", "Roblox folder not found.")
