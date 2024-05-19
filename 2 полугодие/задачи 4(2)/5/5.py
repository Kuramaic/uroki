import csv
m=[]
with open('C:/Users/user/Desktop/проги/COdes/uroki/2 полугодие/задачи 4(2)/2/5.csv') as a:
    reader=csv.reader(a, delimiter=';')
    for row in reader:
       m.append(row[1])
ans=[]
for i in range(len(m)):
    if m[i].isdigit():
        ans.append(int(m[i]))
print(sum(ans))