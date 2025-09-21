import collections
import networkx as nx
import matplotlib.pyplot as plt

def bfs(graph, root):
    visited, queue = [], collections.deque([root])
    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.append(v)
            queue.extend([i for i in graph[v] if i not in visited])
    print("BFS OUTPUT:", visited)

def dfs(graph, root):
    visited, stack = [], [root]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            stack.extend(reversed(graph[v]))  # reversed keeps DFS order consistent
    print("DFS OUTPUT:", visited)

def dls(graph, root, limit, visited=None, depth=0):
    if visited is None:
        visited = []
    visited.append(root)
    if depth < limit:
        for neighbor in graph[root]:
            if neighbor not in visited:
                dls(graph, neighbor, limit, visited, depth+1)
    return visited

def iddfs(graph, root, max_depth):
    for depth in range(max_depth+1):
        visited = dls(graph, root, depth)
        print(f"IDDFS at depth {depth}:", visited)

if __name__=="__main__":
    graph = {
        'A':['B','C','D'],
        'B':['E'],
        'E':['C'],
        'C':['A','D'],
        'D':['A','C']
    }
    
    bfs(graph,'A')
    dfs(graph,'A')
    print("DLS (limit=2):", dls(graph,'A',2))
    iddfs(graph,'A',3)
    

    G = nx.Graph(graph)
    nx.draw(G, with_labels=True)
    plt.show()
