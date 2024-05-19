#1
# class Book:
#     def __init__(self, name, avtor):
#         self.avtor = avtor  
#         self.name = name
        
# book1 = Book("Преступление и наказание", "Достоевский")
# book2 = Book("Война и мир", "Толстой")

# print(book1.name +" - "+ book1.avtor)
# print(book2.avtor)

#2
# class Soda:
#     def __init__(self, dobavka):
#         self.dobavka = dobavka 
        
#     def show(self):
#         if self.dobavka == '':
#             print('Обычная газировка')
#         else:
#             print ('газировка', self.dobavka)
            
# soda1 = Soda("dobavka1")
# soda2 = Soda("dobavka2")
# soda3 = Soda("")

# soda2.show()


# #3
# class triangleChecker:
#     def __init__(self, a, b, c):
        
#         self.a = a
#         self.b = b
#         self.c = c
        
#     def is_triangle(self):
#         if type(self.a)==int and type(self.b)==int and type(self.c)==int:
#             if self.a > 0 and self.b > 0 and self.c > 0:
#                 if self.a+self.b > self.c and self.a+self.c > self.b and self.c+self.b > self.a:
#                     print('можно построить треугольник')
#                 else:
#                     print('нельзя построить')
#             else: 
#                 print('с отрицательными числами ничего не выйдет')
#         else:
#             print('нужно вводить только числа')
            
# tre1 = triangleChecker(1,2,3)
# tre2 = triangleChecker(2,2,2)
# tre3 = triangleChecker('u', 'v', 2)
# tre4 = triangleChecker(-3, 4, 5)

# tre4.is_triangle()


#4
# class Nikola:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def show(self):
#         if self.name != 'Николай':
#             print('Я не ' + self.name + ', а Николай' + ". Мне " + self.age)
#         else:
#             print ('Я '+ self.name + ". Мне " + self.age)
            
# name1 = Nikola("Петя",'3')
# name2 = Nikola("Николай", "32")
# name3 = Nikola("Гоша","52")

# name2.show()

#5
# class Biblioteka:
#     def __init__(self,spisok):
#         self.spisok = spisok
        
#     def show(self,book):
#         self.spisok.append(book)
#     def show1(self,book):
#         self.spisok.remove(book) 
#     def poisk(self,book):
#         a=input('введите книгу которую хотите найти: ')
#         for i in self.spisok:
#             if  i==a:
#                 print('книга, которую вы ищете, есть в списке: ',self.spisok)
                
# b=Biblioteka(['Гроза'])
# b.show("Гроkgjg")
# print(b.spisok)


#6
# class Aviakompania:
#     def __init__(self,planes,marshrut):
#         self.planes = planes
#         self.marshrut = marshrut
        
#     def append_s(self,model):
#         print('вы добавили модель:',model)
#         self.planes.append(model)
#         print('получившийся список самолётов:',self.planes)
        
#     def append_m(self,gorod):
#         print('вы добавили город в маршрут:',gorod)
#         self.marshrut.append(gorod)
#         print('получившийся список маршрутов:',self.marshrut)
        
#     def remove_s(self,model):
#         print('вы удалили модель:',model)
#         self.planes.remove(model) 
#         print('получившийся список самолётов:',self.planes)

#     def remove_m(self,gorod):
#         print('вы удалили город:',gorod)
#         self.marshrut.remove(gorod) 
#         print('получившийся список маршрутов:',self.marshrut)    
            
#     def poisk(self):
#         s=[0]
#         a=input('введите модель,которую хотите найти: ')
#         for i in self.planes:
#             if  i==a:
#                 print('модель, котрую вы ищите, есть в этом списке самолётов:',self.planes)
#                 s.append(1)
#             else: 
#                 s.append(0)
#         d=sum(s)
#         if d==0:
#              print('такой модели не найдено')
   
