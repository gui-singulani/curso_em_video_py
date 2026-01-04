import datetime as date

i = 0
cont = 0


for i in range(1, 7):
    ano = int(input(f"Ano de nascimento da {i}ª pessoa: "))
    idade = date.datetime.now().year - ano
    if idade >= 18:
        cont += 1
print(f"Ao todo tivemos {cont} pessoas maiores de idade")
print(f"E também tivemos {i - cont} pessoas menores de idade")
