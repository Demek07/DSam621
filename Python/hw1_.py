import tensorflow as tf
import numpy as np


def get_float(prompt, default=None):
    """Безопасно считывает число или возвращает значение по умолчанию."""
    while True:
        user_input = input(prompt)
        if not user_input and default is not None:
            return default
        try:
            return float(user_input)
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите число.")


# --- Сбор весов от пользователя ---
print("=== Оценка отелей (TensorFlow Perceptron) ===")
print("Введите веса для формулы оценки:")
w_country = get_float("Вес страны [по умолчанию 0.8]: ", 0.8)
w_price = get_float("Вес цены [по умолчанию 0.3]: ", 0.3)
w_rating = get_float("Вес рейтинга [по умолчанию 0.5]: ", 0.5)
w_dist = get_float("Вес расстояния [по умолчанию -0.6]: ", -0.6)
weights = [w_country, w_price, w_rating, w_dist]

# --- Создание и настройка модели ---
model = tf.keras.Sequential([
    # Один нейрон, принимающий вектор из 4 признаков.
    # use_bias=False, так как в формуле нет свободного члена.
    # kernel_initializer='zeros' нужен только для корректного задания формы,
    # мы сразу перезапишем эти веса.
    tf.keras.layers.Dense(units=1, input_shape=(4,), use_bias=False, kernel_initializer='zeros')
])

# Устанавливаем веса ядра (ядро имеет форму (4, 1))
model.layers[0].set_weights([tf.constant(weights, shape=(4, 1))])

# --- Сбор параметров отеля от пользователя ---
print("\nВведите параметры отеля:")
country_code = get_float("Код страны (например, 1.0): ")
price = get_float("Цена за ночь: ")
rating = get_float("Рейтинг (0–10): ")
distance_km = get_float("Расстояние от вас (км): ")

# Формируем входной массив для модели
features = [[country_code, price, rating, distance_km]]
features = np.array(features)

# --- Предсказание и проверка ограничения ---
raw_score = model.predict(features)[0][0]  # Получаем скалярное значение

if distance_km < 200:
    verdict = f"Не подходит — отель находится ближе 200 км ({distance_km:.1f} км)."
else:
    verdict = f"Оценка: {raw_score:.2f}"

# --- Вывод результата ---
print(f"\nИтоговый результат: {verdict}")
