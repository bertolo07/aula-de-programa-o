import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"
        self.janela = tk.Tk()
        self.botoes = []
        self.criar_interface()

    def criar_interface(self):
        for i in range(3):
            linha_botoes = []
            for j in range(3):
                botao = tk.Button(self.janela, text=" ", font=("Arial", 20), width=5, height=2,
                                  command=lambda row=i, col=j: self.realizar_jogada(row, col))
                botao.grid(row=i, column=j, padx=5, pady=5)
                linha_botoes.append(botao)
            self.botoes.append(linha_botoes)

    def realizar_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].configure(text=self.jogador_atual)

            vencedor = self.verificar_vencedor()
            if vencedor:
                messagebox.showinfo("Fim do jogo", f"Parabéns! O jogador {vencedor} venceu!")
                self.janela.quit()

            if all(self.tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
                messagebox.showinfo("Fim do jogo", "O jogo terminou em empate!")
                self.janela.quit()

            self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vencedor(self):
        # Verificar linhas
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != " ":
                return linha[0]

        # Verificar colunas
        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] != " ":
                return self.tabuleiro[0][coluna]

        # Verificar diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            return self.tabuleiro[0][0]
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            return self.tabuleiro[0][2]

        return None

    def iniciar_jogo(self):
        self.janela.mainloop()


jogo = JogoDaVelha() #troquei as aspas pelo sinal de igual.
jogo.iniciar_jogo()
