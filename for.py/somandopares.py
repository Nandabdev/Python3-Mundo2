# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for n in range(1,7):
    num = int(input(f'Digite o {n} número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
    
print(f'Foram usados {cont} números pares, resultado da soma: {soma} ')