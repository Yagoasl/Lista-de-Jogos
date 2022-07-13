import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    #numero_secreto = round(random.random()*100) # Pode criar de (0.0 a 1.0) *100
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha o nivel de dificuldade!")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Nível escolhido: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for Tentativa_atual in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(Tentativa_atual, total_de_tentativas))

        chute = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute)
        chute = int(chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou! E fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior que o número secreto!")
            elif(menor):
                print("Você errou! Seu chute foi menor que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("O número secreto era: ",numero_secreto)
    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()