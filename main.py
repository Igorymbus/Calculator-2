
import math

def calculator():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")

    choice = input("Введите номер операции (1-10): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Ошибка! Деление на ноль невозможно.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            result = num1 ** num2
            print(f"{num1} ** {num2} = {result}")

    elif choice in ('6', '7', '8', '9', '10'):
        num = float(input("Введите число: "))

        if choice == '6':
            result = math.sqrt(num)
            print(f"Квадратный корень из {num} = {result}")
        elif choice == '7':
            result = math.factorial(num)
            print(f"Факториал {num} = {result}")
        elif choice == '8':
            result = math.sin(num)
            print(f"Синус {num} = {result}")
        elif choice == '9':
            result = math.cos(num)
            print(f"Косинус {num} = {result}")
        elif choice == '10':
            result = math.tan(num)
            print(f"Тангенс {num} = {result}")

    else:
        print("Неверный ввод")

    again()


def again():
    calc_again = input("Хотите выполнить еще одну операцию? (Да/Нет): ")
    if calc_again.upper() == "ДА":
        calculator()
    elif calc_again.upper() == "НЕТ":
        print("До свидания!")
    else:
        again()


calculator()