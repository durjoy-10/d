import heapq
import networkx as nx
import matplotlib.pyplot as plt

# ---------- Uniform Cost Search ----------
def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [start])]  # (cost, node, path)
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return cost, path
        if node in visited:
            continue
        visited.add(node)
        for neigh, edge_cost in graph[node]:
            if neigh not in visited:
                heapq.heappush(pq, (cost + edge_cost, neigh, path + [neigh]))
    return float("inf"), []

# ---------- Greedy Best-First Search ----------
def greedy_best_first(graph, start, goal, h):
    pq = [(h[start], start, [start])]
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neigh, cost in graph[node]:
            if neigh not in visited:
                heapq.heappush(pq, (h[neigh], neigh, path + [neigh]))
    return None

# ---------- A* Search ----------
def a_star(graph, start, goal, h):
    pq = [(h[start], 0, start, [start])]   # (f, g, node, path)
    best_g = {}
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return g, path
        if node in best_g and g >= best_g[node]:
            continue
        best_g[node] = g
        for neigh, cost in graph[node]:
            new_g = g + cost
            heapq.heappush(pq, (new_g + h[neigh], new_g, neigh, path + [neigh]))
    return float("inf"), None


# ---------- Example Usage ----------
if __name__ == "__main__":
    # --- Graph from informed.py ---
    graph = {
        'S': [('A', 1), ('B', 4)],
        'A': [('C', 8)],
        'B': [('C', 2), ('D', 2)],
        'C': [('G', 2)],
        'D': [('G', 1)],
        'G': []
    }

    # Heuristic values to goal G
    heuristic = {'S': 6, 'A': 4, 'B': 2, 'C': 2, 'D': 1, 'G': 0}

    start, goal = 'S', 'G'

    # Run UCS
    ucs_cost, ucs_path = uniform_cost_search(graph, start, goal)
    print("Uniform Cost Search Path :", " -> ".join(ucs_path), "with cost", ucs_cost)

    # Run Greedy Best-First Search
    greedy_path = greedy_best_first(graph, start, goal, heuristic)
    print("Greedy Best-First Path   :", " -> ".join(greedy_path))

    # Run A*
    astar_cost, astar_path = a_star(graph, start, goal, heuristic)
    print("A* Path                  :", " -> ".join(astar_path), "with cost", astar_cost)

    # ---------- Visualize the Graph ----------
    G = nx.Graph([(u, v, {'weight': w}) for u, lst in graph.items() for v, w in lst])
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1200)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    plt.title("Graph for UCS, Greedy Best-First & A* Search")
    plt.show()
