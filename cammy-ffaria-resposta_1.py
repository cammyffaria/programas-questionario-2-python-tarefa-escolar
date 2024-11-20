a = float(input('Digite um número: ').replace (',','.'))
b = float(input('Digite outro número: ').replace (',','.'))

if a > b:
    print(f'O número menor é {b}')
elif b > a:
    print(f'O número menor é {a}')
else:
    print('Os números são iguais')