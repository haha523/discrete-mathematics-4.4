def is_reflexive(relation, elements):
    """Проверяет рефлексивность отношения."""
    for e in elements:
        if (e, e) not in relation:
            return False
    return True

def is_symmetric(relation):
    """Проверяет симметричность отношения."""
    for (a, b) in relation:
        if (b, a) not in relation:
            return False
    return True

def is_transitive(relation):
    """Проверяет транзитивность отношения."""
    for (a, b) in relation:
        for (c, d) in relation:
            if b == c and (a, d) not in relation:
                return False
    return True

# Пример данных
elements = {1, 2, 3}
relation = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}

# Проверка свойств
print("Рефлексивность:", is_reflexive(relation, elements))
print("Симметричность:", is_symmetric(relation))
print("Транзитивность:", is_transitive(relation))
