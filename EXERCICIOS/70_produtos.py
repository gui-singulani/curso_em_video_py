total = m1000 = menor = cont = 0
barato = " "
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço: "))
    cont += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        total += preco
    if preco > 1000:
        m1000 += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if resp == "N":
        break

print(f"O total da compra foi de R${total}.")
print(f"Temos {m1000} produto(s) custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${menor}")
