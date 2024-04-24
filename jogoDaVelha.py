import tkinter as tk
import os
os.system("clear")

class Jogo_da_velha:
    def __init__(self):
        self.tabuleiro_visivel = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.jogadas = [[],[]] # o primeiro array são as jogadas do "X" e o segundo as jogados do "O"
        self.jogadas_certas = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [7,5,3]]
        self.historico = [0, 0]
        self.turno = [True, "X", 0] # Turno True = "X" false = "O" vez da jogada caso seja 0 sera no arr do X e se for 1 sera no 0

    def iniciar(self):
        while True:
            print(" \nInforme o numero de acordo com sua ação")
            print("\n1 - Jogar \n2 - Histórico de partidas \n3 - Finaliza progama")
            try:
                acao = int(input(":"))
                if acao == 1:
                    self.jogar()
                elif acao == 2:
                    self.visualizer_historico()
                elif acao == 3:
                    break
            except:
                print("Informe uma ação válida")
        else:
            print("\n Progama Finalizado")

    def visualizer_historico (self):
        print(f"\njogador 'X' venceu {self.historico[0]} partidas \njogador 'O' venceu {self.historico[1]} partidas")

    def visualizar_tabuleiro(self):
        print("\n┌───┬───┬───┐")
        print(f"│ {self.tabuleiro_visivel[0]} │ {self.tabuleiro_visivel[1]} │ {self.tabuleiro_visivel[2]} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro_visivel[3]} │ {self.tabuleiro_visivel[4]} │ {self.tabuleiro_visivel[5]} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro_visivel[6]} │ {self.tabuleiro_visivel[7]} │ {self.tabuleiro_visivel[8]} │")
        print("└───┴───┴───┘")

    def trocar_turno(self):
        if self.turno[0]:
            self.turno = [False, "O", 1]
        else: 
            self.turno = [True, "X", 0]

    def jogada(self, posicao):
        if self.tabuleiro_visivel[posicao-1] != " ":
            raise NameError("Posicão já ocupada")
        else:
            self.jogadas[self.turno[2]].append(posicao)
            self.tabuleiro_visivel[posicao-1] = self.turno[1]

    def verifica_ganhador(self):
        for combinacao in self.jogadas_certas:
            acertos = 0
            for numero_certo in combinacao:
                if numero_certo in self.jogadas[self.turno[2]]:
                    acertos += 1
                    if acertos == 3: 
                        return True   
        
    def verifica_velha(self): 
        casas_vazias = 9
        for casa in self.tabuleiro_visivel:
            if casa  != " ":
                casas_vazias -= 1
        return True if casas_vazias == 0 else False 

    def jogar(self):
        self.jogadas = [[],[]] 
        self.tabuleiro_visivel = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.visualizar_tabuleiro()
        while True:
            try :
                self.jogada(int(input(f"\nJogador {self.turno[2]+1} sua vez: ")))
                print()
                self.visualizar_tabuleiro()
                if self.verifica_ganhador():
                    print(f"\nJogador {self.turno[2]+1} vençeu!")
                    self.historico[self.turno[2]] += 1
                    break
                elif self.verifica_velha():
                    print(f"\nDeu Velha!")
                    break
                self.trocar_turno()
            except:
                print("Jogada Inválida")

jogo1 = Jogo_da_velha()
jogo1.iniciar()