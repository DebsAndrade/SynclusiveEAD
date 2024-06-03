def verificar_numero():

    numero = int(input("Por favor, insira um número: "))
    

    if numero > 0:
        print(f"O número {numero} é positivo.")
    elif numero < 0:
        print(f"O número {numero} é negativo.")
    else:
        print("O número é zero.")


verificar_numero()


def verificar_paridade():

    numero = int(input("Por favor, insira um número: "))

    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
        

verificar_paridade()

def verificar_letra():

    letra = input("Por favor, insira uma letra: ").lower()
    

    if len(letra) != 1 or not letra.isalpha():
        print("Entrada inválida. Por favor, insira uma única letra.")
    else:
        vogais = 'aeiou'
        
        if letra in vogais:
            print(f"A letra '{letra}' é uma vogal.")
        else:
            print(f"A letra '{letra}' é uma consoante.")
        

verificar_letra()

def calcular_preco_bilhete():

    idade = int(input("Por favor, insira a sua idade: "))
    

    if idade < 12:
        preco = 5
    elif 12 <= idade <= 18:
        preco = 7
    else:
        preco = 10
        

    print(f"O preço do bilhete de cinema é {preco} euros.")


calcular_preco_bilhete()
