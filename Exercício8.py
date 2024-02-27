a3 = (input ("Calcular soma, subtração, multiplicação ou divisão?")).lower()
b3 = float (input ("insira o primeiro valor: "))
c3 = float (input ("insira o segundo valor: "))
if a3 == "soma":
    d2 = b3+c3
    print ("soma igual a ", d2)
elif a3 == "subtração":
    e3 = b3 - c3
    print ("subtração igual a ", e3)
elif a3 == "multiplicação":
    f3 = b3 * c3
    print ("multiplicação igual a ", f3)
else:
    g3 = b3 / c3
    print ("divisão igual a ", g3)

