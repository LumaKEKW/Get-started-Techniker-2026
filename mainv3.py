while True:
    zahl1 = int(input('Taschenrechner:\nBitte erste Zahl eingeben:'))
    zahl2 = int(input('Bitte zweite Zahl eingeben:'))
    if zahl2 == 0:
        print ('0 ist eine unzulässige Zahl!')
    else:
        rz = input('Und das Rechenzeichen eingeben: / oder * oder + oder -:')
        match rz:
            case '+':
                erg1 = zahl1+zahl2
                print ('Das Ergebnis der Addition lautet:', erg1)
            case '-':
                erg2 = zahl1-zahl2
                print ('Das Ergebnis der Subtraktion lautet:', erg2)
            case '/':
                erg3 = zahl1/zahl2
                print ('Das Ergebnis der Division lautet:', erg3)
            case '*':
                erg4 = zahl1*zahl2
                print ('Das Ergebis der Multiplikation lautet:', erg4)
