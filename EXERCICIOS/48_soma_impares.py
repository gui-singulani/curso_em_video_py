soma = 0
cont = 0

for i in range(1, 501):
    if i % 3 == 0 and i % 2 == 1:
        cont = cont + 1
        soma += i

print(
    f"A soma de todos os {cont} números ímpares múltiplos de 3 entre 1 e 500 é: {soma}"
)
