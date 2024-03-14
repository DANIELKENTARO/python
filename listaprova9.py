u = input ("insira um nome")
s = input ("insira sua senha")
ns = input ("insira sua nova senha")
if ns != s:
    print ("aceito")
elif ns == s:
    while ns == s:
        print ("erro")
        ns = input ("insira sua nova senha")
