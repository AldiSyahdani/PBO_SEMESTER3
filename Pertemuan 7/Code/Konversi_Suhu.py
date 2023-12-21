import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temperature = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = temperature * 9/5 + 32
            result_label.config(text=f"{temperature}° C = {result:.2f}° F")
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = temperature + 273.15
            result_label.config(text=f"{temperature}° C = {result:.2f} K")
        elif from_unit == "Celsius" and to_unit == "Reamur":
            result = temperature * 4/5
            result_label.config(text=f"{temperature}° C = {result:.2f}° Reamur")
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (temperature - 32) * 5/9
            result_label.config(text=f"{temperature}° F = {result:.2f}° C")
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (temperature - 32) * 5/9 + 273.15
            result_label.config(text=f"{temperature}° F = {result:.2f} K")
        elif from_unit == "Fahrenheit" and to_unit == "Reamur":
            result = (temperature - 32) * 4/9
            result_label.config(text=f"{temperature}° F = {result:.2f}° Reamur")
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = temperature - 273.15
            result_label.config(text=f"{temperature} K = {result:.2f}° C")
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (temperature - 273.15) * 9/5 + 32
            result_label.config(text=f"{temperature} K = {result:.2f}° F")
        elif from_unit == "Kelvin" and to_unit == "Reamur":
            result = (temperature - 273.15) * 4/5
            result_label.config(text=f"{temperature} K = {result:.2f}° Reamur")
        elif from_unit == "Reamur" and to_unit == "Celsius":
            result = temperature * 5/4
            result_label.config(text=f"{temperature}° Reamur = {result:.2f}° C")
        elif from_unit == "Reamur" and to_unit == "Fahrenheit":
            result = temperature * 9/4 + 32
            result_label.config(text=f"{temperature}° Reamur = {result:.2f}° F")
        elif from_unit == "Reamur" and to_unit == "Kelvin":
            result = temperature * 5/4 + 273.15
            result_label.config(text=f"{temperature}° Reamur = {result:.2f} K")
    except ValueError:
        result_label.config(text="Masukkan suhu yang valid.")

# Buat window utama
window = tk.Tk()
window.title("Konverter Suhu")

# Buat frame utama
main_frame = ttk.Frame(window, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Buat label judul
title_label = ttk.Label(main_frame, text="Konverter Suhu", font=("Helvetica", 18))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Buat label dan entry untuk input suhu
label = ttk.Label(main_frame, text="Masukkan suhu:")
label.grid(row=1, column=0, pady=10, padx=5, sticky=tk.W)

entry = ttk.Entry(main_frame)
entry.grid(row=1, column=1, pady=10, padx=5)

# Pilihan konversi dari dan ke
units = ["Celsius", "Fahrenheit", "Kelvin", "Reamur"]

from_var = tk.StringVar(value=units[0])
to_var = tk.StringVar(value=units[1])

from_label = ttk.Label(main_frame, text="Dari:")
from_menu = ttk.OptionMenu(main_frame, from_var, *units)
to_label = ttk.Label(main_frame, text="Ke:")
to_menu = ttk.OptionMenu(main_frame, to_var, *units)

from_label.grid(row=2, column=0, pady=5, padx=5, sticky=tk.W)
from_menu.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)
to_label.grid(row=3, column=0, pady=5, padx=5, sticky=tk.W)
to_menu.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)

# Buat tombol konversi
convert_button = ttk.Button(main_frame, text="Konversi", command=convert_temperature, style="TButton")
convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Buat label untuk menampilkan hasil konversi
result_label = ttk.Label(main_frame, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Style
style = ttk.Style()
style.configure("TFrame", background="#3498db")
style.configure("TLabel", background="#3498db", foreground="white")
style.configure("TButton", background="#2ecc71", foreground="white")

# Jalankan main loop
window.mainloop()