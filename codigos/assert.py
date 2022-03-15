#RETO FACUNDO
a=int(input("Ingrese numero: "))
assert a>=0, "No es un numero"
b=[x for x in range(1,a+1) if a%x==0]
print(b)