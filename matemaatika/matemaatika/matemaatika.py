import random
# Приветственное сообщение и ввод количества вопросов
print("proverka znanij!")
voprosq=int(input("skolko voprosov?"))
tase=int(input("vqberi tase (Tase 1, Tase 2, Tase 3): "))
# Определяем диапазон чисел в зависимости от выбранного уровня сложности
if tase==1:
    num_range=(1, 10)
elif tase==2:
    num_range=(10, 100)
elif tase==3:
    num_range=(100, 1000)
else:
    print("nu togda vqberu za tebja - tase 2 budet")
    num_range = (10, 100)
# Задаем возможные операции
dejstvija=['+', '-', '*', '/', '**']
prav_otvetq=0   # Счетчик правильных ответов

# Основной цикл для генерации вопросов
for i in range(voprosq):
    dejstvie=random.choice(dejstvija)# Случайный выбор операции
    num1=random.randint(num_range[0], num_range[1])# Случайный выбор первого числа
    num2=random.randint(num_range[0], num_range[1])# Случайный выбор второго числа

    # Выполняем выбранную операцию
    if dejstvie=='+':
        otvet=num1+num2
    elif dejstvie=='-':
        otvet=num1-num2
    elif dejstvie=='*':
        otvet=num1*num2
    elif dejstvie=='/':
        num2=random.randint(1, num_range[1])
        otvet=num1/num2
    elif dejstvie=='**':
        otvet=num1 ** num2 
    print(f"skolko budet {num1} {dejstvie} {num2}?")
    tvoj_otvet=float(input("otvet: ")) # Получаем ответ пользователя и преобразуем его в число с плавающей точкой
    if tvoj_otvet==otvet:
        print("pravilno!")
        prav_otvetq+=1
    else:
        print("haha nepravilno!")
score=(prav_otvetq/voprosq)*100 # Вычисляем процент правильных ответов
print("\nkonec!")
print("tvoj score:", score)
# Выводим оценку в зависимости от процента правильных ответов
if score<60:
    print("Hinne 2")
elif score<75:
    print("Hinne 3")
elif score<90:
    print("Hinne 4")
else:
    print("Hinne 5")
