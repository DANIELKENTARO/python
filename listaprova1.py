n = float (input ("insira a primeira nota (ponto no lugar da virgula)"))
n2 = float (input ("insira a segunda nota(ponto no lugar da virgula)"))
n3 = float (input ("insira a terceira nota(ponto no lugar da virgula)"))
n4 = float (input ("insira a quarta nota(ponto no lugar da virgula)")) 
m = (n + n2 + n3 + n4)/4
if m >= 70.0:
    print(f"aprovado com media {m}.")
elif m <= 70.0:
    print (f"reprovado com média {m}")
elif m == 100.0:
    print (f"provado com distinção, média {m}")