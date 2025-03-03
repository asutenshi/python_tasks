import tkinter as tk
from tkinter import ttk
import requests
import re

def wl(account_id, wins_var, losses_var, error_label):
    URL = f'https://api.opendota.com/api/players/{account_id}/wl'
    try:
        req = requests.get(URL)
        req.raise_for_status()
        stats = req.json()
        wins_var.set(str(stats['win']))
        losses_var.set(str(stats['lose']))
        error_label.config(text="")
        if (int(wins_var.get()) == 0 and int(losses_var.get()) == 0):
            error_label.config(text=f"У аккаунта {account_id} нет игр")
            wins_var.set("")
            losses_var.set("")
    except requests.exceptions.RequestException as e:
        error_label.config(text=f"Ошибка при запросе к API: {e}")
        wins_var.set("")
        losses_var.set("")
    except KeyError:
        error_label.config(text="Ошибка обработки данных API: Неверный формат ответа")
        wins_var.set("")
        losses_var.set("")
    except Exception as e:
        error_label.config(text=f"Неизвестная ошибка: {e}")
        wins_var.set("")
        losses_var.set("")

def check_stats():
    inp = steam_id_entry.get()
    pattern = r'^\d{9}$'

    if re.match(pattern, inp):
        error_label.config(text="")
        wl(int(inp), wins_var, losses_var, error_label)
    else:
        error_label.config(text='Неправильно введен Steam32 ID. ID должен состоять из 9 цифр.')
        wins_var.set("")
        losses_var.set("")

root = tk.Tk()
root.title("Dota 2 Win/Loss Checker")

steam_id_var = tk.StringVar()
wins_var = tk.StringVar()
losses_var = tk.StringVar()

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

steam_id_label = ttk.Label(frame, text="Steam32 Account ID (9 цифр):")
steam_id_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

steam_id_entry = ttk.Entry(frame, textvariable=steam_id_var)
steam_id_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

check_button = ttk.Button(frame, text="Проверить", command=check_stats)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

wins_label = ttk.Label(frame, text="Победы:")
wins_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

wins_value_label = ttk.Label(frame, textvariable=wins_var)
wins_value_label.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

losses_label = ttk.Label(frame, text="Поражения:")
losses_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

losses_value_label = ttk.Label(frame, textvariable=losses_var)
losses_value_label.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

error_label = ttk.Label(frame, foreground="red")
error_label.grid(row=4, column=0, columnspan=2, pady=10)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()