a = float (input ("digite o primeiro lado do tri�ngulo"))

b = float (input ("digite o segundo lado do tri�ngulo"))

c = float (input ("digite o terceiro lado do tri�ngulo"))

chequer = (a + b + c)/c

d = ""

if chequer > 0:
    
	print ("� um tri�ngulo")

    	d = 1

elif chequer < 0:
    
	print ("isso n�o � um tri�ngulo")

if a == b == c and d == 1:

    print ("� um tri�ngulo equilatero")

elif a > b == c or b > a ==c or c > a == b and d == 1:

    print ("� um tri�ngulo is�sceles")

else:

    print ("� um tri�ngulo escaleno")