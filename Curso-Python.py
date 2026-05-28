## Exercícios de Curso em Vídeo (Gustavo Guanabara)
## Mundo 1
# ex001.py

print('Olá Mundo!')

# ex002.py

x = input('Digite algo: ')

print('O tipo de dado informado é: ', type(x))
print('Tem espaços vazios no dado informado?' , x.isspace())
print('É um número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está com letas maiusculas?', x.isupper())
print('Está com letras minusculas?', x.islower())
print('Está capitalizada?', x.istitle())

# ex003.py

x = int(input('Digite um número: '))

a = x - 1
s = x + 1

print(f'O número digitado foi: {x} o antercessor do número digitado é: {a} e o seu sucessor é: {s}')

# ex004.py

x = float(input('Digite um número: '))

dobro = x * 2
triplo = x * 3
raiz = x ** (1/2)

print(f'O dobro do número digitado é: {dobro}')
print(f'O triplo do número digitado é: {triplo}')
print(f'A raiz quadrada do número digitado é: {raiz:.2f}')

# ex008.py

metros = float(input('Digite um valor em metros: '))

cm = metros*100
mm = metros*1000

print(f'O valor digitado em Centímetros é: {cm}cm')
print(f'O valor digitado em Milímetros é: {mm}mm')

km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10

print(f'O valor informado em Decímetro é: {dm}dm')
print(f'O valor informado em Quilômetro é: {km}km')
print(f'O valor informado em Hectômetro é: {hm}hm')
print(f'O valor informado em Decâmetro é: {dam}dam')

# ex009.py

x = int(input('Digite um número inteiro para ver a sua tabuada: '))
print('-'*12)
print('{} x {:2} = {}'.format(x, 1, x*1))
print('{} x {:2} = {}'.format(x, 2, x*2))
print('{} x {:2} = {}'.format(x, 3, x*3))
print('{} x {:2} = {}'.format(x, 4, x*4))
print('{} x {:2} = {}'.format(x, 5, x*5))
print('{} x {:2} = {}'.format(x, 6, x*6))
print('{} x {:2} = {}'.format(x, 7, x*7))
print('{} x {:2} = {}'.format(x, 8, x*8))
print('{} x {:2} = {}'.format(x, 9, x*9))
print('{} x {:2} = {}'.format(x, 10, x*10))
print('-'*12)

# ex010.py

real = float(input('Quanto reais você deseja converter em dólares? R$'))

dolar = real / 3.27

print(f'O valor digitado de reais em dólares é: {dolar:.2f}U$')

# ex011.py

altura = float(input('Digite o valor em metros da altura da parade: '))
largura = float(input('Digite o valor em memtros da largura da parede: '))

area = altura * largura

print(f'A Área em metros quadrados da parede é {area}')

tinta = area / 2

print(f'A quantidade de litros de tinta necessários para pintar a parede será de: {tinta} litros')

# ex012.py

preço = float(input('Qual é o valor do produto? R$: '))
desconto = float(input('Qual é a porcentagem desconto? %:'))
novo = preço - (preço * desconto/100)
print('O preço inicial do produto R${:.2f}, com o desconto de {:.2f}%, sairá por R${:.2f}'.format(preço, desconto, novo))

# ex013.py

salario = float(input('Insira o seu salário inicial R$: '))
reajuste = salario + (salario * 15/100)
print('O seu salário inicial de {:.2f}R$, com o reajuste de 15%, ficará {:.2f}R$.'.format(salario, reajuste))

# ex014.py

cels = float(input('Informe a temperatura em °C: '))
temp = (cels * 9/5 + 32)
print('A temperatura de {:.1f} °C, na conversão fica {:.1f}°F'.format(cels, temp))

# ex015.py

p = float(input('Informe a Quilômetragem porcorrida pelo carro Km: '))
d = int(input('Informe a quantidade de dias de alugel do carro: '))

kmdcd = (p * 0.15) + (d * 60)

print('O valor que deverá ser pago pelo alugel e quilometragem do carro é {:.2f} R$ '.format(kmdcd))

# ex016.py

# import math
# from math import trunc

num_real = float(input('Digite um valor Real: '))

print('O número digitado foi {} e sua porção inteira {:.0f}'.format(num_real, num_real))
# print('O número digitado foi {} e sua porção inteira {}'.format(num_real, math.trunc(num_real))
# print('O número digitado foi {} e sua porção inteira {}'.format(num_real, trunc(num_real))

# ex017.py

# cateto_op = float(input('Digite o valor do Cateto Oposto: '))
# cateto_adj = float(input('Digite o valor do Cateto Adjacente: '))
# hipo = (cateto_op ** 2 + cateto_adj ** 2) ** (1/2)
# print(f'O valor da Hipotenusa do triângulo retangulo é {hipo)}')

from math import hypot

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hi = hypot(co, ca)
print(f'A Hipotenusa vai medir {hi:.2f}')

# ex018.py

from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo qualquer: '))

seno = sin(radians(angulo))
print(f'O angulo {angulo} tem o SENO de {seno:.2f}')

cosseno = cos(radians(angulo))
print(f'O angulo {angulo} tem o COSSENO de {cosseno:.2f}')

tangente = tan(radians(angulo))
print(f'O angulo {angulo} tem a TANGENTE de {tangente:.2f}')

# ex019.py

import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto anulo: '))

lista = [aluno1, aluno2, aluno3, aluno4]
sorte = random.choice(lista)
print(f'O aluno sorteado foi: {sorte}')

# ex020.py

import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto anulo: '))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem dos alunos para a apresentação será: {lista}')

# ex021.py

