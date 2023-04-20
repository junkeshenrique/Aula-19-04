cargo = str(input('Informe seu cargo:'))
horas = float(input('Informe o número de horas trabalhadas:'))
if cargo == 'testador':
    valor = horas * 20.00
    print(f'Receberá o valor de R${valor:.2f}')
elif cargo == 'analista de testes':
    valor = horas * 35.00
    print(f'Receberá o valor de R${valor:.2f}')
elif cargo == 'programador':
    valor = horas * 45.00
    print(f'Receberá o valor de R${valor:.2f}')
elif cargo == 'analista de sistemas':
    valor = horas * 40.00
    print(f'Receberá o valor de R${valor:.2f}')
elif cargo == 'dba':
    valor = horas * 50.00
    print(f'Receberá o valor de R${valor:.2f}')
else:
    print('O cargo informado não está registrado.')