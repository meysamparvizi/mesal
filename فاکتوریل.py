def factorial(a):
    '''فاکتوریل'''
    javab =1
    for i in range(1,a+1):
        javab = javab * i
    return javab
print (factorial(int (input('enter number: '))))




#تابع بازگشتییی
def factorial(a):
    '''فاکتوریل'''
    if a == 1:
        return 1
    else:
        return (a * factorial(a-1))
print (factorial(int(input ('enter number: '))))
