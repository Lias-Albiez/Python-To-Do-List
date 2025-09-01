

import tkinter as tk
from tkinter import simpledialog

# Fenster erstellen
Window = tk.Tk()
Window.title("To-Do-Liste")
Window.geometry("400x300")


Window.configure(bg="#2c2c2c")  # Setzt die Hintergrundfarbe des Fensters

# Liste der Aufgaben (Frame + zugehörige Checkbox-Variable)
Aufgaben = []

def aufgabe_hinzufügen():
    Window.update()
    text = simpledialog.askstring("Hinzufügen", "Aufgabe:", parent=Window)
    Window.focus_force() 

    if text and text.strip():
        frame = tk.Frame(Window, bg="#3b3b3b")
        frame.pack(fill=tk.X, padx=5, pady=2)
        
        var = tk.BooleanVar()
        tk.Checkbutton(frame, variable=var, bg= "#3b3b3b", activebackground="#3b3b3b").pack(side=tk.LEFT)
        tk.Label(frame, text=text.strip(), fg="white", bg="#3b3b3b").pack(side=tk.LEFT, padx=5)


        # Lösch Button
        tk.Button(
            frame, text="✕", fg="White", bg = "#8b0000", activebackground="#8b0000", font=("Arial, 12"),
            command=lambda: [frame.destroy(), Aufgaben.remove((frame, var))]
        ).pack(side=tk.RIGHT)

        Aufgaben.append((frame, var))


def remove_selected():
    # Markierte Aufgabe Löschen
    for frame, var in Aufgaben[:]: 
        if var.get():
            frame.destroy()
            Aufgaben.remove((frame, var))



button_style = {
    "font": ("Segoe UI", 11, "bold"),
    "bd": 0,
    "relief": "flat",
    "highlightthickness": 0,
    "padx": 12,
    "pady": 6
}


# Buttons
tk.Button(Window, text="  ➕ Aufgabe Hinzufügen  ", command=aufgabe_hinzufügen, fg= "white", bg= "#0d6efd", activebackground="#084298", **button_style,
        ).pack(pady=(15, 5))


tk.Button(Window, text="🗑️Markierte löschen", command=remove_selected, fg = "white", bg = "#dc3545", activebackground = "#990000", **button_style,
          ).pack(pady=5)



# starten
Window.mainloop()