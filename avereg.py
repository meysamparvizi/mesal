n=int(input('enter numers dars: '))
a= []
for i in range (0,n):
    x = float(input(f'enter numbers nomre {i+1}: '))
    a.append(x)

avg=sum(a)/n

print('is avaerg: ' , round(avg,2))