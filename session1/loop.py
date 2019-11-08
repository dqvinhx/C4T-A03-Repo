
# from random import randint

# your_num = randint(1, 100)


# while True:
#     print('Số bạn đang nghĩ là', your_num)
#     num = your_num
#     b = input('Câu trả lời của bạn là ')
#     if b is 'c':
#         print('Số đó là', your_num)
#         break
#     if b is 'l':
        
#         your_num = randint(num, num + 10)
#     if b is 's':
#         your_num = randint(1,num - 10)





# basic operation
'''
x = 100
floor_division = 100//7
print(floor_division)

modulus = 100 %  7
print(modulus)



low = 1
high = 100
loop = True

while loop:
    mid = (low + high) // 2
    answer = input('So {} co dung khong '.format(mid))
    if answer == 'c':
        print('Dap an la {} '.format(mid))
        loop = False
    elif answer == 'l':
        low = mid
    elif answer == 's':
        high = mid
'''

# math_2
'''
ask = int(input('Nhap so la '))
for i in range(1, ask):
    if i % 2 == 0:
        print(i)
'''


# math_3
'''
number = int(input('Nhap 1 so ))
for i in range(2, number+1, 2):



number = int(input('Nhap 1 so '))
if number % 2 == 1:
    number = number - 1
for i in range(number, 0, -2):
    print(i)


number -= number % 2
for i in range(number, 0, -2):
    print(i)


'''

# math_4

from math import sqrt
number = int(input('Nhap 1 so '))
count = 0

if number == 1:
    print('Day khong phai so nguyen to')
else:
    for i in range(2, number):
        if number % i == 0:
            count += 1

    if count == 0:
        print('Day la so nguyen to')
    elif count >= 1:
        print('Day khong phai la so nguyen to')