#     def poisk2(self):
#         u=[0]
#         j=input('введите город,который хотите найти: ')
#         for i in self.marshrut:
#             if  i==j:
#                 print('город, котрый вы ищите, есть в этом маршруте:',self.marshrut)
#                 u.append(1)
#             else: 
#                 u.append(0)
#         d=sum(u)
#         if d==0:
#              print('такого города не найдено в маршрутах')             
             
             
# b = Aviakompania(['model1','model2'],['Москва','Казань','Екатеринбург'])
# b.poisk2()


#7
# class Bank:
#     def __init__(self, people, schet, balanse):
#         self.people = people
#         self.schet = schet
#         self.balanse = balanse
        
#     def show_balanse(self):
#         print ('на вашем балансе:  '+self.balanse)
#     def popolnit(self):
#         a=int(input('введите сколько хотите ввести:  '))
#         b=a*0.99
#         c=self.balanse + b
#         print('на вашем балансе:  ',c)
#     def snat(self):
#         r=int(input('введите сколько хотите вывести:  '))
#         t=r*1.01
#         if self.balanse < t:
#             print('на вашем счете недостаточно средств!!!')
#         else:
#             o=self.balanse - t
#             print('на вашем балансе:  ',o)
#             print('вы сняли:  ',r)
        
# name1 = Bank("Петя",'3333',0)
# name2 = Bank("Николай", "3033",3)
# name3 = Bank("Гоша","3022",4500000)

# name2.snat()


#8
# import math
# class Point:
#     def __init__(self, x1,y1,x2,y2):
#         self.x2 = x2
#         self.y2 = y2
#         self.x1 = x1
#         self.y1 = y1
        
#     def rasstoinie(self):
#         a=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
#         print("расстояние между точками -",a)
        
#     def os(self):
#         if self.x1==0:
#             print('точка 1 лежит на оси OY')
#         if self.x2==0:
#             print('точка 2 лежит на оси OY')
#         if self.y1==0:
#             print('точка 1 лежит на оси OX')
#         if self.y2==0:
#             print('точка 1 лежит на оси OX')
     
#     def peremeshenie(self):
#         b=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
#         print("модуль перемещения -",b)
          
# point1 = Point(1,2,5,7)
# point2 = Point(6,0,0,7)

# point2.os()


#9
# class Produkt:
#     def __init__(self, name, zena, N):
#         self.name = name
#         self.zena = zena
#         self.N = N
        
#     def dobavka(self):
#         print('Товара "',self.name,'" -', self.N)
#         a=int(input('введите на сколько хотите увеличить товар:  '))
#         b=self.N + a
#         print('на складе теперь ',b," товар(а)")
    
#     def ybrat(self):
#         print('Товара "',self.name,'" -', self.N)
#         a=int(input('введите на сколько хотите уменьшить товар:  '))
#         b=self.N - a
#         if a>self.N:
#             print('на складе недостаточно товара для уменьшения')
#         else:
#             print('на складе теперь ',b," товар(а)")
#     def cost(self):
#         print('Товара "',self.name,'" -', self.N)
#         g=self.N*self.zena
#         print('общая стоимость товара: ',g)
        
# p1 = Produkt("фломастеры",100,0)
# p2 = Produkt("апельсины", 30,3)
# p3 = Produkt("бутылки",20,4500000)

# p3.cost()


#10
# class Class:
#     def __init__(self,name,age,spisok,marks):
#         self.spisok = spisok
#         self.name = name
#         self.age = age
#         self.marks = marks
        
#     def append(self,urok):
#         self.spisok.append(urok)
#         print(self.spisok)
#         s=int(input('введите оценку по добавленному предмету: '))
#         if s>5 or s<0:
#             print('оценка может быть только от 0 до 5')
#         else:
#             self.marks.append(s)
#             print('оценки по данным предметам: ',self.marks)
        
#     def remove(self,urok):
#         for i in range(len(self.spisok)):
#             if self.spisok[i] == urok:
#                 self.marks.remove(self.marks[i]) 
#         self.spisok.remove(urok) 
#         print(self.spisok)
#         print(self.marks)
        
#     def markses(self):
#         print('все предметы ученика:', self.spisok)
#         s= sum(self.marks)
#         w=s/len(self.marks)
#         print('средний балл студента:',w)        

