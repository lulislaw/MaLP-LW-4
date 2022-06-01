import collections

word = str(input("enter to finish: "))
lista = []
lista.append(word)
while word != "":
    word = str(input("enter to finish: "))
    lista.append(word)

lista = list(collections.OrderedDict((k,None) for k in lista).keys())

for i in range(len(lista)):
    print(lista[i])