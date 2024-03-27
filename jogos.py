import forca
import adivinhaçao


def escolhe_jogo():
    print("**********************************")
    print("*******Escolha o seu jogo !*******")
    print("**********************************")
    
    print("(1) forca (2) Adivinhaçao")

    jogo = int(input("Qual jogo"))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando adivinhçao")
        adivinhaçao.jogar()
        
if(__name__ == "__main__"):
    escolhe_jogo()
        