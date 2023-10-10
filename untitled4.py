def list_sort(a):
    m=[]
    for i in range(len(a)):
        b=max(a)
        a.remove(b)
        m.append(b)
    print(m)
m=[1,4,8,5,67,43,89]
list_sort(m)        

