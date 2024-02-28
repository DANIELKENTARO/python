n1 = float (input("digite o primeiro valor"))
n2 = float (input("digite o segundo valor"))
n3 = float (input("digite o terceiro valor"))
if n1 > n2 and n1 > n3:
   print ("o primeiro valor é maior que os outros dois")
elif n2 > n1 and n2 > n3:
    print ("o segundo valor é maior que os outros dois")
elif n3 > n1 and n3 > n2:
    print ("o terceiro valor é maior que os outros dois")
elif n1 == n2 and n1 == n3:
    print ('todos são iguais')