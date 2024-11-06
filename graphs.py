class Node:
    """
    A class to represent a node in the graph.
    """
    def __init__(self, value):
        """
        Initialize a node with a value and an empty list of adjacent nodes.
        
        Parameters:
        value (str): The value of the node.
        """
        self.value = value
        self.adjacent = []
    
    def add_neighbor(self, neighbor):
        """
        Add a neighbor to the node's adjacency list.
        
        Parameters:
        neighbor (Node): The neighbor node to be added.
        """
        self.adjacent.append(neighbor)
    
    def __str__(self):
        """
        Return a string representation of the node and its neighbors.
        
        Returns:
        str: The string representation of the node.
        """
        return f"{self.value}: {[neighbor.value for neighbor in self.adjacent]}"

class Graph:
    """
    A class to represent a graph.
    """
    def __init__(self):
        """
        Initialize an empty graph with a dictionary of nodes.
        """
        self.nodes = {}
        
    def add_node(self, value):
        """
        Add a node to the graph.
        
        Parameters:
        value (str): The value of the node to be added.
        """
        if value not in self.nodes:
            self.nodes[value] = Node(value)
            
    def add_edge(self, from_node, to_node):
        """
        Add an edge between two nodes in the graph.
        
        Parameters:
        from_node (str): The value of the starting node.
        to_node (str): The value of the ending node.
        """
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)
        
        self.nodes[from_node].add_neighbor(self.nodes[to_node])
    
    def display_graph(self):
        """
        Display the graph by printing each node and its neighbors.
        """
        for node in self.nodes.values():
            print(node)
    
    def bfs(self, start_value, end_value):
        """
        Perform breadth-first search to find a path from start_value to end_value.
        
        Parameters:
        start_value (str): The value of the starting node.
        end_value (str): The value of the ending node.
        
        Returns:
        list: The path from start_value to end_value, or None if no path is found.
        """
        if start_value not in self.nodes or end_value not in self.nodes:
            return None
        
        visited = set()
        queue = [(self.nodes[start_value], [start_value])]
        
        while queue:
            current, path = queue.pop(0)
            if current.value not in visited:
                if current.value == end_value:
                    return path
                visited.add(current.value)
                for neighbor in current.adjacent:
                    if neighbor.value not in visited:
                        queue.append((neighbor, path + [neighbor.value]))
        return None
    
    def dfs_recursive(self, current, end_value, path, visited):
        """
        Perform depth-first search recursively to find a path from current to end_value.
        
        Parameters:
        current (Node): The current node being visited.
        end_value (str): The value of the ending node.
        path (list): The current path being constructed.
        visited (set): The set of visited nodes.
        
        Returns:
        list: The path from the start node to end_value, or None if no path is found.
        """
        if current.value == end_value:
            return path
        
        visited.add(current.value)
        for neighbor in current.adjacent:
            if neighbor.value not in visited:
                result = self.dfs_recursive(neighbor, end_value, path + [neighbor.value], visited)
                if result:
                    return result
        return None
    
    def dfs(self, start_value, end_value):
        """
        Perform depth-first search to find a path from start_value to end_value.
        
        Parameters:
        start_value (str): The value of the starting node.
        end_value (str): The value of the ending node.
        
        Returns:
        list: The path from start_value to end_value, or None if no path is found.
        """
        if start_value not in self.nodes or end_value not in self.nodes:
            return None
        return self.dfs_recursive(self.nodes[start_value], end_value, [start_value], set())

def parse_edges_from_file(filename):
    """
    Parse edges from a file and return a list of edges.
    
    Parameters:
    filename (str): The name of the file containing the edges.
    
    Returns:
    list: A list of tuples representing the edges.
    """
    edges = []
    with open(filename, 'r') as file:
        for line in file:
            from_node, to_node = line.strip().split(',')
            edges.append((from_node, to_node))
    return edges

def main():
    """
    Main function to demonstrate graph operations and interact with the user.
    """
    graph = Graph()
    
    # Parse edges from file
    edges = parse_edges_from_file('cities.txt')
    
    # Add edges to the graph
    for from_node, to_node in edges:
        graph.add_edge(from_node, to_node)
    
    # Display the graph
    print("Graph:")
    graph.display_graph()
    
    # Prompt the user for start and end cities
    start_city = input("\nEnter the starting city: ")
    end_city = input("Enter the destination city: ")
    
    # Perform BFS to find a path
    print(f"\nBFS path from {start_city} to {end_city}:")
    path = graph.bfs(start_city, end_city)
    if path:
        print(" -> ".join(path))
    else:
        print("No path found.")
    
    # Perform DFS to find a path
    print(f"\nDFS path from {start_city} to {end_city}:")
    path = graph.dfs(start_city, end_city)
    if path:
        print(" -> ".join(path))
    else:
        print("No path found.")

if __name__ == "__main__":
    main()