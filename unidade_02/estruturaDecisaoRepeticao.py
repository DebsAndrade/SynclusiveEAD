# Elabore um programa onde seja pedido ao utilizador a quantidade de alunos
# que existem na turma, e de seguida o nome de cada aluno.
# De seguida, o programa tem de dar 'print' ao nome de cada aluno.

numeroDeAluno = int(input("Quantos alunos existem na turma?"))
nomeDosAlunos = []

for i in range(numeroDeAluno):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nomeDosAlunos.append(nome)

print("Os nomes dos alunos são:")
for nome in nomeDosAlunos:
    print(nome)


for i in range(1, 20):
    print(i)

# i += 1 é igual a i = i + 1 incremento ou decremento i = i - 1

i = 0
while i < 10:
    i += 1
    print(i)

direcao = input("Para onde deseja ir? (Lisboa, Porto, Coimbra): ")
if direcao == "Lisboa":
    print("Continue em frente.")
elif direcao == "Porto":
    print("Vire à direita na próxima esquina.")
elif direcao == "Coimbra":
    print("Vire à esquerda na próxima esquina.")
else:
    print("Opção inválida.")