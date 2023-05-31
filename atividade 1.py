#Objetivo do arquivo: printar qual a posição de um valor da lista


lista=[2,6,1,23,6,8,1]

x=len(lista)

for i in range(x):
   
    
    print(f"O {i+1}º valor da lista é {lista[i]}")

#as listas começam com o primeiro número sendo 0, por isso se printarmos x ficará 7, e se printarmos a lista[x] dará erro pois não há o 8 elemento.