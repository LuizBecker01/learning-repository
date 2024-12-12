#string

texto = 'Ola Mundo!'

texto[0]
texto[2:5]
texto[:5]
texto[5:]
texto.lower()
texto.upper()
texto.title()
texto.capitalize()

from datetime import datetime
print(f'Hoje é {datetime.now()}')

a = 10
b = 20
print('A divisão de {} por {} é {:.2f}'.format(a, b, a / b))

#Numericos

type(10)
type(3.14)
a = 2 + 3
type(a)
int(3.14)
round(3.14, 2)

0.1 + 0.1 + 0.1 -0.3

from decimal import *
d = Decimal('0.10')
e = Decimal('0.30')
f = d + d + d - e
print(f'O Resultado é {f}')

#booleanos

#True
#False

minha_lista = [3, 6, None, 21]

if bool(minha_lista) == True:
    print('Minha lista nao é vazia')

for item in minha_lista:
    if item:
        print(f'{item} é valido')
    else:
        print(f'{item} nao é valido')


clima_bom = True
tenho_guardaChuva = False

if not clima_bom or tenho_guardaChuva:
    print('Vou ficar em casa')
else:
    print('Vou sair de casa')