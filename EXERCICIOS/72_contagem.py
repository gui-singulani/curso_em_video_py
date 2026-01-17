contagem = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)
resp = "S"
while resp in "Ss":
    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        if 0 <= num <= 20:
            print(f"Você digitou o número {contagem[num]}")
            break
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
