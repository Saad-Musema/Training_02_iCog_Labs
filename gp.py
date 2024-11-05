class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []
    
    def add_neighbor(self, neighbor):
        self.adjacent.append(neighbor)
    
    def __str__(self):
        return f"{self.value}: {[neighbor.value for neighbor in self.adjacent]}"

class Graph:
    def __init__(self):
        self.nodes = {}
        
    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
            
    def add_edge(self, from_node, to_node):
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)
        
        self.nodes[from_node].add_neighbor(self.nodes[to_node])
    
    def display_graph(self):
        for node in self.nodes.values():
            print(node)
            

graph = Graph()

# New York,Los Angeles
# New York,Chicago
Training Tasks
# New York,Houston
# Los Angeles,Chicago
# Los Angeles,Houston
# Chicago,Houston
# San Francisco,Los Angeles
# San Francisco,Chicago
# San Francisco,Houston
# Seattle,Los Angeles
# Seattle,Chicago
# Seattle,Houston
# Boston,Los Angeles
# Boston,Chicago
# Boston,Houston
# Miami,Los Angeles
# Miami,Chicago
# Miami,Houston

graph.add_edge("New York", "Los Angeles")
graph.add_edge("New York", "Chicage")
graph.add_edge("New York", "Houston")
graph.add_edge("Los Angeles", "Chicago")

graph.display_graph()