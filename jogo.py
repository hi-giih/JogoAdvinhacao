import random

class Jogador():
    def __init__(self, tentativas) -> None:
        self.__tentativas = tentativas

    def get_tentativas(self):
        return self.__tentativas
    
    def contador(self):
        self.__tentativas += 1

    def exibir_tentativas(self):
        return f"Você fez {self.get_tentativas()} tentativas"


class Jogo():
    def __init__(self) -> None:
        self.jogador = Jogador(tentativas=0)
        
    def iniciar_jogo(self):
        print("Iniciando Jogo!")
        numero = random.randint(1, 10)

        escolha = input("Tente adivinhar o número entre 1 e 10.")
        escolha = int(escolha)

        while escolha != numero:
            self.jogador.contador()
            if escolha < numero:
                print( "O seu palpite foi baixo! Tente novamente.")
                escolha = input()
                escolha = int(escolha)
            elif escolha > numero:
                print( "O seu palpite foi alto! Tente novamente.")
                escolha = input()
                escolha = int(escolha)

        if escolha == numero:
            print(f"Parabéns! Você acertou o número, {self.jogador.exibir_tentativas()}")


jogo = Jogo()
jogo.iniciar_jogo()
