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
        self.current_folder_label = None

        self.setup_gui()
        
    def setup_gui(self):
        self.select_button = tk.Button(self.root, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=10)
        
        self.current_folder_label = tk.Label(self.root, text="Current Folder: None")
        self.current_folder_label.pack(pady=5)
        
        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=5)
        
        self.back_button = tk.Button(self.root, text="Back", command=self.play_previous)
        self.back_button.pack(pady=5)
        
        self.next_button = tk.Button(self.root, text="Next", command=self.play_next)
        self.next_button.pack(pady=5)
        
        self.current_file_label = tk.Label(self.root, text="")
        self.current_file_label.pack(pady=5)
        
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.audio_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith((".mp3", ".wav"))]
            if not self.audio_files:
                messagebox.showerror("Error", "No audio files found in the selected folder.")
            else:
                self.current_folder_label.config(text="Current Folder: " + folder_path)
        
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
                self.play_next()
        self.root.after(100, self.check_music_end)
        
    def stop(self):
        pygame.mixer.music.stop()
        
    def play_next(self):
        if self.audio_files:
            self.current_index = (self.current_index + 1) % len(self.audio_files)
            pygame.mixer.music.load(self.audio_files[self.current_index])
            pygame.mixer.music.play()
            self.update_current_file_label()
        
    def play_previous(self):
        if self.audio_files:
            self.current_index = (self.current_index - 1) % len(self.audio_files)
            pygame.mixer.music.load(self.audio_files[self.current_index])
            pygame.mixer.music.play()
            self.update_current_file_label()
        
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