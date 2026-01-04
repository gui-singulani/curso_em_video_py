n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo Valor: "))
opcao = 0
while opcao != 5:
    print("""[1] Somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")

    opcao = int(input("Qual é a sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} é igual a {soma}.")
    elif opcao == 2:
        produto = n1 * n2
        print(f"A multiplicação de {n1} e {n2} é igual a {produto}.")
    elif opcao == 3:
        if n1 == n2:
            print(f"Os valores são iguais.")
        elif n1 > n2:
            maior = n1
            print(f"O maior número entre {n1} e {n2} é {maior}")
        else:
            maior = n2
            print(f"O maior número entre {n1} e {n2} é {maior}")
    elif opcao == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando!")
    else:
        print("Valor inválido!! Digite outro valor de 1 a 5.")
