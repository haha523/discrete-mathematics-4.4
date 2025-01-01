import heapq


def dijkstra(graph, start):
    """
    Алгоритм Дейкстры для нахождения кратчайших расстояний.

    :param graph: Словарь, представляющий граф (взвешенные рёбра).
    :param start: Начальная вершина.
    :return: Словарь с кратчайшими расстояниями от стартовой вершины.
    """
    # Инициализация расстояний (бесконечность для всех вершин, кроме стартовой)
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Очередь приоритетов для обработки вершин
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если текущая длина пути больше, чем записанная, пропускаем
        if current_distance > distances[current_vertex]:
            continue

        # Обновляем расстояния до соседей
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Если нашли более короткий путь
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main():
    # Пример графа: ключ - вершина, значение - список смежных вершин с весами
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 6)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 6), ('C', 3)]
    }

    start_vertex = input("Введите начальную вершину: ")
    if start_vertex not in graph:
        print("Указанной вершины нет в графе.")
        return

    distances = dijkstra(graph, start_vertex)
    print("Кратчайшие расстояния от вершины", start_vertex, ":")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")


if __name__ == "__main__":
    main()
