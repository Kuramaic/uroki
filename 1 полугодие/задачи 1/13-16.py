#13
# def to_dickt(lst):
#     dicktum=dict()
#     for i in lst:
#         dicktum[i]=i
#     print(dicktum)

# m= [1,23,4,7,5453,0]
# to_dickt(m)


#14
# my_dict = {'first_one': 'we can do it'}
# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)
# biggest_dict(k1=22, k2=31, k3=11, k4=91)
# biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
# print(my_dict)

#15
# def count_it(a):	
#     m=[]
#     dick={}
#     for i in '0123456789':
#         sum=a.count(i)
#         m.append(sum)
    

#16
# from collections import OrderedDict
# dick = OrderedDict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})

# first = list(dick.items())[0]
# last = list(dick.items())[-1]
# dick.move_to_end(key=first[0])
# dick.move_to_end(key=last[0], last=False)

# second = list(dick.items())[1]
# del dick[second[0]]

# dick['new_key']='new_value'

# print(dick)
