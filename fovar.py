import random

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

def menu():
    while True:
        print(f"{RED}Bem-vindo ao jogo da Forca :)")
        print("---- MENU ----")
        print("1. Jogar contra o PC")
        print("2. Jogar com um amigo")
        print("3. Sair")
        
        escolha = input(f"{YELLOW}Escolha uma opção (1, 2 ou 3): {RESET}")

        match escolha:
            case "1":
                jogador_contra_pc()
            case "2":
                jogador_contra_amigo()
            case "3":
                print(f"{GREEN}Saindo do jogo... Até logo!{RESET}")
                break
            case _:
                print(f"{RED}Erro: Opção inválida.{RESET}")

def jogador_contra_pc():
    palavras = ["abacaxi", "abismo", "abobrinha", "aceleração"]
    palavra = random.choice(palavras)
    jogo(palavra)

def jogador_contra_amigo():
    palavra = input(f"{YELLOW}Digite uma palavra para o seu amigo adivinhar: {RESET}").lower()
    jogo(palavra)

def jogo(palavra):
    letras_erradas = set()
    letras_certas = set()
    erros = 0
    max_erros = 6

    while erros < max_erros:
        imprimir_forca(erros)
        
        palavra_oculta = ''.join([letra if letra in letras_certas else '_' for letra in palavra])
        print(f"{GREEN}Palavra: {palavra_oculta}{RESET}")
        
        letra = input(f"{YELLOW}Digite uma letra: {RESET}").lower()
        
        if letra == "0":
            print(f"{CYAN}Você desistiu!{RESET}")
            break
        
        if len(letra) != 1:
            print(f"{RED}Digite apenas uma letra.{RESET}")
            continue
        
        if letra in letras_certas or letra in letras_erradas:
            print(f"{GREEN}Você já tentou essa letra.{RESET}")
            continue
        
        if letra in palavra:
            letras_certas.add(letra)
        else:
            letras_erradas.add(letra)
            erros += 1
        
        if set(palavra) == letras_certas:
            print(f"{GREEN}Você ganhou! A palavra era: {palavra}{RESET}")
            break
    
    if erros == max_erros:
        imprimir_forca(erros)
        print(f"{RED}Você perdeu! A palavra era: {palavra}{RESET}")

def imprimir_forca(erros):
    partes = [
        f"{RED}  _____\n{RESET}",
        f"{RED} |     |\n{RESET}",
        f"{RED} |     O\n{RESET}" if erros >= 1 else " |\n",
        f"{YELLOW} |    /|\\ \n{RESET}" if erros >= 4 else f"{YELLOW} |     | \n{RESET}" if erros == 2 else f"{YELLOW} |    /| \n{RESET}" if erros == 3 else " |\n",
        f"{YELLOW} |    / \\ \n{RESET}" if erros >= 6 else f"{YELLOW} |    / \n{RESET}" if erros == 5 else " |\n",
        " |\n",
        "_|___\n",
    ]
    print("".join(partes))

menu()

