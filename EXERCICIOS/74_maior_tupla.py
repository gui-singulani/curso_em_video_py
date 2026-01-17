import random

sorteio = random.sample(range(0, 11), k=5)

numeros = tuple(sorteio)

print(f"Os valores sorteados foram: {numeros}")
print(f"O maior valor sorteado foi: {max(numeros)}")
print(f"O menor valor sorteado foi: {min(numeros)}")
