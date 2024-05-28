import random;

numero_aleatorio = random.randint(1, 10)

palpite = None

while palpite != numero_aleatorio:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

if palpite < numero_aleatorio:
    print("O número é maior.")
elif palpite > numero_aleatorio:
    print("O número é menor.")
else:
    print("Parabéns! Você adivinhou o número.")