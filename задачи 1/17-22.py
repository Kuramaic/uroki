#17
# def search_substr(subst,st):
#     if st.find(subst)>0:
#         return 'Есть контакт'
#     return 'Мимо'
# print(search_substr('ds','dhgfhfghfghfghdsfghfg'))

#18
# def first_last(letter, st):
#     a=st.find(letter)
#     b=st.rfind(letter)
#     if a>0 and b>0:
#         return (a,b)
#     return (None,None)
# print(first_last('j','kjkjkjlkjljdkljljklkjlkj'))

# #19
# from collections import Counter
# def top3(st):
#     counter_top3 = Counter(st.replace(' ', '')).most_common(3)
#     print(counter_top3)
#     return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])
# top3("fsdjkfksdljfhkjfghgfhnmnvytopotypcxmnvmrpwerwer")
        
#20
# def camel(st):
#     s=''
#     count = 0
#     for i,v in enumerate(st):
#         if v.isalpha():
#             if count%2==0:
#                 s+=v.upper()
#             else:
#                 s+=v.lower()
#             count+=1
#         else:
#             s+=v
#     return s
# print(camel('fdsssssdsdfsdf fgsdfsdf  fsdfsdf'))

#21
# def shortener(st):
#     while '(' in st or ')' in st:
#         l = st.rfind('(')
#         r = st.find(')', l)
#         st = st.replace(st[l:r + 1], '')
#     return st
# print(shortener('fdsffffffffffdsfdsdfsd(fsdsddfsdf) dsfaad (fsdffsd)'))

#22
# def cleaned_str(st):
#     m = []
#     for i in st:
#         if i == '@' and m:
#             m.pop()
#         elif i != '@':
#             m.append(i)
#     return ''.join(m)
# print(cleaned_str('poo@pa joo@pa'))