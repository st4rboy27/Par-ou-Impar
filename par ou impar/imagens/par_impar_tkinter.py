import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import os

def verificar_resultado():
    try:
        numero_usuario = int(entry_numero.get())
        if numero_usuario < 0 or numero_usuario > 10:
            raise ValueError("Número fora do intervalo.")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))
        return

    numero_computador = random.randint(0, 10)
    soma = numero_usuario + numero_computador

    if escolha.get() == "par" and soma % 2 == 0 or escolha.get() == "impar" and soma % 2 != 0:
        resultado_label.config(image=win_img)
    else:
        resultado_label.config(image=lose_img)

    computador_label.config(text=f"O computador escolheu: {numero_computador}")
    soma_label.config(text=f"A soma dos números é: {soma}")

def escolher_par():
    escolha.set("par")
    par_button.config(state=tk.DISABLED, bg="#4CAF50")
    impar_button.config(state=tk.NORMAL, bg="#FF5722")

def escolher_impar():
    escolha.set("impar")
    impar_button.config(state=tk.DISABLED, bg="#FF5722")
    par_button.config(state=tk.NORMAL, bg="#4CAF50")

root = tk.Tk()
root.title("Jogo Par ou Ímpar")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

escolha = tk.StringVar(value="")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

par_button = tk.Button(frame, text="Par", font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=10, command=escolher_par)
par_button.grid(row=0, column=0, padx=10)

impar_button = tk.Button(frame, text="Ímpar", font=("Arial", 12), bg="#FF5722", fg="white", padx=20, pady=10, command=escolher_impar)
impar_button.grid(row=0, column=1, padx=10)

entry_numero = tk.Entry(frame, width=5, font=("Arial", 14))
entry_numero.grid(row=1, column=0, columnspan=2, pady=10)

confirmar_button = tk.Button(frame, text="Confirmar", font=("Arial", 12), bg="#007BFF", fg="white", command=verificar_resultado)
confirmar_button.grid(row=2, column=0, columnspan=2, pady=10)

computador_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333")
computador_label.pack(pady=5)

soma_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333")
soma_label.pack(pady=5)

resultado_label = tk.Label(root, bg="#f0f0f0")
resultado_label.pack(pady=20)

# Caminho absoluto para as imagens
win_img_path = r"C:\Users\MJ\par ou impar\imagens\win.png"
lose_img_path = r"C:\Users\MJ\par ou impar\imagens\lose.png"

# Carregar imagens
win_img = ImageTk.PhotoImage(Image.open(win_img_path))
lose_img = ImageTk.PhotoImage(Image.open(lose_img_path))

root.mainloop()
