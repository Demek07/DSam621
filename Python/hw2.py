# === проверка на положительность ===
def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❌ Ошибка: значение не может быть отрицательным. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print("❌ Ошибка: пожалуйста, введите корректное число.")


# === проверка на целое число > 0 ===
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("❌ Ошибка: значение должно быть больше нуля. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print("❌ Ошибка: пожалуйста, введите целое число.")


# === Шаг 1: Запрос данных ===

print("=" * 50)
print("📊 СИСТЕМА АНАЛИЗА ПОКУПОК — ДЕТАЛЬНЫЙ ОТЧЁТ")
print("=" * 50)

total_sum = get_non_negative_float("Введите общую сумму покупок (руб.): ")
quantity = get_positive_int("Введите количество товаров: ")
discount_percent = get_non_negative_float("Введите базовую скидку (%, 0–100): ")

# Коррекция некорректной скидки
if discount_percent > 100:
    print("⚠️  Скидка не может превышать 100%. Устанавливаем 0%.")
    discount_percent = 0

# === Шаг 2: Базовые расчёты ===
discount_amount = total_sum * discount_percent / 100
price_after_base_discount = total_sum - discount_amount
avg_price_per_item = total_sum / quantity

# === Шаг 3: Логика бонусов магазина ===
# Доп. скидка 10% при итоге > 5000
if price_after_base_discount > 5000:
    additional_discount = price_after_base_discount * 0.10
    final_sum = price_after_base_discount - additional_discount
    status_bonus = "✅ Доп. скидка 10% применена"
else:
    additional_discount = 0.0
    final_sum = price_after_base_discount
    status_bonus = "❌ Доп. скидка не применена (нужно > 5000 руб.)"

# Бесплатная доставка при количестве > 10
free_shipping = quantity > 10

# === Шаг 4: Формирование отчёта ===
print("\n" + "─" * 50)
print("🧾 ДЕТАЛЬНЫЙ ЧЕК")
print("─" * 50)

print(f"🔹 Исходная сумма корзины:       {total_sum:10.2f} руб.")
print(f"🔹 Базовая скидка ({discount_percent:.1f}%):      -{discount_amount:10.2f} руб.")
print(f"🔹 Цена после базовой скидки:   {price_after_base_discount:10.2f} руб.")

if additional_discount > 0:
    print(f"🔹 Доп. скидка 10% (за >5000):  -{additional_discount:10.2f} руб.")

print(f"🔹 ИТОГО К ОПЛАТЕ:             {final_sum:10.2f} руб.")

print("\n" + "─" * 50)
print("📈 АНАЛИЗ КОРЗИНЫ")
print("─" * 50)

print(f"🔹 Количество товаров:           {quantity} шт.")
print(f"🔹 Средняя стоимость товара:    {avg_price_per_item:10.2f} руб.")
print(f"🔹 Бесплатная доставка:          {'✅ Да' if free_shipping else '❌ Нет'}")
print(f"   → Условие: более 10 товаров")
print(f"   → Вы имеете: {quantity} товаров")

# === Шаг 5: Подсказки для пользователя ===
print("\n" + "─" * 50)
print("💡 РЕКОМЕНДАЦИИ ПО ОПТИМИЗАЦИИ")
print("─" * 50)

has_recommendations = False

# Подсказка по бесплатной доставке
if not free_shipping:
    needed = 11 - quantity
    print(f"• Чтобы получить бесплатную доставку:")
    print(f"  → Добавьте ещё {needed} товар(а/ов) ✨")

# Подсказка по доп. скидке — только если она ещё не применена
if not (price_after_base_discount > 5000):
    needed = 5000 - price_after_base_discount
    print(f"• Чтобы активировать доп. скидку 10%:")
    print(f"  → Потратьте ещё на {needed:.2f} руб. 💰")

# Подсказка по среднему чеку — только если < 500
if avg_price_per_item < 500:
    print(f"• Средняя стоимость товара низкая ({avg_price_per_item:.0f} руб.)")
    print(f"  → Рассмотрите возможность добавить 1–2 более дорогих позиции 🛍️")

# Если рекомендаций нет — сообщаем пользователю
if not has_recommendations:
    print("✅ Вы уже получили все возможные бонусы — отлично сработано! 🎉")

# Итоговая оценка
print("\n" + "─" * 50)
print("🏆 ИТОГОВАЯ ОЦЕНКА СДЕЛКИ")
print("─" * 50)

discount_total_percent = (total_sum - final_sum) / total_sum * 100 if total_sum > 0 else 0
print(f"🔹 Вы сэкономили: {total_sum - final_sum:.2f} руб. ({discount_total_percent:.1f}% от суммы)")

if discount_total_percent > 15:
    print("🔥 Отличная сделка! Вы максимально использовали бонусы магазина! 🎉")
elif discount_total_percent > 8:
    print("👍 Хорошая скидка — вы близки к максимальной выгоде!")
elif discount_total_percent > 0:
    print("✅ Скидка применена — стоит обратить внимание на рекомендации!")
else:
    print("ℹ️  Скидка не применена — добавьте 5000+ руб. для активации бонусов.")

print("=" * 50)
print("📄 Отчёт сгенерирован успешно.")
print("=" * 50)
