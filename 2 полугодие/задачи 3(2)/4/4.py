import csv

file1 = open("C:/Users/user/Desktop/проги/COdes/uroki/2 полугодие/задачи 3(2)/4/file1.csv", "r")
file2 = open("C:/Users/user/Desktop/проги/COdes/uroki/2 полугодие/задачи 3(2)/4/file2.csv", "r")
file3 = open("C:/Users/user/Desktop/проги/COdes/uroki/2 полугодие/задачи 3(2)/4/file3.csv", "r")

allFiles = []
data1 = file1.read()
data2 = file2.read()
data3 = file3.read()
allFiles.append(data1)
allFiles.append(data2)
allFiles.append(data3)

with open('file.csv', 'w') as file:
    writer = csv.writer(file)
    for row in allFiles:
        writer.writerow(row)
    file.close()

with open("file.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    file.close()
file1.close()
file2.close()
file3.close()