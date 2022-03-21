### Dicionario é uma coleção desordenada de objetos
# representado por chaves {}
### O dicionario utiliza o formato JSON EXAMPLE {'chave': valor} {"id": 1,
#                                                                 "nome": "Ricardo marques" }

### Exemplo de dicionarios

dic01 = {'chave':'valor'}

estados_siglas = {'SC':'Santa Catarina','PR':'Paraná','RS':'Rio Grande do Sul', 'SP':'São Paulo'}

print(estados_siglas)

for d in estados_siglas.values():   #laço iterador, funciona consumindo uma estrutura de dados
    print(d)

for d in estados_siglas.keys():
    print(d)

print(len(estados_siglas))

