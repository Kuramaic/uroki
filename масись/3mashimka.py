# m=[]
# n=[]
# def get_car():
#     global n
#     a=int(input('Введите номер машины '))
#     n.append(a)
#     b=input('Введите марку машины ')
#     n.append(b)
#     c=input('Введите цвет машины ')
#     n.append(c)
#     return n
#     n=[]



# while True:
#     print('1.Добавить машину')
#     print('2.Найти машину по номеру')
#     print('3.Закрыть')
#     a=int(input('Введите номер операции '))
#     if a==1:
#         while True:
#              get_car()
#              m.append(n)
#              n=[]
#              f=input('Вы хотите закончить ввод? YES/NO ')
#              if f=='YES':
#                  break
#     elif a==2:
#         while 1:    
#             number=int(input('Введите номер машины которую хотите найти '))
#             for i in m:
#                 if i[0]==number:
#                     print(str(i[0])+' '+i[1]+' '+i[2])
#                     break
#                 else:
#                     print('Машины с таким номером нет')
#                     break
#             break
#     elif a==3:
#         print('ПОКА!')
#         break


