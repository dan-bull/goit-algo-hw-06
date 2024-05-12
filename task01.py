import networkx as nx
import matplotlib.pyplot as plt

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

# Візуалізація графа
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color=node_color, font_size=10, font_weight='bold', 
        edge_color=edge_color, width=2, alpha=0.7)
plt.title("Мережа метро міста Харкова")
plt.show()

# Аналіз основних характеристик
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:", dict(G.degree()))