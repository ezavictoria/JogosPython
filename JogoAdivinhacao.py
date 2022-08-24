import random

def jogar():

    print("**********************************")
    print("Bem-vindxs ao Jogo de Adivinhação!")
    print("**********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("Nível 1: Fácil, Nível 2: Médio, Nível 3: Difícil")

    nivel = int(input("Defina o nível:"))

    if(nivel == 1):
        total_tentativas = 20

    elif(nivel == 2):
        total_tentativas = 10

    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute = input("Digite um número entre 1 e 100: ")
        print("Você digitou" , chute)

        numero = int(chute)

        if(numero < 1 or numero > 100):
            print("Você deve digitar um número entre 0 e 100.")
            continue

        acertou = numero == numero_secreto  
        chute_maior = numero > numero_secreto
        chute_menor = numero < numero_secreto

        if(acertou):
            print ("Parabéns, você acertou! E, fez {} pontos!".format(pontos))
            break

        else:
            if(chute_maior):
                print("Que pena, você errou! O seu chute foi maior que o número secreto.")
            elif(chute_menor):
                print("Que pena, você errou! O seu chute foi menor que o número secreto.")

            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo.")