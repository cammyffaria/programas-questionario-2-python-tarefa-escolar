try:
    idade = int(input('Digite sua idade: '))

    if idade >= 18:
        print('Você pode assinar a documentação')
    elif idade < 18:
        print('A documentação precisa ser assinada por seu responsável legal')
except ValueError:
    print('Idade inválida')
