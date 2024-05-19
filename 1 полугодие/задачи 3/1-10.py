# #1
# a=input()
# b=input()
# if a==b:
#     print('Draw')
# else:
#     if a=='paper':
#         if b=='rock':
#             print('1 Won!')
#         else:
#             print('2 Won!')
#     if a=='rock':
#         if b=='paper':
#             print('2 Won!')
#         else:
#             print('1 Won!')
#     if a=='scissors':
#         if b=='paper':
#             print('1 Won!')
#         else:
#             print('2 Won!')


#2
# def money(m):
#     n=len(m)/3
#     if n==int(n):
#         return 'DA'
#     return 'He'
# print(money(['popa', 'popa', 'popa', 'popa', 'popa', 'popa'])) 

#3
# def popa(s):
#     s=s.split()
#     sum=0
#     for i in s:
#         if i.isdigit():
#             sum+=int(i)
#     return sum
# print(popa('a 56 m 7 g y r g 6 v r 44 y'))  


#4
# def Black_Jeck(m):
#     s=0
#     for i in m:
#         s+=i
#     if s>21:
#         return True
#     return False
# print(Black_Jeck([20]))

#5
# def oR(s):
#     while "??" in s: 
#         s=s.replace("??","?")
#     while "!!" in s: 
#         s=s.replace("!!","!")
#     return s
# print(oR('sdjh sjdvb jsdhv ???????!!!!!!!!'))

#6
# def plus(s):
#     for i in range (len(s)):
#         if i%2==0 and s[i]=='+':
#             return True
#     return False
# print(plus('a+b+c+d'))

#7
# def sus(time):
#     time=time[0:len(time)+1:-1]
#     if time[1]=='A':
#         return time[0:len(time)+1:-1]
#     if time[1]=='P':
#         time=time[0:len(time)+1:-1]
#         opa=time.find(':')
#         popa=int(time[0:opa])+12
#         return str(popa)+time[opa+1:]
# print(sus('9:00PM'))

#8
# def num(popa):
#     m=[]
#     if popa>=100:
#         m.append(["сто","двести","триста","четыреста","пятьсот","шестьсот","семьсот","восемьсот","девятьсот"][popa//100-1])
#         popa=popa%100
#     if popa>=10:
#         if popa<20:
#             m.append(["десять","одиннадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"][popa%10])
#             popa=0
#         else:
#             m.append(["двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяносто"][popa//10-2])
#             popa=popa%10
#     if popa >= 1:
#         m.append(["один","два","три","четыре","пять","шесть","семь","восемь","девять"][popa-1])
#     if not m:
#         m.append("ноль")
#     return ' '.join(m)
# print(num(89))

#9
# popa = 10
# def lucky(s):
#     n=s//2
#     f=n*popa
#     a=(f+1)*[0]
#     a[0]=1
#     for n in range(1+n):
#         for i in range(min(f, n*(popa - 1)),0,-1):
#             a[i]=sum(a[ max(0,i+1-popa):i+1])
#     return sum(x**2 for x in a )
# print(lucky(3))

    
