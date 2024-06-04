def andar():
    print("Andou uma casa.")

andar()

def correr():
    andar()
    andar()

correr()

def distancia():
    distancia_percorrida = float(input("Quantos metros andou?"))
    return distancia_percorrida

distancia_percorrida = distancia()

print("Débora andou", distancia_percorrida, "metros.")

def vogais():
    print("a, e, i, o, u.")

vogais()

def soma(a, b):
    return a + b

resultado = soma(4, 8)

print(resultado)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Por favor, insira o seu peso em kg: "))
altura = float(input("Por favor, insira a sua altura em metros: "))


imc = calcular_imc(peso, altura)

print(f"O seu IMC é {imc:.2f}")
