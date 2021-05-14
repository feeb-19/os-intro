print('Вас приветствует программа "Медицинская анкета"')
name = input("Введите имя: ")
surname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
weight = float(input('Введите свой вес: '))

if (age < 30) and ((weight >= 50) and (weight <= 120)):
    print(name, surname, 'У вас хорошее состояние.')
elif (age > 30) and ((weight < 50) or (weight > 120)):
    print(name, surname, ',Вам следует начать наблюдать за своим образом жизни.')
elif (age > 40) and ((weight < 50) or (weight > 120)):
    print(name, surname, ',Вам нужно обратиться к врачу!')
else:
    pass