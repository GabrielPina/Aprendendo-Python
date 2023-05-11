import adivinhacao
import forca

def escolher_jogo():

    print("--"*22)
    print("--"*6,"Escolha seu Jogo!","--"*6)
    print("--"*22)

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogano forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("Jogo da adivinhação")
        adivinhacao.jogar_adivinhacao()
if(__name__ == "__main__"):
    escolher_jogo()