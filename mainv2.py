name = input('Bitte Namen eingeben:')
zahl = int(input('Bitte eine Zahl zwischen 1 und 4 eingeben:'))
match zahl:
    case 1:
        print ("Hallo "+name)
    case 2:
        print ("Moin "+name)
    case 3:
        print ("Hola "+name)
    case 4:
        print ("Servus "+name)
