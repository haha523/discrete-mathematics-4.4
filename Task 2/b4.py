from collections import deque


def bfs(graph, start):
    """
    Обход графа в ширину.

    :param graph: Словарь, представляющий граф. Ключи — вершины, значения — списки смежных вершин.
    :param start: Стартовая вершина.
    :return: Список вершин в порядке их посещения.
    """
    visited = set()  # Множество посещенных вершин
    queue = deque([start])  # Очередь для BFS
    order = []  # Порядок посещения вершин

    while queue:
        vertex = queue.popleft()  # Берем вершину из начала очереди
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            # Добавляем в очередь все смежные вершины, которые еще не посещены
            queue.extend(v for v in graph[vertex] if v not in visited)

    return order


def main():
    # Пример графа
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [6],
        6: []
    }

    start_vertex = int(input("Введите стартовую вершину: "))

    if start_vertex not in graph:
        print("Стартовая вершина отсутствует в графе.")
        return

    order = bfs(graph, start_vertex)
    print("Порядок обхода:", order)


if __name__ == "__main__":
    main()
