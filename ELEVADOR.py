pesomax = 500

pesos_lidos = []
indice_peso = 1
novo_peso = -1

while (novo_peso != 0):
    novo_   peso = int (input("Leia um peso" + str (indice_peso) + ": "))
    pesos_lidos.append(novo_peso)
    indice_peso = indice_peso + 1

soma_pesos = 0
proximo_peso = 0
peso_lido = 0

print (peso_lidos)

while (soma_pesos <= 500):
    
