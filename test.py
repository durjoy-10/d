import heapq 
import networkx as nx 
import matplotlib.pyplot as plt 

def uniform_cose_search(graph,start,goal):
    pq =[(0,start,[start])]
    visited=set()
    
    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return cost,path
        if node in visited:
            continue
        visited.add(node)
        
        for neighbour,edge_cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq,(cost+edge_cost,neighbour,path+[neighbour]))
    return float("inf"),[]

if __name__=="__main__":
    graph = {
        'A': [('B', 2), ('C', 5)],
        'B': [('C', 6), ('D', 1), ('E', 3)],
        'C': [('D', 2), ('F', 8)],
        'D': [('E', 4), ('F', 3)],
        'E': [('F', 2)],
        'F': []  # goal or dead end
    }
    
    start,goal='A','F'
    total_cost,best_path= uniform_cose_search(graph,start,goal)
    print(f"Least Cost: {total_cost}")
    print("Path:", "->".join(best_path))
    # print("Path:", " -> ".join(best_path))
    
    G = nx.Graph([(u,v,{'weight':w}) for u, lst in graph.items() for v, w in lst])
    nx.draw(G, pos:=nx.spring_layout(G), with_labels=True,
            node_color="skyblue", node_size=1200)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G,"weight"))
    plt.show()

    
    