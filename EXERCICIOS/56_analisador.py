i = 0
idades = []
m =

for i in range(1, 2):
    print(f"--- {i}ª pessoa ---")
    nome = str(input("Nome:"))
    idade = int(input("Idade:"))
    sexo = str(input("Sexo [M/F]:")).upper().strip()

idades.append(idade)
media_idade = sum(idades) / len(idades)
print(f"A média de idade do grupo é de {media_idade} anos.")
