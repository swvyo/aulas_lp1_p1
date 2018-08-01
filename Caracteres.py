deslocamento = int (input("Valor do deslocamento "))

a = [9, 7, 2, 8, 1, 6, 0]

tamanho = len(a)

'''for i in range (deslocamento % tamanho, tamanho + deslocamento):
    indice = i % tamanho
    print (a [indice])'''

quantidade = len(a)
contador = 0
while (contador < quantidade):
		indice = (deslocamento + contador) % tamanho
		print(a[])
		contador = contador + 1
