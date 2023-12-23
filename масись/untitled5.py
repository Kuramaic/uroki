def all_eq(a):
    m=[]
    popa=[]
    n=len(a[0])
    for i in a:
        b=len(i)
        m.append(b)
    y=max(m)
    for i in a:
        if len(i)<y:
            i=i+('_'*(y-len(i)))
            popa.append(i)
        else:
            popa.append(i)
    print(popa)   
m=['popogpofg','gfdg','df','fgd','tyeryetyeyet','g','gggggg','gsgfg']
all_eq(m)     