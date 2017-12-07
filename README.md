# Exercises
Snippets from Ziemba lessons

from functools import reduce

lista = range(10)
squared=[]
for i in lista:
  squared.append(i**2)
  
list1= range(10)
squared1=list(map(lambda x:x**2,list1))
print(squared)
print(" ")
print(squared1)

lista2 = range(1,7)
reducedList=reduce(lambda x,y:x*y,lista2)
print(reducedList)
