mydict = {'1':4,'b':55,'c':68}

for key, value in mydict.items():
    print("Key: "+str(key)+"Value: "+str(value))
    print(list(mydict.values()))


lista1=[(x,y) for x in range(1,6) for y in range(x,6)]
key='b' in mydict
print(key)
if  key in mydict:
    print("GG "+str(mydict[key]))


print(list(lista1))

listaaa= []

if not listaaa:
    print("Nie mam zawartości")