# b = Class('Петя',23,['математика','русский'],[2,5])

# b.append('литература')


# Лошадь сидит дома, смотрит MTV. Выступает группа, играющая хэви-метал, и гитарист играет удивительное соло.
# Лошадь говорит "это потрясающе, я тоже хочу научиться этому!"
# Лошадь ищет учителя музыки, звонит ему и спрашивает:
# "Привет, я хотела бы научиться играть на гитаре"
# "Конечно," -- отвечает человек по телефону. -- "Просто приходи к нам на урок, чтобы начать занятия"
# "Есть одна проблема," говорит лошадь. "Я лошадь."
# "Не волнуйтесь," говорит человек. "У нас есть новые современные технологии, чтобы учить лошадей. Вы будете играть как профессионал"
# Лошадь и учитель, используя современные технологии, несколько лет, не покладая гитару, занимаются и, наконец, лошадь начинает играть соло.
# Она хочет показать это своим друзьям, поэтому звонит другу-курице.
# "Эй, Цыпленок, приходи ко мне".
# Цыпленок приходит, смотрит, как лошадь играет на гитаре и думает, что это очень здорово.
# Потом они смотрят то самое музыкальное видео, и цыпленок говорит:
# "А ведь и на барабанах здорово стучат. Я хочу научиться также играть"
# Цыплёнок ищет учителя музыки, звонит ему и спрашивает:
# "Привет, я хотел бы научиться играть на гитаре"
# "Конечно," -- отвечает человек по телефону. -- "Просто приходи к нам на урок, чтобы начать занятия"
# "Есть одна проблема," говорит цыпленок. "Я курица"
# "Не волнуйтесь," говорит человек. "У нас есть новые современные технологии, чтобы учить куриц. Вы будете играть как профессионал"
# Курица и учитель, используя современные технологии, несколько лет, не вылезая из-за барабанной установки, занимаются и, наконец, цыпленок начинает лихо стучать на барабанах.
# Цыпленок начинает рубить хэви-металл с лошадью.
# В конце концов, они думают, что чего-то не хватает.
# Они смотрят видео снова и понимают, что им нужен бас-гитарист.
# Они вызывают их друга Корову и показать ей класс.
# Корова думает, что это очень здорово, и хочет научиться играть на бас-гитаре.
# Корова ищет учителя музыки, звонит ему и спрашивает:
# "Привет, я хотела бы научиться играть на бас-гитаре"
# "Конечно," -- отвечает человек по телефону. -- "Просто приходите к нам на урок, чтобы начать занятия"
# "Есть одна проблема," говорит лошадь. "Я корова"
# "Не волнуйтесь," говорит человек. "У нас есть новые современные технологии, чтобы учить коров. Вы будете играть как профессионал"
# Корова и учитель, используя современные технологии, несколько лет, не покладая гитару, занимаются и, наконец, корова начинает играть на бас-гитаре.
# Они начинают играть в общественных местах и однажды их слышит продюсер.
# Он идет к животным и говорит: "Эй, вы, ребята, вы классно играете! Я хотел бы заключить с вами контракт!"
# Группа записывает альбом, выпускает несколько синглов и становится популярной.
# Они едут в мировое турне и зарабатывают кучу денег.
# И прямо перед финальным шоу тура, который должен состояться в Лас-Вегасе, лошади звонят и сообщают, что её мать находится в больнице.
# Лошадь едет к ней, чтобы увидеть ее до начала шоу, в то время как остальная часть группы летит в Лас-Вегас готовиться, настраивать оборудование.
# Но когда лошадь выходит из больницы, ей снова звонят.
# Частный самолет, который перевозил группу и их продюсер упали в океан и никто не выжил.
# Лошадь опустошена.
# Все её лучшие друзья мертвы, она потеряла работу, мама при смерти.
# На глазах у неё слезы, и она решает упиться до смерти.
# Она заходит в бар, присаживается к стойке, подбегает бармен и весело спрашивает:
# "why the long face?"

# Я бы закончил по-другому:
# "Чё такая хмурая? Расслабься"