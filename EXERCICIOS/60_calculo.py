n = int(input("Digite um número para ver o seu fatorial: "))
i = n
f = 1
while i > 0:
    print(f"{i}", end="")
    print(" x " if i > 1 else " = ", end="")
    f *= i
    i -= 1
print(f"{f}")
