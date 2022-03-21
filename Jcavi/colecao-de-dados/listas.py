
tupla1 = 45,3,78,12   # imutável, o que define uma tuplas são as virgulas

print(type(tupla1))

# Lista é uma estreutura de dados finita e ordenada 
## Possui indice de memoria,Pode ser mutável(adcionar,remover)

lista_inteiros = [12,56,89,20,52,76] 
# Indice de memória de uma estrutura de dados começa pelo 0

lista_mista = ['morango',23,'uva','tomate',53]

print(lista_mista[2])


lista_frutas = ['morango','uva','maçã','abacate']

lista_frutas.append('jaca')

print(lista_frutas)

del lista_frutas [1]

print (lista_frutas)

lista_mista.extend(lista_inteiros)

print(lista_mista)