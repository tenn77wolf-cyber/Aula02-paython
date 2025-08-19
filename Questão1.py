palavra = input("Digite uma palavra: ")
tamanho = len(palavra)
divisao = tamanho / 3

resultado_arredondado = round(divisao, 2)
print(f"A palavra '{palavra}' tem {tamanho} letras.")
print(f"O resultado da divisão do tamanho por 3 é: {resultado_arredondado}")