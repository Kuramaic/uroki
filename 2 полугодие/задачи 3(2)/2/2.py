import csv
def main():
    with open('C:/Users/user/Desktop/проги/COdes/uroki/2 полугодие/задачи 3(2)/2/2.csv', encoding="utf-8") as a:
        reader=csv.reader(a)
        for row in reader:
            print (row)
main()

# я хз чо он не работает просто с названием файла, поетому весь путь ему дал
