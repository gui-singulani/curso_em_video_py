num = 0
total = 0
cont = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    cont += 1
    total += num
    num = int(input("Digite um número [999 para parar]: "))

    if num == 999:
        print(f"Você digitou {cont} números e a soma entre eles foi {(total)}.")
