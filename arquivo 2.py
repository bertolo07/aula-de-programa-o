#Objetivo: Criar um programa que printe os numeros de uma lista e, depois, eles multiplicados por 2
#Bonus: Colocar os numeros multiplicados em uma outra lista e printa-la


lista=[2,3,7,12,2]
multiplicados = []
multiplicados = [4,6,14,24,4]


for numero in lista:
    print(numero)  # imprime o número atual
    print(numero * 2)  # imprime o número atual multiplicado por 2

    multiplicados.append(multiplicados)  # adiciona o número multiplicado à nova lista

print(multiplicados)  # imprime a lista com os números multiplicados
