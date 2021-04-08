wordsnumber = (("", "ciento", "docientos", "trecientos", "cuatrocientos", "quinientos", "seiscientos", "sietecientos", "ochocientos", "novecientos"),
		("", "dieci", "veinti", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"),
        ("cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"))

varwordsnumber = ("",
        ("", ("diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"),("veinte", "ventiuno", "ventidos", "ventitres", "venticuatro", "venticinco", "ventiseis", "ventisiete", "ventiocho", "ventinueve")),
		("", "cien", "mil"),
        ("","millones", "billones", "trillones", "cua...")) #expandible

def ReadNumber(intnumber):#recibe el numero entero y lo lee
    #Divide el numero en tres
    strnumber = str(intnumber)
    for i in range(3):
        if len(strnumber) % 3 == 0:
            strnumber = list(''.join(strnumber.split()))
            temp = list()
            numberstuple = list()
            for number in strnumber:
                temp.append(number)
                if len(temp) == 3:
                    numberstuple.append(temp)
                    temp = list()
            #numberstuple.append(temp)
            del temp
            break
        else:
            strnumber = "0" + strnumber
    del strnumber

    textnumber = ""

    for indicator in range(len(numberstuple)): #loop en los grupos de tres
        texttuplenumber = ""
        #identifica los numeros
        for numberkey in range(len(numberstuple[indicator])):
            if numberkey == 0 and int(numberstuple[indicator][numberkey]) != 0 and int(numberstuple[indicator][numberkey]) == 1 and int(numberstuple[indicator][numberkey+1]) == 0 and int(numberstuple[indicator][numberkey+2]) == 0: #identifica el cien 100
                texttuplenumber = texttuplenumber + " " + varwordsnumber[2][1]
                break
            elif numberkey == 1 and int(numberstuple[indicator][numberkey]) != 0 and int(numberstuple[indicator][numberkey]) <= 2: #excepciones del 10, 20
                texttuplenumber = texttuplenumber + " " + varwordsnumber[1][int(numberstuple[indicator][numberkey])][int(numberstuple[indicator][numberkey+1])]
                break
            elif int(numberstuple[indicator][numberkey]) != 0: #Centenas, Decenas, Unidades
                texttuplenumber = texttuplenumber + " " + wordsnumber[numberkey][int(numberstuple[indicator][numberkey])]
        
        #identifica los miles y millones
        indicator = len(numberstuple)-indicator-1 #inversor
        if indicator % 2 == 0 and indicator != 0:
            texttuplenumber = texttuplenumber + " " + varwordsnumber[3][int(indicator/2)] #añade los millones
        elif indicator != 0: 
            texttuplenumber = texttuplenumber + " " + varwordsnumber[2][2] #añade el mil
        textnumber = textnumber + texttuplenumber
    return textnumber

print(ReadNumber(123213))