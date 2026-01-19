n = cont = soma = 0
n = int(input("Digite um número diferente de 999: "))

while True:
    if n == 999:
        break
    cont += 1
    soma += n
    n = int(input("Digite um número diferente de 999: "))
print(f"Você digitou {cont} números e a soma entre eles foi {soma}.")
