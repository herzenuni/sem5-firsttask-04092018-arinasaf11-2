"""
Функция выводит название введенной цифры от 0 до 9 и ,если указан второй аргумент, преобразует ее в бинарную, восьмеричную или шестнадцатиричную систему счисления и выводит значение
"""
def func(x, y=''):
  if (x == 0):
    string = 'ноль '
  elif (x == 1):
   string = 'один '
  elif (x == 2):
    string = 'два '
  elif (x == 3):
    string ='три '
  elif (x == 4):
    string = 'четыре '
  elif (x == 5):
    string = 'пять '
  elif (x ==6):
    string = 'шесть '
  elif (x == 7):
    string = 'семь '
  elif (x == 8):
    string = 'восемь '
  elif (x == 9):
    string = 'девять '
  else:
    print('Введенное число не входит в диапазон от 0 до 9,попробуйте еще раз')
  if (y == 'bin'):
   string += str(bin(x))
  elif (y == 'oct'):
   string += str(oct(x))
  elif y == 'hex':
   string += str(hex(x))

  return string

print(func(0, 'hex'))

assert func(0) == 'ноль ', 'Название цифры не верно'
assert func(1,'oct') == 'один 0o1', 'Название или перевод цифры не верен'
assert func(3,'hex') == 'три 0x3', 'Название или перевод цифры не верен'
