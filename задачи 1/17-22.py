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

#19

def top3(st):
    m=[]
    alfavit='абвгдеёжзиёклмнопрстуфхцчшщьыъэюя'
    for i in alfavit:
        
        