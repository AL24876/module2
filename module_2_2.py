first = int(input("Выберите число: "))
second = int(input("Выберите число: "))
thrid = int(input("Выберите число: "))
if first == second and second == thrid and thrid == first :
    print(3)
elif first != second and second != thrid and thrid != first :
    print(0)
elif first == second or second == thrid or thrid == first :
    print(2)
else:
    print("Error")