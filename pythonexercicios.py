#num1 = int (input ( "digite um número" ) )
#num2 = int (input ("digite o segundo número") )
#soma = num1 + num2
#print ("soma igual a: ", soma)

#nota1 = int (input ("nota 1:"))
#nota2 = int (input ("nota 2:"))
#nota3 = int (input ("nota 3:"))
#nota4 = int (input (" nota 4:"))
#média = (nota1 + nota2 + nota3 + nota4)/4
#print ("média: ", média)

#metros = int(input ('insira uma medida em metros'))
#centimetros =int (metros * 100)
#print ("converção de metros para centimetros:", centimetros)

#quadrado = int (input ('insira o 1 lado do quadrado:'))
#print ("área quadrada do quadrado", quadrado * 2)
#print("o dobro:", quadrado * 4)

# = float (input ("insira temp. em fahrenheit:"))
#conversor = 5 * ((fahrenheit - 32) / 9)
#print ('temp. em celcius', conversor)

#celcius = float (input ('insira temp. em celcius:'))
#covertor = 9 * ((celcius + 32) / 5)
#print ('temp. em fahrenheit', covertor)

pergunta = float (input ('insira o valor do seu salário por hora:'))
pergunta2 = float (input ('insira total de horas trabalhadas por mês:'))
totalbruto = pergunta * pergunta2
print ("total bruto: ", totalbruto)
if (totalbruto<=1412.00):
    inss = totalbruto * 0.075
    ipr = 0
    sindicato = pergunta * 8
    totaldesconto = inss + ipr + sindicato
    print ('salário líquido sem abonos e beneficios computados: ', totalbruto-totaldesconto)
elif (totalbruto>=1412.00 or totalbruto<=2666.68):
    inss = totalbruto * 0.09
    ipr = totalbruto * 0.075
    sindicato = pergunta * 8
    totaldesconto2 = inss + ipr + sindicato
    print ('salário líquido sem abonos e beneficios computados mais ou menos preciso: ', totalbruto-totaldesconto2)
elif (totalbruto>=2666.69 or totalbruto<=4000.03):
    inss = totalbruto * 0.012
    ipr = totalbruto * 0.075
    sindicato = pergunta * 8
    totaldesconto3 = inss + ipr + sindicato
    print ('salário líquido sem abonos e beneficios computados mais ou menos preciso: ', totalbruto-totaldesconto3)
else:
    inss = totalbruto * 0.014
    ipr = totalbruto * 0.075
    sindicato = pergunta * 8
    totaldesconto4 = inss + ipr + sindicato
    print ('salário líquido sem abonos e beneficios computados mais ou menos preciso: ', totalbruto-totaldesconto4)
    