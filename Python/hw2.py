# Функция для безопасного ввода неотрицательного числа
def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Ошибка: значение не может быть отрицательным. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное число.")

# Функция для безопасного ввода целого неотрицательного числа


def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Ошибка: значение не может быть отрицательным. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")


# === Шаг 1: Запрос данных у пользователя ===
print("=== Анализ покупок в интернет-магазине ===")

# Общая сумма покупок (до скидок)
total_sum = get_non_negative_float("Введите общую сумму покупок (в рублях): ")

# Количество товаров (обязательно >= 1)
while True:
    quantity = get_non_negative_int("Введите количество товаров в корзине: ")
    if quantity == 0:
        print("Ошибка: количество товаров должно быть больше нуля.")
        continue
    break

# Базовая скидка (в %)
discount_percent = get_non_negative_float("Введите сумму скидки (в процентах): ")
if discount_percent > 100:
    print("⚠️  Скидка не может быть больше 100% — устанавливаем 0%.")
    discount_percent = 0


# === Шаг 2: Расчёт базовых значений ===
# Применяем указанную пользователем скидку (если есть)
discount_amount = total_sum * discount_percent / 100
price_after_user_discount = total_sum - discount_amount

# Средняя стоимость товара — по ИСХОДНОЙ сумме (так принято в таких задачах)
avg_price = total_sum / quantity


# === Шаг 3: Дополнительные условия магазина ===
# Доп. скидка 10%, если итоговая сумма > 5000 руб.
additional_discount = 0.0
final_sum = price_after_user_discount

if final_sum > 5000:
    additional_discount = final_sum * 0.10
    final_sum -= additional_discount

# Бесплатная доставка, если товаров > 10
free_shipping = quantity > 10


# === Шаг 4: Вывод результатов ===
print("\n--- Итоговый чек ---")
print(f"Исходная сумма покупок: {total_sum:.2f} руб.")
print(f"Базовая скидка ({discount_percent:.1f}%): -{discount_amount:.2f} руб.")
print(f"Сумма после базовой скидки: {price_after_user_discount:.2f} руб.")

if additional_discount > 0:
    print(f"Доп. скидка 10% (сумма > 5000): -{additional_discount:.2f} руб.")
else:
    print("Доп. скидка: не положена (сумма ≤ 5000 руб.)")

print(f"Итоговая к оплате: {final_sum:.2f} руб.")
print(f"Средняя стоимость товара: {avg_price:.2f} руб.")
print(f"Бесплатная доставка: {'✅ Да' if free_shipping else '❌ Нет'} (товаров: {quantity})")

# --- Полезные подсказки ---
print("\n--- Подсказки магазина ---")
if not free_shipping:
    needed_for_free = 11 - quantity
    print(f"Чтобы получить бесплатную доставку, добавьте ещё {needed_for_free} товар(а/ов).")
if final_sum < 5000:
    needed_for_bonus = 5000 - final_sum
    print(f"Чтобы получить доп. скидку 10%, потратьте ещё на {needed_for_bonus:.2f} руб.")
