def run():
    cua=[]
    #Nums elevados al cuadrado en lista
    for i in range(1,101):
        if i%3!=0:
            cua.append(i**2)
    print(cua)

    #Nums elevados al cuadrado con list comprehension
    abc = [i**2 for i in range (1,11) if i %3 != 0]
    print(abc)


    #Solucion al reto de Facundo
    cde = [i for i in range (1,9999) if i%4==0 if i %6 ==0  if i%9 ==0]
    print(cde)


if __name__=="__main__":
    run()



