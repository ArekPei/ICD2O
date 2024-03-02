import tkinter as tk
from tkinter import filedialog
import subprocess

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("MP4 Video Player")
        self.root.geometry("600x400")

        self.video_frame = tk.Frame(self.root)
        self.video_frame.pack(pady=10)

        self.player = None

        self.open_button = tk.Button(self.root, text="Open Video", command=self.open_video)
        self.open_button.pack(pady=5)

    def open_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        if file_path:
            try:
                if self.player:
                    self.player.terminate()
                ffplay_path = r"C:\Users\Eric\Documents\ffmpeg-2024-02-29-git-4a134eb14a-essentials_build\bin\ffplay.exe"  # Change this to the actual path of ffplay
                self.player = subprocess.Popen([ffplay_path, '-autoexit', file_path])
            except Exception as e:
                print("Error:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()