import pygame
pygame.init()
pygame.mixer.music.load('hojeanoite.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

# ex022.py

"""frase = 'Lucas tu precisa melhorar'
print(frase.replace('melhorar', 'mudar'))"""

nome = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('O seu nome em letras minúsculas é {}'.format(nome.lower()))
print('O seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
completo = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(completo[0], len(completo[0])))

# ex023.py

num = int(input('Digite um número de 0 à 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cent}')
print(f'Milhar: {mil}')

# ex024.py

cidade = str(input('Digite da sua cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')

# ex025.py

nome = str(input('Digite o seu Nome Completo: ')).strip()
print('SILVA' in nome.upper())

# ex026.py

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aperece na posição {}'.format(frase.rfind('A'+1)))

# ex027.py

nome = str(input('Digite o seu nome completo: ')).title().strip()
completo = nome.split()
print(f'O seu primeiro nome é {completo[0]}')
print(f'O seu ultimo nome é {completo[len(completo)-1]}')

# ex028.py 

from random import randint
from time import sleep
sort = randint(0, 5)
print('~=~' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar qual vai ser...')
print('~=~' * 20)
numb = int(input('Digite um número inteiro entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if numb == sort:
    print('PARABÉNS! Você venceu, consegui adivinhar o número corretamente.')
else:
    print('Você perdeu! Você não conseguiu adivinhar o número...')

# ex029.py

velo = float(input('Digite a velocidade do seu carro em Km/h: '))

if velo > 80:
    multa = velo - 80
    custo = multa * 7
    print(f'O seu carro passou pela lombada eletrônica na velocidade {velo} e o custo da multa é de {custo:.2f}R$')
else:
    print('O seu carro passou pela lombada eletrônica em uma velocidade permitida.')

# ex030.py

numb = int(input('Digite um número inteiro: '))
div = numb % 2
if div == 1:
    print(f'O número digitado foi {numb} e ele é um número Impar.')
else:
    print(f'O número digitado foi {numb} e ele é um número Par.')

# ex031.py

distancia = float(input('Digite a distância da viagem que você deseja fazer em Km: '))
if distancia <= 200:
    valor = distancia * 0.50
    print(f'O valor da sua viagem sairá por R$ {valor:.2f}')
else:
    promo = distancia * 0.45
    print(f'O valor da sua viagem, com desconto, sairá por R$ {promo:.2f}')

# valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45

# ex032.py

ano = int(input('Digite uma ANO, para saber se ele é um ano BISSEXTO: '))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano informado é um ano BISSEXTO.')
else:
    print(f'O ano informado não é um ano BISSEXTO.')

# ex033.py

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior número informado.')
if n1 < n2 and n1 < n3:
    print(f'O número {n1} é o menor número informado.')
if n2 > n1 and n2 > n3:
    print(f'O número {n2} é o maior número informado.')
if n2 < n1 and n2 < n3:
    print(f'O número {n2} é o menor número informado.')
if n3 > n1 and n3 > n2:
    print(f'O número {n3} é o maior número informado.')
if n3 < n1 and n3 < n2:
    print(f'O número {n3} é o menor número informado.')

# ex034.py

salario = float(input('Informe o seu salário em R$: '))

if salario >= 1.250:
    reajuste10 = salario + (salario * 10/100)
    print(f'O seu salário de {salario:.2f} R$, será reajustado em 10% e ficará em {reajuste10:.2f} R$.')
else:
    reajuste15 = salario + (salario * 15/100)
    print(f'O seu salário de {salario:.2f} R$, será reajustado em 15% e será {reajuste15:.2f} R$.')

# ex035.py

lado1 = float(input('Digite o valor de uma 1° reta: '))
lado2 = float(input('Digite o valor de uma 2° reta: '))
lado3 = float(input('Digite o valor de uma 3° reta: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
# if (lado1 <= lado2 or lado1 <= lado3) and (lado2 <= lado1 or lado2 <= lado3) and (lado3 <= lado2 or lado3 <= lado1):
# print('ERRO! O valores informados não formam um triângulo...')
# else: print(f'Os valores informados {lado1},{lado2} e {lado3} formam um triângulo')
    print('Os lados informados formam um triângulo.')
else:
    print('Os lados informandos não formam um triângulo.')

# ex036.py

casa = float(input('Digite o valor da sua casa em R$: '))
salario = float(input('Digite o seu salário em R$: '))
prestacao = float(input('Digite em quantos ano você deseja financiar a casa: '))
parcela = casa / (prestacao * 12)
limite = (salario * 30/100)

if limite >= parcela:
    print('O valor da sua prestação mensal será R$.')
else:
    print('O seu salário atual não te permite financiar a casa com as parcelas desejadas.')

# ex037.py

numb = int(input('Digite um número inteiro: '))
base = int(input('Digite a base de conversão:'
                 '\n1 para BINÁRIO'
                 '\n2 para OCTADECIMA'
                 '\n3 para HEXADECIMAL'
                 '\nEscolha uma das opções: '))
if base == 1:
    print(f'O valor BINÁRIO do número digitado é: {bin(numb)[2:]}.')
elif base == 2:
    print(f'O valor OCTADECIMAL do número digitado é: {oct(numb)[2:]}.')
elif base == 3:
    print(f'O valor HEXADECIMAL do número digitado é: {hex(numb)[2:]}.')
else:
    print('ERRO. Você não digitou as informações corretamente.')

# ex038.py

pv = int(input('Digite o primeiro valor: '))
sv = int(input('Digite o segundo valor: '))

if pv > sv:
    print(f'O primeiro valor {pv} é maior do que o segundo valor {sv}.')
elif sv > pv:
    print(f'O segundo valor {sv} é maior do que o primeiro valor {pv}.')
elif pv == sv:
    print(f'Os valores digitados {pv} e {sv} são iguais.')
else:
    print('ERRO. Digite valores válidos.')

# ex039.py

from datetime import date
hoje = date.today().year
nasc = int(input('Digite em que ano você nasceu: '))
idade = hoje - nasc
print(f'Quem nasceu no ano de {nasc} tem {idade} em {hoje}.')
if idade == 18:
    print('Você está no ano do seu ALISTAMENTO.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já PASSOU do prazo, o seu ALISTAMENTO já ocorreu em {saldo}')
    alista = hoje + saldo
    print(f'O seu ALISTAMENTO foi em {alista}')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não está no tempo de realizar o ALISTAMENTO, ele ocorrerá em {saldo}.')
    alista = hoje + saldo
    print(f'O seu ALISTAMENTO será em {alista}')

# ex040.py

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2) / 2

if media <= 5:
    print(f'Você está reprovado! A sua média é: {media:.1f}')
elif media > 5 and media <= 6.9:
    print(f'Você está de recuperação! A sua média é: {media:.1f}')
else:
    print(f'PARABÉNS você foi APROVADO! A sua média é: {media:.1f}')

# ex041.py

nascimento = int(input('Digite o seu ano de nascimento: '))
ano = 2022 - nascimento
if ano <= 9:
    print(f'A sua idade é {ano} e a sua categoria é MIRIM.')
elif ano <= 14:
    print(f'A sua idade é {ano} e a sua categoria é INFANTIL')
elif ano <= 19:
    print(f'A sua idade é {ano} e a sua categoria é JUNIOR.')
elif ano <= 20:
    print(f'A sua idade é {ano} e a sua categoria é SENIOR.')
else:
    print(f'A sua idade é {ano} e a sua categoria é MASTER.')

# ex042.py

lado1 = float(input('Digite o valor de uma 1° reta: '))
lado2 = float(input('Digite o valor de uma 2° reta: '))
lado3 = float(input('Digite o valor de uma 3° reta: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado3:
    print('O lados informados formam um triângulo.')
    if lado1 == lado2 and lado1 == lado3:
        print(f'O triangulo formado pelos lados {lado1}, {lado2} e {lado3} é um triangulo EQUÍLATERO.')
    elif lado1 != lado2 and lado1 != lado3:
        print(f'O triangulo formado pelos lados {lado1}, {lado2} e {lado3} é um triangulo ESCALENO.')
    else:
        print(f'O triangulo formado pelos lados {lado1}, {lado2} e {lado3} é um triangulo ISÓSCELES.')
else:
    print('Os lados informandos não formam um triângulo.')

# ex043.py

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / altura ** 2

if imc <= 18.5:
    print(f'O seu IMC é {imc:.2f} e você está abaixo do peso ideal.')
elif imc > 18.5 and imc <= 24.9:
    print(f'O seu IMC é {imc:.2f} e você está no peso ideal.')
elif imc > 25 and imc <= 29.9:
    print(f'O seu IMC é {imc:.2f} e você está com sobrepeso.')
elif imc > 30 and imc <= 40:
    print(f'O seu IMC é {imc:.2f} e você está com obesidade.')
else:
    print(f'O seu IMC é {imc:.2f} e você está com Obesidade Morbida. Procure um Médico.')

# ex044.py

print('{:=^40}'.format(' LOJAS ALEMIDA '))
valor = float(input('Digite o valor do produto em R$: '))
print('''Formas de PAGAMENTO
[ 1 ] à vista no dinheiro com 10% de desconto
[ 2 ] no cartão com 5% de desconto
[ 3 ] 2x no cartão com o preço normal
[ 4 ] 3x ou mais no cartão com 20% de juros''')
metodo = int(input('Informe o método de pagameto: '))
if metodo == 1:
    print(f'O valor do produto com 10% de desconto, fica por: {valor - (valor * 10/100):.2f}')
elif metodo == 2:
    print(f'O valor do produto com 5% de desconto, fica por: {valor - (valor * 5/100):.2f}')
elif metodo == 3:
    print(f'O valor será parcelada em 2x {valor / 2:.2f}, porém sem desconto no final.')
elif metodo == 4:
    parcela = int(input('Digite o total de parcelas que você deseja fazer: '))
    novopreço = valor + (valor * 20/100)
    totalparcela = novopreço / parcela
    print(f'O valor receberá um acrescimo de 20% de juros, ele sairá por: {totalparcela:.2f} ')

# ex045.py

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÔES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESROURA''')
jogador = int(input('Qual é sua jogada? '))
print('=-=' * 10)
print(f'O Computador escolheu {itens[computador]}')
print(f'O Jogador escolheu {itens[jogador]}')
print('=-=' * 10)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O JOGADOR VENCEU!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('ERRO! Jogada INVALIDA.')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O JOGADOR VENCEU!')
    else:
        print('ERRO! Jogada INVALIDA.')
elif computador == 2:
    if jogador == 0:
        print('O JOGADOR VENCEU!')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('ERRO! Jogada INVALIDA.')

# ex046.py

from time import sleep
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print('BOOM!!! Começou o estourar dos fogos de artifícios!')

# ex047.py

for intervalo in range(2, 51, 2):
    print(intervalo)
print('Acabou.')

# ex048.py

soma = 0
contador = 0
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        soma += contador
        contador += 1
print(contador, soma)

# ex049.py

nume = int(input('Digite um número positivo inteiro: '))
for c in range(1, 11):
    print(nume, c, nume*c)

# ex050.py

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite {c} número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} PARES e a soma desses números foi {soma}.')

# ex051.py

valor = int(input('Digite um valor: '))
razao = int(input('Digita um valor para a razão: '))

for c in range(1, 11):
    pa = valor + (c - 1) * razao
    print(pa)

# ex052.py

num = int(input('Digite um número: '))
for c in range(1, num+1):
    if c % num == 0:
        print(f'O número {num} é PRIMO.')
    else:
        print(f'O número {num} não é PRIMO')
print('Ele só é divisivel por 1 e por ele mesmo.')

# ex053.py

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Palindromo')
else:
    print('Não é')

# ex054.py

from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nasci = int(input('Digite o seu ano de nascimento: '))
    idade = atual - nasci
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Ao todo temos {totalmaior} pessoas mairores de idade.')
print(f'Ao todo temos {totalmenor} pessoas menores de idade.')

# ex055.py

maiorpeso = 0
menorpeso = 0

for pessoa in range(1, 6):
    peso = float(input(f'O peso da {pessoa}° pessoa em Kg é: '))
    if pessoa == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'O maior peso registrado foi {maiorpeso}Kg.')
print(f'O menor peso registrado foi {menorpeso}Kg.')

# ex056.py

somaidade = 0
mediaiadade = 0
maioridadehomem = 0
nomevelho = 0
totalmulher20 = 0
for pessoa in range(1, 5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    somaidade += idade
    if pessoa == 1 and sexo == 'M': #if pessoa == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
mediaiadade = somaidade / 4
print(f'A idade média do grupo é {mediaiadade}.')
print(f'O nome do homem mais velho é {nomevelho} e sua idade é {maioridadehomem}.')
print(f'O total de mulheres com idade menores de vinte anos é {totalmulher20}.')

# ex057.py

sexo = str(input('Digite o seu Sexo [F/M]: ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('ERRO. Digite o seu sexo de forma correta, [F/M]: ')).upper()[0].strip()
print(f'Seu sexo é {sexo}, obrigado pela informação.')

# ex058.py

from random import randint
from time import sleep
computador = randint(0, 10)
print('Vou pensar em um número entre 0 e 10, tente adivinhar qual vai ser...')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Digite um número inteiro entre 0 e 10: '))
    print('PROCESSANDO...')
    sleep(1)
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior...')
        elif jogador > computador:
            print('Tente um número menor...')
print(f'PARABÉNS, Você venceu! Seu total de tentativas foi: {tentativas}.')

# ex059.py

v1 = int(input('Digite o 1° Valor: '))
v2 = int(input('Digite o 2° valor: '))
opção = 0
while opção != 5:
    print('''
    [ 1 ] Somar os valores
    [ 2 ] Multiplicar os valores
    [ 3 ] Qual é o maior número
    [ 4 ] Adicionar número
    [ 5 ] Fechar o programa''')
    opção = int(input('Digite uma das opções: '))
    if opção == 1:
        soma = v1 + v2
        print(f'A soma dos valores informados é {soma}.')
    elif opção == 2:
        produto = v1 * v2
        print(f'A multiplicação dos valores informados é {produto}.')
    elif opção == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print(f'O maior valor digitado entre {v1} e {v2}, é {maior}.')
    elif opção == 4:
        print('Digite os novos valores.')
        v1 = int(input('Digite o novo primeiro valor: '))
        v2 = int(input('Digite o novo segundo valor: '))
    elif opção == 5:
        print('Obrigado por utilizar o meu programa.')
print('Volte sempre.')

# ex060.py

n = int(input('Digite um número para ser fatorado: '))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print(f)

# ex061.py

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da P.A.: '))
termo = primeiro
contador = 1
while contador <= 10:
    print(termo, end='')
    termo += razão
    contador += 1

# ex062.py

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da P.A.: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} => ', end='')
        termo += razão
        contador += 1
    print('Calculado.')
    mais = int(input('Você quer calcular mais termos? Digite a quantidade: '))
(print(f'Total de termos foi {total}.'))

# ex063.py

numeros = int(input('Quantos termos você quer mostrar: '))
termo1 = 0
termo2 = 1
print(f'{termo1} > {termo2}', end='')
contador = 3
while contador <= numeros:
    termo3 = termo1 + termo2
    print(f' > {termo3} ', end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print('FIM.')

# ex064.py

numero = contador = soma = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número [999 para parar]: '))
print(f'Você digiou {contador} números e a soma entre eles foi {soma}.')

# ex065.py

resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    resposta= str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quantidade
print(f'FIM {numero}, {media}.')
print(f'O maior foi {maior} e o menor foi {menor}')

# ex066.py

soma = contador = 0
num1 = int(input('Digite um número inteiro: '))
while True:
    num = int(input('Digite um número inteiro, Caso queira parar digite 999: '))
    if num == 999:
        break
    contador += 1
    soma += num
    
print(f'Você digitou {contador} números e a soma de todos eles foi: {soma + num1}.')

# ex067.py

# Exercicio 067

print('---'*30)
print(' - Programa da Tábuada - ')
print('---'*30)

def tabuada(valor):
    print('-'*30)
    print(f'{valor} x 1 = {valor*1}')
    print(f'{valor} x 2 = {valor*2}')
    print(f'{valor} x 3 = {valor*3}')
    print(f'{valor} x 4 = {valor*4}')
    print(f'{valor} x 5 = {valor*5}')
    print(f'{valor} x 6 = {valor*6}')
    print(f'{valor} x 7 = {valor*7}')
    print(f'{valor} x 8 = {valor*8}')
    print(f'{valor} x 9 = {valor*9}')
    print(f'{valor} x 10 = {valor*10}')
    print('-'*30)


while True:
    numero = int(input('Digite um número para ver a sua tábuada [Digite um número NEGATIVO para interromper o programa]: '))
    if numero > 0:
        tabu = tabuada(numero)
    else:
        print('O programa foi interrompido.')
        break

# ex068.py

import random
from time import sleep


print('---'*30)
print(' - Jogo do Par ou Ímpar - ')
print('---'*30)

def jogar(valor):
    div = valor // 2
    if div == 0:
        return True
    else:
        return False

ganhou = 0
jogadas = 0
inicio = print('O jogo vai começar!')
print('Fazendo a sua jogada...')
sleep(2)
jogo = jogar(random.randint(1,2))
if jogo == True:
    ganhou += 1
    jogadas += 1
    print('Você GANHOU essa rodada.')
elif jogo == False:
    print('Você PERDEU na primeira rodada... Tente novamente.')

while True:
    contiuar = str(input('Quer continuar a jogar? [S/N]: ')).strip().upper()
    if contiuar == 'S':
        sleep(2)
        jogo = jogar(random.randint(1,2))
        if jogo == True:
            ganhou += 1
            jogadas += 1
            print('Você GANHOU essa rodada.')
        elif jogo == False:
            jogadas += 1
            print('Você PERDEU nessa rodada.')
            print(f'Você fez um total de {jogadas} jogadas e o seu total de vitórias foi: {ganhou}')
            break
    elif contiuar == 'N':
        print(f'Você decidiu parar. Você fez um total de {jogadas} jogadas e o seu total de vitórias foi: {ganhou}')
        break

# ex069_1.py

totalMaioresIdade = totalH = totalM20 = totalPessoas = 0

while True:
    nome = str(input('Digite o nome da pessoa a ser cadastrada: ')).upper()
    sexo = str(input('Digite o SEXO da pessoa a ser cadastrada [F/M]: ')).strip().upper()[0]
    idade = int(input('Digite a IDADE da pessoa a ser cadastrada: '))
    totalPessoas += 1
    if idade >= 18:
        totalMaioresIdade += 1
    if sexo == 'M':
        totalH += 1
    elif sexo == 'F' and idade < 20:
        totalM20 += 1
    try:
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    finally:
        if opcao == 'S':
            continue
        else:
            print(f'O total de PESSOAS CADASTRADAS foi: {totalPessoas}')
            print(f'O total de pessoas MAIORES DE IDADE, cadastradas foi: {totalMaioresIdade}')
            print(f'O total de pessoas do SEXO MASCULINO, cadastradas foi: {totalH}')
            print(f'O total de pessoas do SEXO FEMININO MENORES DE 20 ANOS, cadastradas foi: {totalM20}')
            break

# ex069_2.py

# Exercício 069


print('---'*30)
print(' - Cadastro de Pessoas - ')
print('---'*30)

def cadastro(n, s, i):
    dados = dict()
    chave = dados['nome']
    dados[chave] = {
        'nome': n,
        'sexo': s,
        'idade': i
    }
    return dados

contadorCadastro = 0
while True:
    nome = str(input('Digite o nome da pessoa a ser cadastrada: ')).upper()
    sexo = str(input('Digite o SEXO da pessoa a ser cadastrada [F/M]: ')).strip().upper()[0]
    idade = int(input('Digite a IDADE da pessoa a ser cadastrada: '))
    cadastros = cadastro(nome, sexo, idade)
    contadorCadastro += 1
    opcao = input('Deseja cadastrar outra pessoa? [S/N]').strip().upper()[0]
    if opcao == 'S':
        nome = str(input('Digite o nome da pessoa a ser cadastrada: ')).upper()
        sexo = str(input('Digite o SEXO da pessoa a ser cadastrada [F/M]: ')).strip().upper()[0]
        idade = int(input('Digite a IDADE da pessoa a ser cadastrada: '))
        cadastros = cadastro(nome, sexo, idade)
        contadorCadastro += 1
    else:
        break
    for c in cadastros['idade']:
        idadeTotal = c
        if idade > 18:
            maioresIdade = idadeTotal
    for i in cadastros['sexo']['M']:
        sexoM = i
    for y in cadastros['sexo']['F']:
        sexoF = y
        for x in cadastros['idade']:
            menoresIdade = x            
print(maioresIdade)
print(sexoM)
print(menoresIdade)

# ex070.py

print('---'*30)
print('\n- LISTA DE PRODUTOS - \n')
print('---'*30)

def listaP(nome, valor):
    lista = []
    dicionario = {
        'produto': nome,
        'preço' : valor
    }
    lista.append(dicionario)
    return lista

totalGasto = 0
produto1000 = 0
menorProduto = 0

while True:
    produto = str(input('Informe o produto: '))
    preço = float(input('Informe o preço do produto: '))
    cadastro = listaP(produto, preço)
    totalGasto += preço
    if preço >= 1000:
        produto1000 += 1
    if menorProduto <= preço:
        menorProduto = preço
    try:
        opcao = str(input('Quer continuar a cadastrar os produtos? [S/N]: ')).strip().upper()[0]
    finally:
        if opcao == 'S':
            continue
        else:
            print(totalGasto)
            print(produto1000)
            print(menorProduto)
            print(cadastro)
            break

# ex071.py

print('---'*30)
print(' - CAIXA ELETRÔNICO - ')
print('---'*30)

def caixa(valor):
    valorTotal = valor
    maiorCedula = 50
    contador = 0
    
    while valorTotal > maiorCedula:
        contador += 1
        if valorTotal >= 50:
            c50 = valorTotal // 50
            contador += 50
            valorTotal -= 50
            if c50 != 0:
                return (f'Notas de 50 Reais = {c50}')
        elif valorTotal == 20 or 40:
            c20 = valorTotal // 20
            contador += 20
            if c20 != 0:
                return (f'Notas de 20 Reais = {c20}')
        elif valorTotal == 10:
            c10 = valorTotal // 10
            contador += 10
            if c10 != 0:
                return (f'Notas de 10 Reais= {c10}')
        elif valorTotal < 10:
            c1 = valorTotal
            contador += 1
            if c1 != 0:
                return (f'Notas de 1 Real = {c1}')

while True:
    try:
        sacar = int(input('Digite o valor a ser sacado [O caixa só aceita valores inteiros]: '))
    finally:
        saque = caixa(sacar)
        print(saque)
        break
        
# ex072.py

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
)

print('---'*30)
print(' - NÚMERO POR EXTENSO - ')
print('---'*30)

numero = int(input('Digite um número entre 0 e 20: '))
if numero >= 0 and numero <= 20:
    print(f'Você digitou o número: {tupla[numero]}')

# ex073.py

# Exercício 073


tuplaTabela = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athetico-PR', 'Atlético-MG', 'América-MG',
'Goiás', 'Santos', 'Bragantino', 'Botagofo', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Coritiba', 'Cuiabá', 'Avai',
'Juventude', 'Atlético-GO', 'Juventude')

print('---'*30)
print(' - TABELA CAMPEONATO BRASILEIRO DE FUTEBOL - ')
print('---'*30)
opcao = int(input('\
| 1 | Os 5 Primeiros colocados\n\
| 2 | Os 4 Últimos colocados\n\
| 3 | Listar todos os times em ordem alfabética\n\
| 4 | Em que posição está o seu time\n\
Selecione uma opcões: \
'))

if opcao == 1:
    print(f'Os Cinco Primeiros colocados são: {tuplaTabela[0:5]}')
elif opcao == 2:
    print(f'Os Quatro Últimos colocados são: {tuplaTabela[-4:]}')
elif opcao == 3:
    ordLista = sorted(tuplaTabela)
    print(f'A ordem alfabética dos times da Série A, é: {ordLista} ')
elif opcao == 4:
    time = str(input('Digite o nome do seu Clube: ')).capitalize()
    if time in tuplaTabela:
        times = tuplaTabela.index(time)+1
        print(f'O seu Time está, atualmente, na {times}° posição do Campeonato Brasileiro')
    else:
        print('Não foi possível encontrar o seu Time.')

# ex074.py

from random import randint

tupla = (
randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
)
listaNumeros = []

for c in tupla:
    listaNumeros.append(c)
print(f'Os números sorteados foram: {listaNumeros}')
print(f'O maior número sorteado foi: {max(tupla)}')
print(f'O menor número sorteado foi: {min(tupla)}')

# ex075.py

print('---'*30)
print(' - ARMAZENADOR DE NÚMERO - ')
print('---'*30)

tupla = tuple()
numero1 = int(input('Digite o 1° número: '))
numero2 = int(input('Digite o 2° número: '))
numero3 = int(input('Digite o 3° número: '))
numero4 = int(input('Digite o 4° número: '))
tuplaFinal = (*tupla, numero1, numero2, numero3, numero4)

if 9 in tuplaFinal:
    n9 = tuplaFinal.count(9)
    if n9 == 1:
        print(f'O número 9, apareceu {n9} vez')
    else: 
        print(f'O número 9, apareceu {n9} vezes')
if 3 in tuplaFinal:
    print(f'O número 3 apareceu pela 1° na posição {tuplaFinal.index(3)+1}')
for c in tuplaFinal:
    num = c 
    if num % 2 == 0:
        print(f'{num} é Par')
    else:
        print(f'{c} é Impar')

# ex076.py

tuplaProdutos = tuple()
lista = dict()

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o preço do produto: '))
    lista = dict()
    lista = {
        'produto': produto,
        'preço': preco
    }
    tuplaProdutos = lista
    opcao = input('Quer continuar a cadastrar Produtos? [S/N]').strip().upper()[0]
    if opcao == 'S':
        continue
    else:
        print(tuplaProdutos)
        break

# ex077.py

palavras = ('APRENDER', 'PROGRAMAR', 'LUTAR', 'CONQUISTAR', 'DEFENDER', 'PYTHON', 'VITORIA')

vogais = 'AEIOU'
f = ''

for c in palavras:
    print(f'\nNa palavra {c}, temos as vogais: ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra, end='')

# ex078.py

print('---'*30)
print(' - ARMAZENADOR DE NÚMEROS - ')
print('---'*30)

listaFin = list()
listaIni = list()
while True:
    for c in range(5):
        num = int(input(f'Digite o {c}° valor: '))
        listaIni.append(num)
        listaFin = listaIni
    listaFin.sort()
    print(f'A lista de números digitados foi: {listaFin}')
    print(f'O MENOR número digitado foi: {listaFin[0]} e sua posição foi {listaIni.index()}')
    print(f'O MAOIR número digitado foi: {listaFin[4]} e sua posição foi {listaIni.index()}')
    opcao = input('Deseja Armazenar novos números? [S/N]: ').strip().upper()[0]
    if opcao == 'S': continue
    else: break

# ex079.py

print('---'*30)
print(' - ARMAZENADOR DE NÚMEROS - ')
print('---'*30)

lista = list()
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    lista.sort()
    opcao = input('Deseja digitar outro número? [S/N]: ').strip().upper()[0]
    if opcao == 'S': 
        continue
    else:
        print(f'Os números digitados, em ordem crescente, foram: {lista}')
        break
    
# ex080.py

print('---'*30)
print(' - LISTAGEM DE 5 NÚMEROS - ')
print('---'*30)

lista = list()

for c in range(5):
    num = int(input(f'Digite {(c)+1}° número: '))
    if num not in lista:
        if c == 0 or num > lista[-1]:
            lista.append(num)
        else:
            for posicao, x in enumerate(lista):
                if num <= x:
                    lista.insert(posicao, num)
                    break
print(lista)

# ex081.py

print('---'*30)
print(' - LISTA DETALHADA DE NÚMEROS - ')
print('---'*30)

lista = []
contador = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    lista.sort(reverse=True)
    contador += 1
    opcao =  input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'S':
        continue
    else:
        print(f'A quantidade de números digitados foi: {contador}')    
        print(f'A lista dos números, em ordem decrescente, é: {lista}')
        if 5 in lista:
            print('O número 5, foi digitado e está contido na lista.')
        else:
            print('O número 5, não foi digitado, portanto, não está na lista.')
        break

# ex082.py
print('---'*30)
print(' - LISTA DE NÚMEROS PARES E ÍMPARES - ')
print('---'*30)

listaGeral = []
listaPar = []
listaImpar = []

while True:
    num = int(input('Digite um número: '))
    listaGeral.append(num)
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'S':
        continue
    else:
        print(f'A lista dos números digitados, é: {listaGeral}')
        print(f'A lista dos números PARES, é: {listaPar}')
        print(f'A lista dos números IMPARES, é: {listaImpar}')
        break

# ex083.py

lista = []
mat = str(input('Digite uma expressão matemática: '))

for simb in mat:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Valida')
else:
    print('Invalida')

# ex084.py

print('---'*30)
print(' - PESSOA E PESO - ')
print('---'*30)

listaGeral = []
listaPessoa = []

while True:
    nome = str(input('Digite o nome da pessoa: ')).capitalize()
    peso = float(input('Digite o peso da pessoa: '))
    listaPessoa.append(nome)
    listaPessoa.append(peso)
    listaGeral.append(listaPessoa)
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'N':
        print(listaGeral)
        break

# ex085.py

print('---'*30)
print(' - LISTA PAR E ÍMPAR - ')
print('---'*30)

listaGeral = []
listaPar = []
listaImpar = []

for c in range(0, 7):
    numero = int(input(f'Digite o {c+1}° número: '))
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
    listaPar.sort()
    listaImpar.sort()    
listaGeral.append(listaPar)
listaGeral.append(listaImpar)
print(f'A listagem dos números PARES foi: {listaGeral[0]}')
print(f'A listagem dos números ÍMPARES foi: {listaGeral[1]}')

# ex086.py

print('---'*30)
print(' - MATRIZ 3x3 - ')
print('---'*30)


matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for i in range(0,3):
    for x in range(0,3):
        matriz[i][x] = int(input(f'Digite um valor para as posições [{i} , {x}]: '))
for i in range(0,3):
    for x in range(0,3):
        print(f' | {matriz[i][x]:^5} | ', end='')
    print()

# ex087.py

print('---'*30)
print(' - MATRIZ 3x3 - ')
print('---'*30)

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somarPar = 0
somaTerceira = 0
maiorLinha = 0
for i in range(0,3):
    
    for x in range(0,3):
        matriz[i][x] = int(input(f'Digite um valor para as posições [{i} , {x}]: '))
        if matriz[i][x] % 2 == 0:
            somarPar += matriz[i][x]        

for i in range(0,3):
    for x in range(0,3):
        print(f' | {matriz[i][x]:^5} | ', end='')
    print()

for d in range(0,3):
    somaTerceira += matriz[d][2]

for c in range(0,3):
    if c == 0:
        maiorLinha = matriz[1][c]
    elif matriz[1][c] > maiorLinha:
        maiorLinha = matriz[1][c]

print(f'A SOMA dos valores PERES, foi: {somarPar}')
print(f'A SOMA dos valores da Tercerira Coluna, é: {somaTerceira}')
print(f'O MAIOR valor digitado na Segunda Linha, foi: {maiorLinha}')

# ex088.py

from random import randint

print('---'*30)
print(' - MEGA SENA - ')
print('---'*30)

def gerarNumeros():
    numeros = []
    # exNum = [1,2,22,39,44,55,57,58,59,60]
    exNum = []
    while len(numeros) < 7:
        numPalpite = randint(1, 60)
        if numPalpite not in exNum:
            if numPalpite not in numeros:
                numeros.append(numPalpite)
    return numeros

cartela = []

while True:
    qntCartelas = int(input('Quantas Cartelas você deseja gerar?: '))
    for c in range(qntCartelas):
        cartela = gerarNumeros()
        cartela.sort()
        print(f'Jogo {c+1}° : {cartela}')
    opc = input('Jogar novamente:').strip().upper()[0]
    if opc == 'S': continue
    else: break

# ex089.py

print('---'*30)
print(' - BOLETIM - ')
print('---'*30)

boletim = []

while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a Primeira Nota: '))
    nota2 = float(input('Digite a Segunda Nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'N': break

print('---'*30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('---'*30)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    num = int(input('Deseja saber as notas de algum aluno? (Digite o número dele): '))
    if num <= len(boletim) -1:
        print(f'As Notas do aluno N° {boletim[num][0]}, são: {boletim[num][1]}')
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N': break

# ex090.py

print('---'*30)
print(' - LISTA DE ALUNOS - ')
print('---'*30)

dados = dict()
lista = []
def dicionario(n,m):
    dados = {
        'nome': n,
        'media': m
    }
    return dados

nome = str(input('Digite o nome do aluno: ')).capitalize()
media = float(input('Digite a média das notas do aluno: '))
dados = dicionario(nome, media)
print(dados['nome'])
print(dados['media'])
if dados['media'] > 6:
    print(f'A situação do Aluno(a) {nome}, é APROVADO.')
else:
    print(f'A situação do Aluno(a) {nome}, é REPROVADO.')

# ex091.py

from random import randint

resultado = {
    'Jogador N° 1' : randint(1, 6),
    'Jogador N° 2' : randint(1, 6),
    'Jogador N° 3' : randint(1, 6),
    'Jogador N° 4' : randint(1, 6),
}

for k, v in resultado.items():
    print(f'O {k} tirou {v}')

ordem = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
print(ordem)

# ex092.py

import datetime

nome = input('Digite o seu Nome: ').capitalize()
ano = int(input('Digite o seu Ano de Nascimento: '))
carteiraTrabalho = int(input('Digite a sua Carteira de Tabralho [Caso não tenha, digite 0]: '))
hoje = datetime.date.today()
anoAtual = hoje.year
idade = anoAtual - ano

ficha = {
    'nome': nome,
    'idade': idade,
    'ctps': carteiraTrabalho
}

if carteiraTrabalho != 0:
    anoContratacao = int(input('Digite o Ano de Contratação: '))
    salario = float(input('Digite quanto é o seu Salário: '))
    anoAposentadoria = 65 - idade
    ficha.update({
        'contratação': anoContratacao,
        'salário': salario,
        'aposentadoria': anoAposentadoria
    })
print(ficha)
print(f'O Seu NOME é {ficha["nome"]}')
print(f'A Sua IDADE é {ficha["idade"]}')
if ficha["ctps"] == 0:
    print('Você ainda não possui uma Carteira de Trabalho.')
else:
    print(f'O NÚMERO da sua Carteira de Trabalho é: {ficha["ctps"]}')
    print(f'O seu ANO DE CONTRACAÇÃO foi: {ficha["contratação"]}')
    print(f'O seu SALÁRIO é: {ficha["salário"]}')
    print(f'A sua APOSENTADORIA acontecerá em: {ficha["aposentadoria"]} anos.')

# ex093.py

lista = []
totalGols = 0
nomeJogador = input('Digite o Nome do Jogador: ').capitalize()
qtdPartidas = int(input('Digite a Quantidade de Partidas que ele jogou: '))
jogador = {
    'nome': nomeJogador,
    'partidas': qtdPartidas
}
for c in range(qtdPartidas):
    qtdGolsPartida = int(input(f'Quantos Gols foram feitos pelo jogador na {c+1}° partida?: '))
    lista.append(qtdGolsPartida)
    totalGols += qtdGolsPartida
jogador.update({'golspartida': lista})
jogador.update({'saldogols': totalGols})

print(jogador["nome"])
print(jogador["golspartida"])
for i, v in enumerate(jogador["golspartida"]):
    print(f'Na partida {i+1} o Jogador fez {v} gols.')
print(jogador["saldogols"])

# ex094.py

lista = []
mulheres = []
pessoas = {}
acimaMedia = []
soma = 0
while True:
    pessoas.clear()
    nome = input('Digite o NOME: ').upper()
    sexo = input('Digite o SEXO [F/M]: ').upper()
    idade = int(input('Digite a sua IDADE: '))
    pessoas = {
        'nome' : nome,
        'sexo': sexo,
        'idade': idade
    }
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    if sexo == 'F':
        mulheres.append(pessoas.copy())
    opcao = input('Deseja continuar adicionando pessoas? [S/N]: ').strip().upper()[0]
    if opcao == 'S': continue
    else: 
        print(lista)
        break

media = soma/len(lista)
if pessoas['idade'] > media:
    acimaMedia.append(pessoas)
print(len(lista))
print(media)
print(mulheres)
print(acimaMedia)

# ex095.py

listaJogadores = []
gols = []
totalGols = 0
while True:
    jogador.clear(0)
    nomeJogador = input('Digite o Nome do Jogador: ').capitalize()
    qtdPartidas = int(input('Digite a Quantidade de Partidas que ele jogou: '))
    jogador = {
        'nome': nomeJogador,
        'partidas': qtdPartidas
    }
    for c in range(qtdPartidas):
        qtdGolsPartida = int(input(f'Quantos Gols foram feitos pelo jogador na {c+1}° partida?: '))
        gols.append(qtdGolsPartida)
        totalGols += qtdGolsPartida
    jogador.update({'golspartida': gols})
    jogador.update({'saldogols': totalGols})
    
    listaJogadores.append(jogador.copy())
    
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'S': 
        continue
    
    else:

        print(jogador["nome"])
        print(jogador["golspartida"])

        for k, v in enumerate(listaJogadores):
            print(f'Na partida {k+1} o Jogador fez {v} gols.')
        print(jogador["saldogols"])
        
        break

# ex096.py

def area(l,c):
    a = l * c
    return a

largura = float(input('Digite a Largura do Terreno: '))
comprimento = float(input('Digite o Comprimento do Terreno: '))

terreno = area(largura, comprimento)
print(f'A área do terreno de {largura} por {comprimento}, tem {terreno:.2f}m².')

# ex097.py

def escreva(txt):
    tamanho = len(txt) +2
    print('-'*tamanho)
    print(f' {txt}')
    print('-'*tamanho)

texto = str(input('Digite um Texto [Palavra/Frase]: '))

saida = escreva(texto)
print(saida)

# ex098.py

def contador(i, f, p):
    print(f'{i} até {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
        print()    

saida = contador(1,10,1)
saida2 = contador(10,0,2)

def contadorP(i, f, p):
    print(f'{i} até {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
        print()

num1 = int(input('Digite o 1° valor: '))
num2 = int(input('Digite o 2° valor: '))
num3 = int(input('Digite o 3° valor: '))

saida3 = contadorP(num1, num2, num3)