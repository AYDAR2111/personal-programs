import random

print('Добро пожаловать в числовую угадайку')
n = int(input('Укажите максимальное заданное число: '))
num = random.randint(1, n + 1)

def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= n:
            return True
        else:
            return False
    else:
        return False

count = 0
again = 'да'
stop = ''
while again.lower() == 'да':
    value = input('Введите число от 1 до {}: '.format(n))
    if value == 'стоп':
        print('Надеюсь вы ещё вернётесь...')
        break
    if not is_valid(value):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    value = int(value)
    if value < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count += 1
    elif value > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count += 1
    else:
        print('Вы угадали, поздравляем!')
        count += 1
        print('Количество потыток:', count)
        again = input('Хотите сыграть ещё? (да или нет): ')
        count = 0
        num = random.randint(1, n + 1)
        
if again != 'да':
    print('Спасибо, что играли в числовую угадайку.') 