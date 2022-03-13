def multip(num):
    a = []
    for i in range(1, num+1):
        if num % i == 0:
            a.append(i)
    return a


def run():

    num = int(input("Ingrese un nufamero: "))
    print(multip(num))


if __name__ == "__main__":
    run()