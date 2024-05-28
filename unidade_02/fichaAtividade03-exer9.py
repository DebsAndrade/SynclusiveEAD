import random

opcoes = ["pedra", "papel", "tesoura"]

opcao_computador = random.choice(opcoes)

opcao_usuario = input("Escolha entre pedra, papel ou tesoura: ")

print(f"O computador escolheu: {opcao_computador}")

if opcao_usuario == opcao_computador:
    print("Empate!")
elif opcao_usuario == "pedra" and opcao_computador == "tesoura":
    print("Você venceu!")
elif opcao_usuario == "papel" and opcao_computador == "pedra":
    print("Você venceu!")
elif opcao_usuario == "tesoura" and opcao_computador == "papel":
    print("Você venceu!")
else:
    print("Você perdeu!")

print("Obrigado por jogar!")
