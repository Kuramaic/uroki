def kalculator():
    
    a,b=map(int, input('Введите два числа ').split())
    c=input("Введите операцию +,-,*,/,^ ")
    if c == '+':
        print(a+b)
    elif c == "-":
        print(a-b)
    elif  c == '/':
        print(a/b)
    elif c == "*":
        print(a*b)
    elif c == '^':
        print(a**b)
        
    
kalculator()