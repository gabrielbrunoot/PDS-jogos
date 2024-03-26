def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    palevra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_acertadas2 = []
    
    for letra in (palevra_secreta):
        letras_acertadas2.append("_")
        
        enforcou = false
        acertou = false
        arros = 0
        
        print(letras_acertadas)
        
        while (not enforcou and not acertou):
            
            chute = input("qual letra?")
            chute = chute.strip().upper()
            
            if (chute in palvra_secreta):
                index = 0
                for letra in palvra_secreta:
                    if (chute == letra):
                        letras_acertadas[index] = letras
                        index += 1 
            else:
                erros += 1 
                
                enforcou = erros == 6 
                acertou = "_" not in letras_acertadas
                print(letras_acertadas)
                
                if (acertou):
                    print("Voce ganhou!!")
                else:
                    print("Voce perdeu!!")
                    print("Fim de jogo")
                    
                    if (__name__ == "__main__"):
                        jogar()
            