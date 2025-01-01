def boolean_function_to_zhengalkin(table):
    n = len(table).bit_length() - 1  # Количество переменных
    terms = []

    # Генерация всех возможных комбинаций переменных
    for i in range(len(table)):
        if table[i] == 1:
            term = []
            for j in range(n):
                if (i >> j) & 1:  # Проверяем j-ый бит числа i
                    term.append(f"x{j}")
                else:  # Если бит равен 0, используем отрицание
                    term.append(f"x{j}'")
            terms.append(" * ".join(term))

    # Объединяем термы в полином
    polynomial = " + ".join(terms) if terms else "0"
    return polynomial

def main():
    # Пример таблицы истинности для булевой функции
    # Функция: f(0, 0) = 0, f(0, 1) = 1, f(1, 0) = 1, f(1, 1) = 0
    truth_table = [0, 1, 1, 0]  # f(0,0), f(0,1), f(1,0), f(1,1)

    # Находим полином Жегалкина
    polynomial = boolean_function_to_zhengalkin(truth_table)

    # Выводим результат
    print("Полином Жегалкина:", polynomial)

if __name__ == "__main__":
    main()