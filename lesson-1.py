#author: Плуталов Максим Александрович

# Задача-1: Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

x = "Hello"
y = "world"
z = "2020!"
print (x, y, z)

# Задача-2:  Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int (input("Введите количество секунд:  "))
h = time // 3600
m = (time - h * 3600) // 60
s = time - (h * 3600 + m * 60)
print (f'{h} : {m} : {s}')

# Задача-3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.

n = int (input("Введите целое число n:  "))
nn = int (str(n)*2)
nnn = int (str(n)*3)
c=n++nn++nnn
print ('Сумма чисел n+nn+nnn равна', c)

# Задача-4: Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = (int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Самая большая цифра в числе ", max)
        break

# Задача-5: Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль в расчете на одного сотрудника составила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

#Задача - 6: Cпортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input("В первый день спортсмен пробежал в км: "))
b = int(input("Цель спортсмена в км: "))
day = 1
km = a
while km <= b:
        day += 1
        km*= 1.1
print(f"Спортсмен достиг цели на %.d день" % day)
