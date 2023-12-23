n = int(input())
a=[100,50,20,10,5,2,1]
print(n)
for x in a:
    print(f'{int(n/x)} nota(s) de R$ {x},00')
    n=n%x
