primeira = float (input ("digite a primeira nota"))
segunda = float (input ("digite a segunda nota"))
media = (primeira + segunda)/2
if media <= 60.0:
    print (F"reprovado com {media} de media")
elif media <=99.9:
    print (F"aprovado com {media} de media")
elif media == 10:
    print (F"aprovado com distinção. Média {media}")