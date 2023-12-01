import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk

class VideoPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Player")

        # Inisialisasi OpenCV VideoCapture
        self.cap = None

        # Frame untuk menampilkan video
        self.video_frame = tk.Label(master)
        self.video_frame.pack(pady=10)

        # Button play
        self.play_button = tk.Button(master, text="Play", command=self.play_video)
        self.play_button.pack(pady=5)

        # Button stop
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_video)
        self.stop_button.pack(pady=5)

        # Path video yang akan diputar
        self.video_path = "Media/Play_video.mp4"

    def play_video(self):
        if self.cap is not None and self.cap.isOpened():
            messagebox.showinfo("Error", "Video is already playing.")
            return

        # Inisialisasi OpenCV VideoCapture dengan file video
        self.cap = cv2.VideoCapture(self.video_path)

        # Periksa apakah video berhasil dibuka
        if not self.cap.isOpened():
            messagebox.showinfo("Error", "Failed to open video.")
            return

        # Baca dimensi video
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Membuat frame untuk menampilkan video
        self.video_frame.config(width=width, height=height)

        # Fungsi untuk membaca dan menampilkan frame video
        def update_frame():
            ret, frame = self.cap.read()
            if ret:
                # Konversi frame dari BGR ke RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Konversi frame OpenCV ke format yang dapat ditampilkan oleh tkinter
                img = Image.fromarray(rgb_frame)
                img = ImageTk.PhotoImage(image=img)

                # Tampilkan frame di label video_frame
                self.video_frame.img = img
                self.video_frame.config(image=img)

                # Jalankan fungsi secara rekursif untuk mendapatkan frame berikutnya
                self.video_frame.after(10, update_frame)
            else:
                # Video selesai, hentikan pemutaran
                self.stop_video()

        # Mulai pemutaran video
        update_frame()

    def stop_video(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
            self.video_frame.config(image=None)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()