import pandas as pd
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

# Присвоєння ваги 1 кожному ребру
for u, v in G.edges:
    G.edges[u, v]['weight'] = 1

# Алгоритм Дейкстри
def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes()}
    shortest_paths[start] = 0
    unvisited_nodes = set(graph.nodes())
    
    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: shortest_paths[node])
        unvisited_nodes.remove(current_node)
        if shortest_paths[current_node] == float('inf'):
            break
        for neighbor, weight in graph[current_node].items():
            alternative_route = shortest_paths[current_node] + weight['weight']
            if alternative_route < shortest_paths[neighbor]:
                shortest_paths[neighbor] = alternative_route
    
    return shortest_paths

# Знаходження найкоротших шляхів між всіма парами вершин
all_shortest_paths = {}
for node in G.nodes():
    all_shortest_paths[node] = dijkstra(G, node)

# Формування таблиці результатів
table_data = []
for source, paths in all_shortest_paths.items():
    for target, distance in paths.items():
        if source != target:
            table_data.append([source, target, distance])

# Створення DataFrame з таблиці даних
df = pd.DataFrame(table_data, columns=['Початкова вершина', 'Кінцева вершина', 'Відстань'])

# Виведення результатів у вигляді таблиці
print(df)

# Завантажити результати у csv форматі
df.to_csv(r"Метро Харків.csv", index=False)

