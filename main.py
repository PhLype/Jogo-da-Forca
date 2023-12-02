import random

class Cor:
    RESET = "\033[0m"
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CIANO = "\033[96m"

mensagem_fim = """
 ____  ____  __  __    ____  ____     ____  _____  ___  _____ 
( ___)(_  _)(  \/  )  (  _ \( ___)   (_  _)(  _  )/ __)(  _  )
 )__)  _)(_  )    (    )(_) ))__)   .-_)(   )(_)(( (_-. )(_)( 
(__)  (____)(_/\/\_)  (____/(____)  \____) (_____)\___/(_____)
"""

def escolher_palavra():
    palavras = ["python", "programacao", "jogo", "computador", "desenvolvimento"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra
        else:
            exibicao += "_"
    return exibicao

def jogar_forca():
    palavra_secreta = escolher_palavra()
    tentativas_maximas = 6
    letras_corretas = []
    tentativas = 0

    mensagem_ascii = """
 ____  _   _  __   _  _  ____  ____ 
(  _ \( )_( )(  ) ( \/ )(  _ \( ___)
 )___/ ) _ (  )(__ \  /  )___/ )__) 
(__)  (_) (_)(____)(__) (__)  (____)
    """
    print(Cor.AZUL + mensagem_ascii + Cor.RESET)
    print(Cor.VERDE + "Bem-vindo(a) ao Jogo da Forca!" + Cor.RESET)

    while tentativas < tentativas_maximas:
        letra = input(Cor.CIANO + "\nDigite uma letra: " + Cor.RESET).lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in letras_corretas:
                print(Cor.VERMELHO + "Você já tendeu essa letra. Tente outra." + Cor.RESET)
            elif letra in palavra_secreta:
                letras_corretas.append(letra)
                print(Cor.VERDE + "Letra correta!" + Cor.RESET)
            else:
                tentativas += 1
                print(Cor.VERMELHO + f"Letra incorreta. Tentativas restantes: {tentativas_maximas - tentativas}" + Cor.RESET)
            
            palavra_atual = exibir_palavra(palavra_secreta, letras_corretas)
            print(Cor.AMARELO + "Palavra atual: ", palavra_atual)

            if palavra_atual == palavra_secreta:
                print(Cor.AZUL + mensagem_fim + Cor.RESET)
                print(Cor.VERDE + "Parabéns! Você acertou a palavra!" + Cor.RESET)
                break
        else:
            print(Cor.AMARELO + "Por favor, digite uma única letra válida." + Cor.RESET)
    if tentativas == tentativas_maximas:
        print(Cor.AZUL + mensagem_fim + Cor.RESET)
        print(Cor.VERMELHO + f"Fim de Jogo! A palavra era: {palavra_secreta}" + Cor.RESET)

if __name__ == "__main__":
    jogar_forca()