import tkinter as tk
from datetime import datetime

Elektronik_Zaman = datetime(2023, 5, 14, 7, 0, 0)  #14 Mayıs 2023, 07:00

def countdown():
    current_date = datetime.now() #Anlık tarih ve saat
    remaining_time = Elektronik_Zaman - current_date
    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    countdown_label.config(text=f"{days} gün {hours} saat, {minutes} dakika, {seconds} saniye kaldı")
    countdown_label.after(1000, countdown) # 1 sanİye sonra yeniden çalışır

root = tk.Tk()
root.title("Seçim Geri Sayımı (RECEP TAYYİP VS KILICDARGOLU)")

countdown_label = tk.Label(root, font=("Helvetica",30))
countdown_label.pack(padx=50, pady=50)
countdown()
root.mainloop()
    
