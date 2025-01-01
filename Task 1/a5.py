def truth_table_to_skf(tt):
    n = len(tt[0]) - 1  # Количество переменных (не считая последнюю колонку с результатом)
    sknf = []

    for row in tt:
        if row[-1] == 0:  # Строки, где выходное значение 0
            term = []
            for i in range(n):
                if row[i] == 0:
                    term.append(f"¬x{i + 1}")  # Отрицание переменной
                else:
                    term.append(f"x{i + 1}")  # Прямая переменная
            sknf.append(f"({' ∨ '.join(term)})")

    return ' ∧ '.join(sknf)


# Пример использования:
# Таблица истинности: {x1, x2}, выходное значение в последней колонке
# f(x1, x2) = x1 AND x2
tt = [
    [0, 0, 0],  # f(0, 0) = 0
    [0, 1, 1],  # f(0, 1) = 1
    [1, 0, 1],  # f(1, 0) = 1
    [1, 1, 0]  # f(1, 1) = 0
]

result = truth_table_to_skf(tt)
print(f"СКНФ: {result}")