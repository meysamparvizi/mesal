import random
chars = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM\!@#$%^&*()_+.,123456789'
tedad=int(input('enter tedad: '))
chandraqmi=int(input('enter raqam: ')) 
for pws in range(tedad):
    password = ''
    for c in range(chandraqmi):
        password += random.choice(chars)
    print (password)
