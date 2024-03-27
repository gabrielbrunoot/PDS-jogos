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