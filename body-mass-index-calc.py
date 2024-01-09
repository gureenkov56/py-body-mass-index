weight = input('Введите массу тела (кг): ')
height = input('Введите рост (см): ')

if not (weight.isdigit() and height.isdigit()):
    print('Ошибка! Вы можете вводить только числа!')
    exit()

weight = int(weight)
height = int(height)    

body_mass_index = weight / ((height / 100) ** 2)

res = ''

if body_mass_index < 16:
    res = 'Выраженный дефицит массы тела'
elif body_mass_index < 18.5:
    res = 'Недостаточная масса тела'
elif body_mass_index < 25:
    res = 'Норма'
elif body_mass_index < 30:
    res = 'Избыточная масса тела'
elif body_mass_index < 35:
    res = 'Ожирение 1 степени'
elif body_mass_index < 40:
    res = 'Ожирение 2 степени'
else:
    res = 'Ожирение 3 степени'

print(f'Индекс массы вашего тела: {body_mass_index}')
print(f'Ваш показатель: {res}')