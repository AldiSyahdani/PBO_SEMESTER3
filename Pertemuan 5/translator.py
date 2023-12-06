import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator App")
        self.root.geometry("450x350")
        
        style = ttk.Style()
        style.theme_use('alt')  # tema

        self.label1 = ttk.Label(root, text="Enter text:")
        self.label1.pack(pady=10)

        self.entry = ttk.Entry(root, width=60)
        self.entry.pack(pady=10)

        self.label2 = ttk.Label(root, text="Translated text:")
        self.label2.pack(pady=10)

        self.result_text = tk.Text(root, height=5, width=50)
        self.result_text.pack(pady=10)

        self.translate_button_en = ttk.Button(root, text="Translate to English", command=lambda: self.translate_text('en'))
        self.translate_button_en.pack(pady=5)

        self.translate_button_de = ttk.Button(root, text="Translate to German", command=lambda: self.translate_text('de'))
        self.translate_button_de.pack(pady=5)

        self.translate_button_vi = ttk.Button(root, text="Translate to Vietnam", command=lambda: self.translate_text('vi'))
        self.translate_button_vi.pack(pady=5)

    def translate_text(self, dest):
        text_to_translate = self.entry.get()

        if text_to_translate:
            translator = Translator()
            translated_text = translator.translate(text_to_translate, dest=dest).text

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, translated_text)
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please enter text to translate.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()