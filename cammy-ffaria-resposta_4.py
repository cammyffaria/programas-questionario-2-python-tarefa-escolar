a = float(input('Digite sua primeira nota: ').replace (',','.'))
b = float(input('Digite sua segunda nota: ').replace (',','.'))
media = (a + b) / 2

if media == 10:
    print(f'Média',media,'Aprovado com distinção')
elif media >= 7:
    print(f'Média', media, 'Aprovado')
else:
    print(f'Média', media, 'reprovado')