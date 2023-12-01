import tkinter as tk
import pygame
from tkinter import Label

class MusicPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")

        # Inisialisasi pygame mixer
        pygame.mixer.init()

        # Button play
        self.play_button = tk.Button(master, text="Play Song", command=self.play_music)
        self.play_button.pack(pady=10)

        # Button stop
        self.stop_button = tk.Button(master, text="Stop Song", command=self.stop_music)
        self.stop_button.pack(pady=10)

        # Label untuk menampilkan info file
        self.grid = Label(master, text="Now Playing: ")
        self.grid.pack(pady=5)

        # Lokasi file musik
        self.music_file = "Media/MAGIC_Rude_Music.mp3"

    def play_music(self):
        # Stop musik yang sedang diputar
        pygame.mixer.music.stop()

        # Load dan mainkan musik
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play()

        # Update label dengan informasi musik yang diputar
        self.grid.config(text="Now Playing: " + self.music_file)

    def stop_music(self):
        # Hentikan musik
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
