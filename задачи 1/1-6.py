#1
# m=[1,4,8,8,67,43,89]
# b=[]
# for i in range(len(m) - 1, -1, -1):
#     b.append(m[i])
# print(m)
# print(b)

#2
# def change(a):
#     c=len(a)-1
#     b=a[c]
#     d=a[0]
#     a.pop()
#     a.pop(0)
#     a.append(d)
#     a.insert(0,b)
#     print(a)
# m=[1,4,8,5,67,43,89]   
# change(m)
    
#3
# def to_list():
#     m=[]
#     print('Введите 0 чтобы завершить ввод параметров')
#     while 1:
#         a=int(input('Введите параметр '))
#         if a==0:
#             break
#         else:
#             m.append(a)
#     print(m)
# to_list()        

#4
# def useless(a):
#     m=max(a)
#     s=len(a)
#     print(m//s)
# m=[1,4,8,5,67,43,89]
# useless(m)

#5
# def list_sort(a):
#     m=[]
#     for i in range(len(a)):
#         b=max(a)
#         a.remove(b)
#         m.append(b)
#     print(m)
# m=[1,4,8,5,67,43,89]
# list_sort(m)        

#6
# def all_eq(a):
#     m=[]
#     popa=[]
#     n=len(a[0])
#     for i in a:
#         b=len(i)
#         m.append(b)
#     y=max(m)
#     for i in a:
#         if len(i)<y:
#             i=i+('_'*(y-len(i)))
#             popa.append(i)
#         else:
#             popa.append(i)
#     print(popa)   
# m=['popogpofg','gfdg','df','fgd','tyeryetyeyet','g','gggggg','gsgfg']
# all_eq(m)     
