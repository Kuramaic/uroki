inp = open('c:/Users/user/Desktop/проги/COdes/uroki/2 полугодие/задачи 4(2)/2/input.txt','r')
q = [x for x in inp.readline().split()]
m=[]
for i in range(len(q)):
   a=q.count(q[i])
   m.append(i)
print(q[max(m)])
