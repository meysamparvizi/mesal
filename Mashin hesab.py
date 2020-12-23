def mashinhesab():
    number1=int(input('enter number 1: '))

    amale = input(''' yeki az amaliat haro bezan
    +
    -
    *
    /
       ''')

    number2=int(input('enter number 2: '))
    
    if amale == '+':
        print (number1+number2)
    elif amale == "-":
        print (number1-number2)
    elif amale =='*':
        print (number1*number2)
    elif amale =="/":
        print (number1/number2)
    else:
        print ('amale entekhab shode sahih nis')
    dobare()

def dobare ():
    mashinhesab_dobare = input(''' age mikhai dobare hesab koni Y bezan
    age nemikhay N bezan
    ''')
    if mashinhesab_dobare == 'Y':
        mashinhesab()
    elif mashinhesab_dobare == 'N':
        print ('bay bay')
    else:
        dobare()

mashinhesab()
