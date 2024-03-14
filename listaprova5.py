n1 = int (input ("insira um numero"))
n2 = int (input ("insira um numero"))
n3 = int (input ("insira um numero"))
if n1 > n2 and n1 > n3:
    print (f"{n1} e maior do que os outros dois")
elif n2 > n1 and n2 > n3:
    print (f"{n2} e maior do que os outros dois")
elif n3 > n1 and n3 > n2:
    print (f"{n3} e maior do que os outros dois")
