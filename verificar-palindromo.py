entrada = input("Digite a frase que deseja verificar se é palíndromo: ")
saida = ""
for letra in entrada:
    if letra == " ":
        saida += letra.strip()
    else:
        saida += letra.lower()
if saida == saida[::-1]:
    print("\"{}\" é palindromo!")
else:
    print("\"{}\" NÃO é palindromo!")
