import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randint(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if (nivel == 1):
        total_de_tentativas = 15
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}.")
        chute = int(input("Digite um número entre 1 e 100: "))
        if chute < 1 or chute > 100:
            print("Você deve digiar um número entre 1 e 100!")
            continue
        print("Você digitou ", chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Você acertou e fez {pontos}!!")
            break
        elif maior:
            pontos_perdidos = abs(chute - numero_secreto)
            pontos -= pontos_perdidos
            print("Você Errou!! O seu chute foi maior do que o múmero secreto.")
        elif menor:
            pontos_perdidos = abs(chute - numero_secreto)
            pontos -= pontos_perdidos
            print("Você Errou!! O seu chute foi menor do que o múmero secreto.")

    print("Fim do Jogo!!")
    print(f"O número secreto era {numero_secreto}!!")


if __name__ == "__main__":
    jogar()
