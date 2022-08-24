
import JogoAdivinhacao
import JogoForca

print("**********************************")
print("Escolha o seu Jogo!")
print("**********************************")

print("(1) Forca, (2) Adivinhação")

jogo = int(input("Qual o jogo?"))

if(jogo == 1):
    print("Você está no jogo da Forca!")
    JogoForca.jogar()

elif(jogo == 2):
    print("Você está no jogo de Adivinhação!")
    JogoAdivinhacao.jogar()