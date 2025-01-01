def generate_power_set(s):
    power_set = []
    n = len(s)
    # Обходим все возможные комбинации
    for i in range(1 << n):  # 2^n
        subset = []
        for j in range(n):
            # Если j-ый бит числа i установлен, добавляем элемент s[j]
            if i & (1 << j):
                subset.append(s[j])
        power_set.append(subset)
    return power_set

def main():
    # Задайте множество чисел
    numbers = [1, 2, 3]  # Пример для тестирования

    # Генерируем булеан
    power_set = generate_power_set(numbers)

    # Выводим результирующее множество
    print("Булеан множества:", power_set)

if __name__ == "__main__":
    main()