turno = input("digite o horário que você estuda (manhã, tarde, noite)").lower()
if turno == 'manhã' or turno == 'manha':
    print ("Bom dia!")
elif turno == 'tarde':
    print ("Boa tarde!")
elif turno == 'noite':
    print ("Boa noite!")
else:
    print('invalido')