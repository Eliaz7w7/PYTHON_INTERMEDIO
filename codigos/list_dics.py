def run():
    list=["hello",1,True]
    dic= {"Nombre":"Elias", "Apellido":"Auque"}

    super_list= [
    {"Nombre":"Elias", "Apellido":"Auque"},
    {"Nombre":"Cristian", "Apellido":"Domingez"},
    {"Nombre":"Jazmin", "Apellido":"Aguilar"},
    {"Nombre":"Harry", "Apellido":"Potter"}
    ]

    super_dic={
        "num_nat":[1,2,3,4,5],
        "letras":["a","b","c","d"],
        "flotantes":[1.2,2.5,3.5],
    }

    #IMPRIMIR DICCIONARIO
    for key, values in super_dic.items():
        print(key, values)
    print()
    #IMPRIMIR LISTAS
    for i in super_list:
        print(i.values())



if __name__=="__main__":
    run()