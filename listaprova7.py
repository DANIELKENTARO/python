sa = float (input ("digite o salario:"))
if sa <= 280:
    print (f"salario anterior:{sa}, salario reajustado para {sa*1.25}, com aumento de 25%")
elif sa <= 700:
    print (f"salario anterior:{sa}, salario reajustado para {sa*1.22}, com aumento de 22%")
elif sa <= 1500:
    print (f"salario anterior:{sa}, salario reajustado para {sa*1.20}, com aumento de 20%")
elif sa >=1501:
    print (f"salario anterior:{sa}, salario reajustado para {sa*1.05}, com aumento de 5%")