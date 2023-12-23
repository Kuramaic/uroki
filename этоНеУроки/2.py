my_dick={}

def biggest_dick():
    global my_dick
    m=['FIRST_ONE']
    n=['WE CaN DO it']
    while 1:
        a=input()
        if a == 'END':
            break
        m.append(a)
        b=input()
        n.append(b)
        print('Vvedite END esli hotite zakonchit vvod')
    my_dick=dict(zip(m,n))
    print(my_dick)
    
biggest_dick()