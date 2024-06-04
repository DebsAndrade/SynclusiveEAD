def linhas(n_linhas):
    contador = 1
    while contador <= n_linhas:
        print("Linha", contador)
        contador +=1

print("Olá! Sou o contador de Linhas!")
escolha_linhas = int(input("Me diga um número de linhas: "))
linhas(escolha_linhas)
