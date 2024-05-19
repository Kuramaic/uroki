#7
# def to_float(num):
#     if isinstance(num, (int, float)):
#         return float(num)
#     return "Невозможно преобразовать"
# print(to_float(50))


#8
# def avg_5(a,b,c,d):
#     sum= a+b+c+d
#     avg= sum/4
#     return round(avg,5)
# print(avg_5(123136731,222213134,32217,42139))


#9
# def mul_to_int(a, b):
#     g=a*b
#     if g==int(g):
#         return int(g)
#     return g
# print(mul_to_int(2,3.56))


#10
# from math import pi
# def radius(V):
#     return round(((3*V/(4*pi))**(1/3)),4)
# print(radius(50))

#11
# def dislike_6(a):
#     if (type(a) is int or type(a) is float) and a==6.0:
#         return 'Только не 6!'
#     else:
#         return True
# print(dislike_6(3))


#12
# def help_bool(letter):
#     if letter == 'к':
#         return 'A or B=B or A  A and B=B and A'
#     elif letter == 'а':
#         return 'Прикол'
#     elif letter == 'д':
#         return 'Анекдот'
#     elif letter == 'м':
#         return 'Шутеечка'
# print(help_bool('а'))