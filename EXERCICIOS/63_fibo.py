print("-" * 20)
print("Sequência Fibonacci")
print("-" * 20)
termo = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print(f"{t1} -> {t2} -> ", end="")
cont = 3

while cont <= termo:
    termo_atual = t1 + t2
    print(f"{termo_atual} -> ", end="")
    t1 = t2
    t2 = termo_atual
    cont += 1

print("Fim!")
