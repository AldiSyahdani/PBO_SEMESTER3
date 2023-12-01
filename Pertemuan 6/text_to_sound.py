import tkinter as tk
from gtts import gTTS
from playsound import playsound

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text to Speech")

        # Inisialisasi variabel pilihan bahasa
        self.language_var = tk.StringVar()
        self.language_var.set("id")  # Default bahasa Indonesia

        # Text entry untuk input teks
        self.text_entry = tk.Entry(master, width=50)
        self.text_entry.pack(pady=10)

        # Label untuk memilih bahasa
        self.language_label = tk.Label(master, text="Choose Language:")
        self.language_label.pack()

        # RadioButton untuk bahasa Indonesia
        self.radio_indonesia = tk.Radiobutton(master, text="Bahasa Indonesia", value="id", variable=self.language_var)
        self.radio_indonesia.pack()

        # RadioButton untuk bahasa Inggris
        self.radio_english = tk.Radiobutton(master, text="English", value="en", variable=self.language_var)
        self.radio_english.pack()

        # Button untuk mengonversi teks ke suara
        self.convert_button = tk.Button(master, text="Convert to Speech", command=self.convert_to_speech)
        self.convert_button.pack(pady=5)

    def convert_to_speech(self):
        # Dapatkan teks dari text entry
        text_to_speak = self.text_entry.get()

        # Dapatkan pilihan bahasa
        language = self.language_var.get()

        # Pastikan teks tidak kosong
        if text_to_speak:
            # Gunakan gTTS untuk mengonversi teks ke suara
            tts = gTTS(text=text_to_speak, lang=language)

            # Simpan audio dalam file sementara
            tts.save("temp_audio.mp3")

            # Putar audio dari file sementara
            playsound("temp_audio.mp3")
        else:
            # Jika teks kosong, tampilkan pesan peringatan
            tk.messagebox.showinfo("Warning", "Please enter text to convert.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()