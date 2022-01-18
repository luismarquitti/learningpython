print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print("Você digitou ", chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if acertou:
    print("Você Acertou!!")
elif maior:
    print("Você Errou!! O seu chute foi maior do que o múmero secreto.")
elif menor:
    print("Você Errou!! O seu chute foi menor do que o múmero secreto.")


print("Fim do Jogo!!")
