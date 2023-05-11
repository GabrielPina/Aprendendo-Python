import random

def jogar_adivinhacao():

    print("----"*10)
    print("Bem vindo no jogo de Adivinhação!")
    print("----"*10)

    numero_secreto = random.randrange(1,101,1)
    #print(numero_secreto)
    total_tentativas = 0
    pontos = 1000
    #rodada = 1

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = input("Digite um numero entre 1 e 100: ") # para o usuário poder digitar
        numero_chute = int(chute)
        print("Você digitou ", numero_chute)
        print("----"*10)

        if(numero_chute < 1 or numero_chute > 101):
            print("Você deve digitar um numero entre 1 e 100!")
            print("----" * 10)
            continue

        acertou = numero_secreto == numero_chute
        foi_maior = numero_chute > numero_secreto
        foi_menor = numero_chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(foi_maior):
                print("Você errou! O seu chute foi MAIOR do que o numero secreto.")
            elif(foi_menor):
                print("Você errou! O seu chute foi MENOR do que o numero secreto.")
                pontos_perdidos = abs(numero_secreto - numero_chute)
                pontos = pontos - pontos_perdidos

    print("----"*10)
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar_adivinhacao()