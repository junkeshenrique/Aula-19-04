num = int(input('Informe um número:'))

if num > 0:
    raiz = num ** (1/2)
    print(f'A raiz quadrada de {num:.0f} é de {raiz:.0f}')
elif num < 0:
    quadrado = num ** 2
    print(f'O quadrado de {num:.0f} é de {quadrado:.0f}')
else:
    print(f'O número é 0.')