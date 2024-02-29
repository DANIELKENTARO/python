n1 = float (input("digite o primeiro valor"))
n2 = float (input("digite o segundo valor"))
n3 = float (input("digite o terceiro valor"))
if n1 > n2 and n1 > n3 and n2 > n3:
    print (f"{n1}, {n2}, {n3}")
elif n1 > n2 and n1 > n3 and n3 > n2:
    print (f"{n1}, {n3}, {n2}")
elif n2 > n1 and n2 > n3 and n1 > n3:
    print (f"{n2}, {n1}, {n3}")
elif n2 > n1 and n2 > n3 and n3 > n1:
    print (f"{n2}, {n3}, {n1}")
elif n3 > n1 and n3 > n2 and n1 > n2:
    print (f"{n3}, {n1}, {n2}")
elif n3 > n1 and n3 > n2 and n2 > n1:
    print (f"{n3}, {n2}, {n1}")