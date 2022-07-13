import forca
import Adivinhacao

def escohe_jogo():
    print("*********************************")
    print(" Bem vindo!! Escolha o seu jogo! ")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        Adivinhacao.jogar()

if(__name__ == "__main__"):
    escohe_jogo()