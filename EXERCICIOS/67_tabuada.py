while True:
    valor = int(input("Quer ver a tabuada de qual valor? "))
    if valor < 0:
        break
    cont = 1
    if valor > 0:
        while cont <= 10:
            soma = valor * cont
            print(f"{valor} x {cont} = {soma}")
            cont += 1
print("PROGRAMA TABUADA ENCERRADO")
