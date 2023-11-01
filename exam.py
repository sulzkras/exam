"""
Учитывая целое число num, несколько раз складывать все его цифры, пока результат не будет содержать только одну цифру, и возвращать его.

Example 1:
Input: num = 38 Output: 2 Explanation: Процесс 38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Поскольку 2 имеет только одну цифру, верните ее.

Example 2:
Input: num = 0 Output: 0

"""

# num = int(input('Введите число: '))
# sum_num = 0
# while (num != 0):
#     sum_num = sum_num + num % 10
#     num = num // 10

# print(f'Сумма всех цифр числа равна: ", {sum_num}')


def sum_num(num):
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    print(f'Сумма всех цифр числа равна {sum}')

num = int(input('Введите число: '))
sum_num(num)
