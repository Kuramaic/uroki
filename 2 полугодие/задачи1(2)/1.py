#2
# b=[]
# c=[]
# a='пук пук пук пук пук непук'
# a=a.split()
# for i in range(len(a)):
#     if a[i] in b:
#         c.append(a[i])
#     b.append(a[i])
# for i in range(len(c)):
#     a.remove(c[i])
# a=sorted(a)
# print(a)

#3
# a=1
# b=20
# c=[]
# v=[]
# for i in range(b + 1):
#     if i >=a:
#         c.append(i)

# for i in c:
#        for j in range(2, i):
#            if(i % j==0):
#                break;
#            if(j==i-1):
#               v.append(i)
# print(v)
# s=sum(v)
# print(s)

#4
# a='шалаш'
# for i in range(len(a)):
#     a=a.replace(' ','')
#     a=a.replace('.','')
#     a=a.replace('!','')
#     a=a.replace(',','')
# b=a[::-1]
# if b==a:
#     print('это полиндром')

#5
# import random
# b=random.randint(1,3)
# if b==3:
#     b='бумага'
# if b==1:
#     b='камень'
# if b==2:
#     b='ножницы'
# a=input('ваш ход: ')
# print("компьютер выбрал: ",b)
# if a==b:
#     print('ничья')
# else:
#     if a=='бумага':
#         if b=='камень':
#             print('вы выиграли')
#         else:
#             print('вы проиграли')
#     if a=='камень':
#         if b=='бумага':
#             print('вы проиграли')
#         else:
#             print('вы выиграли')
#     if a=='ножницы':
#         if b=='бумага':
#             print('вы выиграли')
#         else:
#             print('вы проиграли')