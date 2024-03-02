import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        
        self.current_index = 0
        self.audio_files = []
        self.current_file_label = None
        self.paused = False
        self.paused_time = 0

        self.setup_gui()
        
    def setup_gui(self):
        self.select_button = tk.Button(self.root, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=10)
        
        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack(pady=5)
        
        self.pause_resume_button = tk.Button(self.root, text="Pause", command=self.pause_resume)
        self.pause_resume_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=5)
        
        self.current_file_label = tk.Label(self.root, text="")
        self.current_file_label.pack(pady=5)
        
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.audio_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith((".mp3", ".wav"))]
            if not self.audio_files:
                messagebox.showerror("Error", "No audio files found in the selected folder.")
        
    def play(self):
        if not self.audio_files:
            messagebox.showerror("Error", "Please select a folder containing audio files.")
            return
        
        pygame.init()
        pygame.mixer.init()
        
        pygame.mixer.music.load(self.audio_files[self.current_index])
        pygame.mixer.music.play()
        self.update_current_file_label()
        
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        self.root.after(100, self.check_music_end)
        
    def check_music_end(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.current_index = (self.current_index + 1) % len(self.audio_files)
                pygame.mixer.music.load(self.audio_files[self.current_index])
                pygame.mixer.music.play()
                self.update_current_file_label()
        self.root.after(100, self.check_music_end)
        
    def stop(self):
        pygame.mixer.music.stop()
        
    def pause_resume(self):
        if pygame.mixer.music.get_busy():
            if not self.paused:
                pygame.mixer.music.pause()
                self.paused_time = pygame.mixer.music.get_pos()
                self.paused = True
                self.pause_resume_button.config(text="Next")
            else:
                pygame.mixer.music.load(self.audio_files[self.current_index])
                pygame.mixer.music.play(start=self.paused_time / 1000)
                self.paused = False
                self.pause_resume_button.config(text="Mode")

        
    def update_current_file_label(self):
        current_file = os.path.basename(self.audio_files[self.current_index])
        self.current_file_label.config(text="Current file: " + current_file)
        
    def quit(self):
        pygame.mixer.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
