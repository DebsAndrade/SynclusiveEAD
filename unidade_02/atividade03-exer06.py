def calcular_imc():

    peso = float(input("Por favor, insira o seu peso em kg: "))
    altura = float(input("Por favor, insira a sua altura em metros: "))
    

    imc = peso / (altura ** 2)
    

    if imc < 18.5:
        categoria = "abaixo do peso"
    elif 18.5 <= imc < 24.9:
        categoria = "com peso normal"
    elif 25 <= imc < 29.9:
        categoria = "com sobrepeso"
    else:
        categoria = "obesa"
        

    print(f"O seu IMC é {imc:.2f}. Você está {categoria}.")
    

calcular_imc()
