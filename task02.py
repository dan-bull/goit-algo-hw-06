import networkx as nx

# Створення порожнього графа
G = nx.Graph()

# Додавання станцій метро та їх зв'язків
metro_lines = {
    "Холодногірсько-заводська лінія": ["Холодна гора", "Південний вокзал", "Центральний ринок", "Майдан Конституції", 
                                       "Проспект Гагаріна", "Спортивна", "Завод ім. Малишева", "Палац спорту", 
                                       "Армійська", "ім. Масельського", "Тракторний завод", "Індустріальна"],
    "Олексіївська лінія": ["Перемога", "Олексіївська", "23 серпня", "Ботанічний сад", "Наукова", "Держпром", 
                            "Архітектора Бекетова", "Захисників України", "Метробудівників"],
    "Салтівська лінія": ["Героїв праці", "Студентська", "Академіка Павлова", "Академіка Барабашова", "Київська", 
                          "Пушкінська", "Університет", "Історичний музей"]
}

# Додавання вершин та ребер
for line, stations in metro_lines.items():
    G.add_nodes_from(stations)
    for i in range(len(stations) - 1):
        G.add_edge(stations[i], stations[i+1])

# Додавання пересадок
transfers = [("Держпром", "Університет"), ("Спортивна", "Метробудівників"), ("Історичний музей", "Майдан Конституції")]
G.add_edges_from(transfers)

# Визначення кольорів вершин і ребер
node_color = ['lightblue' if node not in sum(transfers, ()) else 'lightgreen' for node in G.nodes()]
edge_color = ['gray' if edge not in transfers else 'green' for edge in G.edges()]

# Алгоритм DFS
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Алгоритм BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Знаходження шляхів за допомогою DFS
dfs_paths_result = list(dfs_paths(G, "Перемога", "Завод ім. Малишева"))

# Знаходження шляхів за допомогою BFS
bfs_paths_result = list(bfs_paths(G, "Перемога", "Завод ім. Малишева"))

print("Шляхи, знайдені за допомогою DFS:", dfs_paths_result)
print("Шляхи, знайдені за допомогою BFS:", bfs_paths_result)
