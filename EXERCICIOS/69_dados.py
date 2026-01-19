print("-" * 30)
print("Cadastre uma pessoa: ")
print("-" * 30)
maior = masculino = feminino = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == "M":
        masculino += 1
    if sexo == "F" and idade < 20:
        feminino += 1
    sn = " "
    while sn not in "SN":
        sn = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if sn == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {maior}")
print(f"Ao todo temos {masculino} homens cadastrados.")
print(f"E temos {feminino} mulheres com menos de 20 anos.")
