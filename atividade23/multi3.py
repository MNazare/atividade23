# Exercício Python 23: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0

for i in range(1, 501):
    if i % 3 == 0:
        print (i)
        soma =+ i
    
print(f"a soma é igual a {soma}")