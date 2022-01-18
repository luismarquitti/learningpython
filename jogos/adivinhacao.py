print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

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
        print("Você Acertou!!")
        break
    elif maior:
        print("Você Errou!! O seu chute foi maior do que o múmero secreto.")
    elif menor:
        print("Você Errou!! O seu chute foi menor do que o múmero secreto.")


print("Fim do Jogo!!")
