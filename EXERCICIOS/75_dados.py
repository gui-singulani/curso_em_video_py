n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))
pares = 0
valores = (n1, n2, n3, n4)
print(f"Você digirou os valores {valores}")
print(f"O valor 9 apareceu {valores.count(9)} vezes")
print(f"O valor 3 apareceu na {valores.index(3) + 1}ª posição")
for i in valores:
    if i % 2 == 0:
        pares += 1
print(f"Os valores pares digitados foram {pares}")

# forma feita pelo guanabara:
num = (
    int(input("Digite um número: ")),
    int(input("Digite um número: ")),
    int(input("Digite um número: ")),
    int(input("Digite um número: ")),
)
print(f"Você digitou os valores: {num}")
print(f"O valor 9 apareceu {num.count} vezes")
if 3 in num:
    print(f"O valor 3 apareceu na posição {num.index(3)+1}")
else:
    print("O valor 3 não foi digitado")
print(f"Os valores pares digitados foram ", end="")
for i in num:
    if i % 2 == 0
        print(n, end="")
