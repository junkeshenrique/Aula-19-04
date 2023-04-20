nota = float(input('Informe sua média escolar de 0 a 10:'))

if nota == 0:
    print(f'Sua classificação é "Sem rendimento".')
elif nota >= 0.1 and nota <= 2.9:
    print(f'Sua classificação é "Inferior".')
elif nota >= 3.0 and nota <= 4.9:
    print(f'Sua classificação é "Médio Inferior".')
elif nota >= 5.0 and nota <= 6.9:
    print(f'Sua classificação é "Médio".')
elif nota >= 7.0 and nota <= 8.9:
    print(f'Sua classificação é "Médio Superior".')
elif nota >= 9.0 and nota == 10:
    print(f'Sua classificação é "Superior".')
else:
    print(f'A nota irformada não está em 0 e 10 pontos.')