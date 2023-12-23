def to_list():
    m=[]
    print('Введите 0 чтобы завершить ввод параметров')
    while 1:
        a=int(input('Введите параметр '))
        if a==0:
            break
        else:
            m.append(a)
    print(m)
    
to_list()        