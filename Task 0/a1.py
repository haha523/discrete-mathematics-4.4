def check_properties(relation, elements):
    reflexive = all((x, x) in relation for x in elements)
    symmetric = all((b, a) in relation for (a, b) in relation)
    transitive = all(((a, c) in relation) for (a, b) in relation for (b2, c) in relation if b == b2)

    return reflexive, symmetric, transitive

def main():
    # Задаем элементы и отношение
    elements = {1, 2, 3}
    relation = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}

    # Проверяем свойства
    reflexive, symmetric, transitive = check_properties(relation, elements)

    # Выводим результаты
    print(f"Рефлексивность: {'Да' if reflexive else 'Нет'}")
    print(f"Симметричность: {'Да' if symmetric else 'Нет'}")
    print(f"Транзитивность: {'Да' if transitive else 'Нет'}")

if __name__ == "__main__":
    main()