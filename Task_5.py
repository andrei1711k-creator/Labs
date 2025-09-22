s=0
n = int(input("Введите число: "))

if n % 7 == 0:
    print("Магическое число!")
else:
   for d in str(abs(n)):
       s = int(d)+s
   print("Сумма цифр:", s)
