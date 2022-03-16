#Sobre-escribir archivo
a=[1,2,3,4,5,6,7,8]
with open(".\imagenes\ejm.txt", "w", encoding="utf-8") as f:
    for i in a:
        f.write(str(i)+"\n")


a=[]
#Leer el archivo
with open(".\imagenes\ejm.txt", "r", encoding="utf-8") as f:
    for i in f:
        a.append(int(i))
print(a)


#Escribir archivo (añade al final)
a=[9,10,11,12,13,14]
with open(".\imagenes\ejm.txt", "a", encoding="utf-8") as f:
    for i in a:
        f.write(str(i)+"\n")
        

