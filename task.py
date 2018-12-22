#Собственное исключение
class RangeException(Exception):
  def __init__(self,text):
    self.text=text

  def __str__(self):
    return "RangeException: " + self.text

try:
  number = int(input('Введите число от 0 до 9 - '))
  if ((number<0) | (number>9)):
    raise RangeException('Введенное число не входит в указанный интервал')
except RangeException as ex:
  print(str(ex))
  number = int(input('Введите число от 0 до 9 - '))
except ValueError:
  print('Введенный символ не является числом,попробуйте еще раз')
  number = int(input('Введите число от 0 до 9 - '))
answer = input('Напишите ="да", если хотите перевести это число в какую-либо систему счисления, или "нет", если хотите увидеть только название введенной вами цифры - ')
if (answer == 'да'):
  typ = input('"bin"-бинарная система\n"oct"-восьмеричная система\n"hex"-шестнадцатиричная система\n')
else:
  typ=''


"""
Функция выводит название введенной цифры от 0 до 9 или,если указан второй аргумент, преобразует ее в бинарную, восьмеричную или шестнадцатиричную систему счисления и выводит значение
"""
def func(x, y):
    if (x == 0):
      string = 'ноль'
    elif (x == 1):
      string = 'один'
    elif (x == 2):
      string = 'два'
    elif (x == 3):
      string ='три'
    elif (x == 4):
      string = 'четыре'
    elif (x == 5):
      string = 'пять'
    elif (x ==6):
      string = 'шесть'
    elif (x == 7):
      string = 'семь'
    elif (x == 8):
      string = 'восемь'
    elif (x == 9):
      string = 'девять'
    if (y == 'bin'):
      string += ": "+str(bin(x))
    elif (y == 'oct'):
      string += ": "+str(oct(x))
    elif y == 'hex':
      string += ": "+str(hex(x))
    print(string)
    return string


with open (".\history_of_func.txt",'a') as history:
    history.write(str(func(number, typ))+"\n")

#assert func(0,'') == 'ноль', 'Название цифры не верно'
#assert func(1,'oct') == '0o1', 'Название или перевод цифры не верен'
#assert func(3,'hex') == '0x3', 'Название или перевод цифры не верен'
