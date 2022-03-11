
from functools import reduce

#LAS MAS IMPORTANTES SON
#FILTER
"""Se usa para eliminar datos innecesarios (datos que no son usados, como si se usara un if)"""
abc=list(filter(lambda x: x%2==0, range(1,11)))
print(abc)

#MAP
"""No elimina datos, se usa en caso de tener un if en el lambda"""
cde=list(map(lambda x: x**2,range(1,11)))
print(cde)

#REDUCE
"""Usa dos variables de un solo iteral(lista), no es necesario usar list()
 y se importa 'from functools import reduce'"""

n=[2,2,2,2,2,2,2,2]
efg=reduce(lambda x,i: x+i,n)
print(efg)