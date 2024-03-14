sat = int (input ("digite uma nota entre 0 a 10"))
if sat > 10 or sat < 0:
    print ("valor invalido, digite um valor entre 0 a 10")
    while sat <= 0 or sat >= 10 :
        sat = int (input ("digite uma nota entre 0 a 10"))