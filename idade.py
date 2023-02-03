def idade(a,m,d):
    print('-'*50)
    print('Calculadora de idade em dias')
    print('-'*50)
    return (d +(a*365)+(m*30) 'dias.')

a = 0
m = 0
d = 0

a = int(input('Digite a sua idade: '))
while a >= 0:
    m = a*30
    print(f'Você tem {m} meses de vida.')
    d = a*365
    print(f'Você tem {d} dias de vida.')
    break


print(idade(a,m,d))
