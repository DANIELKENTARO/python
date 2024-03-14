s = float (input("insira quanto você ganha por hora"))
b = s*220
l = b - (b*0.12 + b*0.05 + b*0.02)
print(f"salário bruto (contando que se trabalhe por 220 horas por mes){b}, e o liquido sendo {l}")