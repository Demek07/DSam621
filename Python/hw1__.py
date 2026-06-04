import numpy as np
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self, n_inputs, learning_rate=0.1):
        """
        n_inputs: количество входных сигналов
        learning_rate: скорость обучения (как быстро учится)
        """
        # Инициализируем веса маленькими случайными числами
        self.weights = np.random.randn(n_inputs) * 0.1
        # bias (смещение) - это и есть отрицательный порог
        self.bias = np.random.randn(1) * 0.1
        self.lr = learning_rate

    def activation(self, x):
        """Пороговая функция активации"""
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        """Предсказать выход для одного набора входных данных"""
        # Взвешенная сумма + смещение
        linear_output = np.dot(inputs, self.weights) + self.bias
        return self.activation(linear_output)

    def train(self, X, y, epochs=100):
        """
        X: массив входных данных
        y: правильные ответы (целевые значения)
        epochs: сколько раз пройти по всем примерам
        """
        history = []  # для записи ошибок

        for epoch in range(epochs):
            errors = 0

            # Проходим по каждому примеру в обучающей выборке
            for inputs, target in zip(X, y):
                # Делаем предсказание
                prediction = self.predict(inputs)

                # Считаем ошибку (0 или 1)
                error = target - prediction

                if error != 0:
                    errors += 1
                    # КЛЮЧЕВОЙ МОМЕНТ: обновляем веса и bias
                    # Формула: новый_вес = старый_вес + скорость_обучения * ошибка * входной_сигнал
                    self.weights += self.lr * error * inputs
                    self.bias += self.lr * error

            # Запоминаем количество ошибок на этой эпохе
            history.append(errors)

            # Если ошибок нет - обучение закончено
            if errors == 0:
                print(f"Обучение завершено на эпохе {epoch+1}")
                break

        return history

# ============================================
# ЗАДАЧА: учим перцептрон принимать решение о походе на пляж
# ============================================

# Обучающая выборка:
# [температура (нормализованная), солнце (0 или 1)] -> решение (0 или 1)
# Нормализуем температуру: делим на 40 (максимальная температура)
# Фактические значения: 30°C -> 0.75, 15°C -> 0.375, 10°C -> 0.25, 5°C -> 0.125

# Пример 1: 30°C, солнечно -> ИДЁМ (1)
# Пример 2: 5°C, пасмурно -> НЕ ИДЁМ (0)
# Пример 3: 10°C, солнечно -> ИДЁМ (1)  # хотя холодно, но солнце!
# Пример 4: 20°C, пасмурно -> НЕ ИДЁМ (0)  # тепло, но пасмурно


X_train = np.array([
    [30/40, 1],   # 0.75, 1 -> 1
    [5/40,  0],   # 0.125, 0 -> 0
    [10/40, 1],   # 0.25, 1 -> 1
    [20/40, 0]    # 0.5, 0 -> 0
])

y_train = np.array([1, 0, 1, 0])

# Создаём перцептрон с 2 входами и скоростью обучения 0.1
p = Perceptron(n_inputs=2, learning_rate=0.1)

# Показываем начальные веса и bias
print("=== ДО ОБУЧЕНИЯ ===")
print(f"Начальные веса: w1 = {p.weights[0]:.3f}, w2 = {p.weights[1]:.3f}")
print(f"Начальный bias: {p.bias[0]:.3f} (это отрицательный порог)")
print(f"Порог (threshold): {-p.bias[0]:.3f}")

print("\n--- Проверка на обучающих примерах ДО обучения ---")
for inputs, target in zip(X_train, y_train):
    pred = p.predict(inputs)
    temp_c = inputs[0] * 40
    sun = "☀️" if inputs[1] == 1 else "☁️"
    print(f"{temp_c:.0f}°C {sun} -> предсказание: {pred}, должно быть: {target}")

# Обучаем перцептрон
print("\n=== ОБУЧЕНИЕ ===")
history = p.train(X_train, y_train, epochs=20)

print(f"\n=== ПОСЛЕ ОБУЧЕНИЯ ===")
print(f"Итоговые веса: w1 = {p.weights[0]:.3f}, w2 = {p.weights[1]:.3f}")
print(f"Итоговый bias: {p.bias[0]:.3f}")
print(f"Итоговый порог (threshold): {-p.bias[0]:.3f}")

print("\n--- Проверка на обучающих примерах ПОСЛЕ обучения ---")
for inputs, target in zip(X_train, y_train):
    pred = p.predict(inputs)
    temp_c = inputs[0] * 40
    sun = "☀️" if inputs[1] == 1 else "☁️"
    result = "✅" if pred == target else "❌"
    print(f"{temp_c:.0f}°C {sun} -> предсказание: {pred}, должно быть: {target} {result}")

# ============================================
# ТЕСТИРОВАНИЕ НА НОВЫХ ДАННЫХ
# ============================================
print("\n=== ТЕСТ НА НОВЫХ ПРИМЕРАХ ===")
test_cases = [
    (25, 1, "25°C ☀️ -> "),   # 25°C, солнечно
    (15, 1, "15°C ☀️ -> "),   # 15°C, солнечно
    (8,  0, "8°C  ☁️ -> "),   # 8°C, пасмурно
    (18, 0, "18°C ☁️ -> "),   # 18°C, пасмурно
    (28, 1, "28°C ☀️ -> "),   # 28°C, солнечно
]

for temp, sun, desc in test_cases:
    inputs = np.array([temp/40, sun])
    pred = p.predict(inputs)
    decision = "🏖️ ИДЁМ!" if pred == 1 else "🏠 ОСТАЁМСЯ"
    print(f"{desc}{decision}")

# Визуализируем процесс обучения
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(history, 'b-', marker='o')
plt.xlabel('Эпоха обучения')
plt.ylabel('Количество ошибок')
plt.title('Снижение ошибок в процессе обучения')
plt.grid(True)

plt.subplot(1, 2, 2)
# Показываем разделяющую линию, которую нашёл перцептрон
x_line = np.array([0, 1])
# Формула: w1*x1 + w2*x2 + bias = 0 -> x2 = (-w1*x1 - bias) / w2
y_line = (-p.weights[0] * x_line - p.bias[0]) / p.weights[1]

# Рисуем точки обучающей выборки
for inputs, target in zip(X_train, y_train):
    color = 'green' if target == 1 else 'red'
    plt.scatter(inputs[0]*40, inputs[1], c=color, s=100,
                marker='o', label='Идём' if target == 1 else 'Не идём')

plt.plot(x_line*40, y_line, 'b--', label='Граница решения')
plt.xlabel('Температура (°C)')
plt.ylabel('Солнечно (1=☀️, 0=☁️)')
plt.title('Разделяющая линия, которую нашёл перцептрон')
plt.xlim(0, 40)
plt.ylim(-0.2, 1.2)
plt.grid(True)

plt.tight_layout()
plt.show()
