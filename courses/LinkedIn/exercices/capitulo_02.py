# Váriaveis e Tipos de Dados

doce = 'chocolate'

# Convenções para nomear as váriaveis
 # Iniiar sempre com letra minúsula;
 # O nome pode ser composto por letras, algarismos e underline;
 # E não podemos usar palavras reservadas do Python, como if, for, from, etc.

# Tipos de Dados
ineiro = 10
decimal = 3.14
complexo = 3 + 4j
simples = 'Ola Mundo!'
duplas = "Ola Mundo!"
triplo = '''Ola 
Mundo!'''
verdadeiro = True
falso = False
type(complexo)
type(simples)

#Estrutura de Dados

lista = []
lista_numeros = [1, 2, 3]
lista_mista = [1, 2, 3, 'Ola Mundo!', True]
len(lista_mista)
tupla = (1, 2, 3)
conjunto_num = {1, 2, 3}
len(conjunto_num)
dicionario = {'a': 1, 'b': 2, 'c': 3}
dicionario['a']

#Operadores Aritméticos
a = 5
b = 2
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
h = a ** b
i = a // b
print(c, d, e, f, g, h, i)

#Operadores Relacionais
a = 5
b = 2
a > b
a < b
a >= b
a <= b
a == b
a != b

#Operadores Lógicos
a = 5
b = 2
c = 3
d = 4
e = a > b and c > d
f = a > b or c > d
g = not a > b

#Operadores de Atribuição
a = 5
a += 2
a -= 2
a *= 2
a /= 2
a **= 2
a //= 2

#estrutura de controle

# if condição:
#     faça isso
# else:
#     faça outra coisa

a ='internet'
lista = ['internet', 'rede', 'wifi', 'cabeada']

if a in lista:
    print('tem internet')
else:
    print('não tem internet')

for palavra in lista:
    print(palavra)

b = 2
while b < 10:
    print(b, 'o número é menor que 10')
    b += 1

#função

print('Ola Mundo')

def multiplicarPorCinco(numero):
    return numero * 5

def somarDoisNumeros(num1, num2):
    return num1 + num2

somarDoisNumeros(1, 2)

def retiraUltimoElemento(lista):
    lista.pop()

centenas = [100, 200, 300]
retiraUltimoElemento(centenas)

#classe de objetos

class Pessoa:
    def __init__(self, nome="Mauro", idade=20):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Oi, meu nome é {self.nome} e tenho {self.idade} anos.")

