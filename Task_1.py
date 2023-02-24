# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

myListLength = int(input("Enter the length of your list "))
myList = []
for i in range(0, myListLength):
    myList.append(random.randint(1, 100))
print(myList)

number = int(input("Enter the number you looking for "))
counter = 0
deltaMin = abs(myList[0] - number)
closest = myList[0]
for num in myList:
    if num == number:
        counter += 1
    delta = abs(num - number)
    if delta < deltaMin:
        deltaMin = delta
        closest = num
if counter != 0:
    print(f"Your number was found {counter:^5} times in the list ")
else:
    print(f"Your number is not in the list, but the closest is {closest:^5}")
