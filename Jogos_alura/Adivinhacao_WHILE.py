print("----"*10)
print("Bem vindo no jogo de Adivinhação!")
print("----"*10)

numero_secreto = 10
total_tentativas = 3
rodada = 1

while (rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = input("Digite o seu numero: ") # para o usuário poder digitar
    numero_chute = int(chute)
    print("Você digitou ", numero_chute)
    print("----"*10)

    acertou = numero_secreto == numero_chute
    foi_maior = numero_chute > numero_secreto
    foi_menor = numero_chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if(foi_maior):
            print("Você errou! O seu chute foi MAIOR do que o numero secreto.")
        elif(foi_menor):
            print("Você errou! O seu chute foi MENOR do que o numero secreto.")
    rodada = rodada + 1

print("----"*10)
print("Fim e jogo")