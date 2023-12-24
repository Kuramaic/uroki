#1
# x=[1,43,2,5,67,3]
# y=[4,5,3,4,2,56]
# c=[]
# for i in range(len(x)):
#     m=[]
#     m.append(x[i])
#     m.append(y[i])
#     c.append(m)
# print(c)

#2
# a=['Аутист', 'Наркоман', 'Алкоголик', 'ДЦП', 'Клоун']
# def privet(a):
#     for i in a:
#         print('Привет! '+i)
# privet(a)


# 3
# def dooble(a):
#     m=[]
#     for i in range(len(a)):
#         m.append(a[i])
#     print(m)
#     for i in range(len(m)-1):
#         if m[i]==m[i+1]:
#             return True
#     return False
# print(dooble('popajopaa'))

#4
# a="hgkg      bffjhggkhg       ejfejf        efaf;i"
# while "  " in a:
#     a=a.replace("  "," ")
# print(a)

#5
# from math import pi
# r,h,p=map(int,input('r h p ').split())
# s= pi*(r^2)
# o= h*s
# m=o*p
# print (round(m,2))

#6
# a = "2, 45, 35, 546, 231"
# a="2, 45, 35, 546, 231".split(", ")
# a=map(int,a)
# a=list(a)
# n=1
# for i in a:
#     n=n*i
# print(n)

#7
# a=[[1,2,3],[4,5,6],[7,8,9]]
# s=1
# m=0
# for i in a:
#     for j in i:
#         s*=j
#     m+=s
#     s=1
# print(m)


#8
# a={
#     'x':30,
#     'y':32
# }
# b={
#     'x':50,
#     'y':20
# }
# x=b['x']-a['x']
# y=b['y']-a['y']
# n=(x**2+y**2)**0.5
# print(n)

#9
# def nedohacer(a):
#     while "а" in a: 
#         a=a.replace("а","4")
#     while "е" in a: 
#         a=a.replace("е","3")
#     return a
# print(nedohacer("аывалорплваоплрваолрлорареваеыаеывеаывеаа"))


#10
# def mass(m):
#     n=[]
#     g=0
#     for i in m:
#         g+=i
#         n.append(g)
#     return n
# print(mass([1,2,3]))

#11
# def up(m):
#     if m[0]<m[1]:
#         return True
#     return False
# print(up([1,2,3]))

#12
