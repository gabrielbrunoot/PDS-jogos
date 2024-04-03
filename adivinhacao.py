import random

nomeroSecreto = random.randint(1, 101)
tentativas = 0 

def jogar():
    
    print("*********************************")
    print("Bem vindo ao jogo de adivinhaçao!")
    print("*********************************")
    
    NivelDigiculdade()
    
    print("numero secreto", numeroSecreto)
    global tentativas
    while tentativas > 0:
        numeroDigitado = int(
            input("Digite um numero de 1 a 100 para tentar adivinhar o numero secreto: "))
        if numeroDigitado == numeroSecreto:
            print("Parabens o numero escolhido esta correto")
            print("O numero secreto era", numeroSecreto)
            break
        else:
            tentativas -= 1 
            print("o numero ets errado")
            pint(dica(numeroDigitado))
            if tentativas > 0: 
                print("tente novamente, voce tem: ", tentativas, "tentativas")
            else:
                print("game over")

def dica (numeroEscolhido: int):
    print("Escolhido", numeroEscolhido, "Secreto", numeroSecreto)
    if numeroEscolhido > numeroSecreto:
        return "O numero escolhido é Maior que o numero secreto, ", numeroEscolhido
    else:
        return "O numero escolhido é Menor que o numero secreto", numeroEscolhido

def NivelDificuldade():
    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")
    dificuldade = int(input("Defina o nivel: "))
    global tentativas
    if (dificuldade == 1):
        tentativas = 1
    elif (dificuldade == 2):
        tentativas = 8
    else:
        tentativas = 6

54 jogar()
