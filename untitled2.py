def listiok():
    o=[]
    m=[]
    n=int(input('Введите количество элементов '))
    for i in range(n):
        i=float(input('Введите число '))
        o.append(i)
    for i in o:
        if i <5:
            m.append(i)
    print('Число')
        
listiok()