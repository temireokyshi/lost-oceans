# Função para retirar acentuação (https://wiki.python.org.br/RemovedorDeAcentos)
from unicodedata import normalize


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


# Minha criação daqui para baixo
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
