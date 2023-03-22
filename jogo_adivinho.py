import random
import tkinter as tk
from tkinter import messagebox


class JogoAdivinho:
    def __init__(self, master):
        self.master = master
        master.title("Jogo da Adivinhação")

        # campo de entrada do jogo
        self.entry_label = tk.Label(master, text= f"Digite um número de 0 a 10:")
        self.entry_label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()

        # cria botão para confirmar a tentativa
        self.button = tk.Button(master, text="Tentar", command=self.verificar_tentativa)
        self.button.pack()

        # inicializa o jogo
        self.comp = random.randint(0, 10)
        self.max_tentativas = 3
        self.contador = 0

    def verificar_tentativa(self):
        try:
            jogador = int(self.entry.get())
            self.contador += 1

            if jogador == self.comp:
                messagebox.showinfo("Resultado", f"Você venceu em {self.contador} tentativas.")
                self.master.destroy()

            elif jogador > 11:
                messagebox.showinfo("erro", f"escolha numeros inteiro entre 0 e 10 {self.contador} tentativas")

            elif jogador < self.comp:
                messagebox.showinfo("resultado", f"seu palpite foi baixo: te resta {self.contador} tentativas")

            elif jogador > self.comp:
                messagebox.showinfo("resultado", f"seu palpite foi alto: te resta {self.contador} tentativas")
          
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite apenas números inteiros de 0 a 10.")
        if self.contador == self.max_tentativas:
            messagebox.showinfo("Resultado", f"Você esgotou o número máximo de {self.max_tentativas} tentativas. O número era {self.comp}.")
            self.master.destroy()

root = tk.Tk()
jogo = JogoAdivinho(root)
root.mainloop()
