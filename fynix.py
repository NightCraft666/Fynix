import tkinter as tk
from tkinter import messagebox
import os

# Lista gier (można dodać więcej)
games = [
    {"title": "Gra Pierwsza"},
    {"title": "Super Wyścigi"},
    {"title": "Pixelowa Przygoda"},
    {"title": "Strzelanka 3000"},
    {"title": "Kosmiczny Skok"}
]

INSTALL_DIR = "zainstalowane_gry"

# Tworzy folder na gry
os.makedirs(INSTALL_DIR, exist_ok=True)

# Sprawdź, czy gra jest zainstalowana
def is_installed(game_title):
    return os.path.exists(os.path.join(INSTALL_DIR, game_title))

# "Instalowanie" gry
def install_game(game_title):
    os.makedirs(os.path.join(INSTALL_DIR, game_title), exist_ok=True)
    refresh_game_list()

# "Odinstalowanie" gry
def uninstall_game(game_title):
    game_path = os.path.join(INSTALL_DIR, game_title)
    if os.path.exists(game_path):
        os.rmdir(game_path)
    refresh_game_list()

# "Uruchamianie" gry
def play_game(game_title):
    messagebox.showinfo("Graj", f"Uruchamianie: {game_title}")

# Odśwież listę gier
def refresh_game_list():
    for widget in game_frame.winfo_children():
        widget.destroy()

    search_query = search_var.get().lower()

    for game in games:
        title = game["title"]
        if search_query in title.lower():
            frame = tk.Frame(game_frame)
            frame.pack(pady=5, fill="x")

            tk.Label(frame, text=title, font=("Arial", 12)).pack(side="left", padx=10)

            if is_installed(title):
                tk.Button(frame, text="Graj", command=lambda t=title: play_game(t)).pack(side="right", padx=5)
                tk.Button(frame, text="Odinstaluj", command=lambda t=title: uninstall_game(t)).pack(side="right", padx=5)
            else:
                tk.Button(frame, text="Zainstaluj", command=lambda t=title: install_game(t)).pack(side="right", padx=5)

# Utwórz główne okno
root = tk.Tk()
root.title("Mini Steam Launcher")
root.geometry("500x400")
root.configure(bg="#1e1e1e")

# Pole wyszukiwania
search_var = tk.StringVar()
search_entry = tk.Entry(root, textvariable=search_var, font=("Arial", 12), width=40)
search_entry.pack(pady=10)
search_entry.bind("<KeyRelease>", lambda event: refresh_game_list())

# Ramka z listą gier
game_frame = tk.Frame(root, bg="#2b2b2b")
game_frame.pack(fill="both", expand=True)

# Załaduj gry
refresh_game_list()

root.mainloop()
