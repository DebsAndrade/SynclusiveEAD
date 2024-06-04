def linhas(n_linhas):
    contador = 1
    while contador <= n_linhas:
        print("Linha", contador)
        contador +=1

print("Olá! Sou o contador de Linhas!")
escolha_linhas = int(input("Me diga um número de linhas: "))
linhas(escolha_linhas)

def linhas(n_linhas):
    for contador in range(1, n_linhas + 1):
        print("Linha", contador)

print("Olá! Sou o contador de Linhas!")
try:
    escolha_linhas = int(input("Me diga um número de linhas: "))
    if escolha_linhas < 0:
        print("Por favor, insira um número não negativo.")
    else:
        linhas(escolha_linhas)
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")

