def run():
    #Se guardan los numeros divisibles por 3
    abc={}
    for i in range(1,101):
        cde[i]=i**3
    print (abc)

    #Se guardan los numero divisibles por 3 si no es divisible por3
    cde = {}
    for i in range (1,101):
        if i%3!=0:
            cde[i]=i**3
    print(cde)

    #Numeros al cubo por valor usando comprehension
    
    efg={i:i**3 for i in range(1,101) }
    print(efg)

    #Reto facundo
    reto={i:round(pow(i,0.5),2) for i in range(1,1001) }
    print(reto)

if __name__=="__main__":
    run()