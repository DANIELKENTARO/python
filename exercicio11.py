a = float (input ("digite o primeiro lado do triagulo"))

b = float (input ("digite o segundo lado do triangulo"))

c = float (input ("digite o terceiro lado do triangulo"))

chequer1 = b - c
chequer2 = a - c
chequer3 = a - b
d = int (0)
if (chequer1) < a < (b + c) and (chequer2) < b < (a + c) and (chequer3) < c < (a + b) or a == b == c:
    d + 1

if d == 1:
    
	print ("e um triangulo")


elif d == 0:
    
	print ("isso nao e um triangulo")

if a == b == c and d == 1:

    print ("e um triangulo equilatero")

elif a > b == c or b > a ==c or c > a == b and d == 1:

    print ("e um triangulo isosceles")

elif a != b !=c:

    print ("e um triangulo escaleno")
