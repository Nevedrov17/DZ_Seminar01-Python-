x = int(input("Введите номер четверти: "))
if x == 1:
    print("X от 0 до +&\nY от 0 до +&")
elif x == 2:
    print("X от 0 до -&\nY от 0 до +&")
elif x == 3:
    print("X от 0 до -&\nY от 0 до -&")
elif x == 4:
    print("X от 0 до +&\nY от 0 до -&")
else: print("Такой четверти нет")