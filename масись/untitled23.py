def change(a):
    c=len(a)-1
    b=a[c]
    d=a[0]
    a.pop()
    a.pop(0)
    a.append(d)
    a.insert(0,b)
    print(a)
m=[1,4,8,5,67,43,89]   
change(m)
    