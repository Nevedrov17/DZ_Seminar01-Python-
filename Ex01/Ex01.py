a = int(input("Является данный день недели выходным?\nВведите число: "))
if a > 5 and a <=7 and a >=1:
    print ("да")
elif a < 6:
    print("нет")
else: print("Такого дня недели не существует")