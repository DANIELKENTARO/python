#exercicio 1
a = float (input ("digite um numero:"))
if a < 0:
    print ("numero menor que 0")
elif a == 0:
    print ("numero igual a 0")
else:
    print ("numero maior que 0")
#exercicio 2
b = int (input ("digite um de 1 a 10:"))
if b == 2 or b == 4 or b == 6 or b ==8 or b == 10:
    print ("numero par")
else:
    print("numero inpar")
#exercicio 3
i = 10
while i >= 0:
    print(i)
    i -= 1
#exercicio 4

import random
numero = random.randint(1, 10)
palpite = 0
num_tentativas = 0
while numero != palpite:
 if palpite < numero:
    print('digite um numero maior')
    palpite = int (input("digite um numero entre 1 a 10"))
    num_tentativas += 1
 elif palpite > numero:
    print("digite um numero menor")
    palpite = int (input("digite um numero entre 1 a 10"))
    num_tentativas += 1
 elif numero == palpite:
    print(f"parabens voce acertou com {num_tentativas} tentativas")

#exercicio 5
menu = ["iniciar", "sair"]
seletor = ""
while menu:
    seletor = (input ("iniciar ou sair?").lower())
    if seletor == "iniciar":
        print ("não implementado")
    elif seletor == "sair":
        print ("tchau")
        break