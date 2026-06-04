# Функция для безопасного ввода положительного числа
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Ошибка: значение должно быть больше нуля. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное число.")


# Функция для ввода целого положительного числа
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Ошибка: значение должно быть больше нуля. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")


# Шаг 1. Запрос данных у пользователя с проверкой
distance = get_positive_float("Введите расстояние до места назначения (в км): ")
fuel_consumption = get_positive_float("Введите расход топлива автомобиля (в литрах на 100 км): ")
fuel_price = get_positive_float("Введите стоимость топлива за литр: ")
nights = get_positive_int("Введите количество ночей проживания: ")
accommodation_price = get_positive_float("Введите стоимость проживания за ночь: ")
food_cost = get_positive_float("Введите оценочную стоимость питания в день: ")
days = get_positive_int("Введите количество дней поездки: ")

# Шаг 2. Рассчитываем значения
total_fuel_cost = distance / 100 * fuel_consumption * fuel_price
total_accommodation_cost = nights * accommodation_price
total_food_cost = days * food_cost

# Шаг 3. Рассчитываем общую сумму расходов
total_expenses = total_fuel_cost + total_accommodation_cost + total_food_cost

# Шаг 4. Выводим результаты
print("\n--- Результаты расчёта ---")
print(f"Общая стоимость топлива: {total_fuel_cost:.2f} руб.")
print(f"Общая стоимость проживания: {total_accommodation_cost:.2f} руб.")
print(f"Общая стоимость питания: {total_food_cost:.2f} руб.")
print(f"Общая сумма расходов на поездку: {total_expenses:.2f} руб.")
