Here's a detailed README file for your assignment, covering the heap and graph implementations provided.

---

# Assignment: Heap and Graph Implementations

This project includes implementations for Max Heap, Heap Sort, and Graph traversal. It demonstrates the basics of heap operations, sorting, and graph algorithms, along with examples of how to use each module.

## Project Structure

- **max_heap.py**: Contains the `MaxHeap` class for max heap operations.
- **heap_sort.py**: Contains functions to perform Heap Sort on an array.
- **graphs.py**: Implements a `Graph` class with breadth-first search (BFS) and depth-first search (DFS) for finding paths between nodes, using a file (`cities.txt`) to define edges.

## Requirements

- Python 3.x

## Modules Overview

### 1. MaxHeap (`max_heap.py`)

The `MaxHeap` class is designed to manage a max heap, a complete binary tree where each parent node is greater than or equal to its children. This structure is useful for implementing priority queues and sorting algorithms.

#### Key Methods

- **`insert(data)`**: Inserts a new element into the heap and reorders to maintain the max heap property.
- **`heapify_up(index)`**: Recursively moves an element up the tree to restore heap order.
- **`heapify_iterative(index)`**: Iteratively moves an element up to maintain heap order.
- **`get_height()`**: Returns the height of the heap based on the number of elements.
- **`print_heap()`**: Prints the current elements in the heap.

#### Example Usage

```python
max_heap = MaxHeap()
elements = [10, 20, 5, 30, 25, 40]
for elem in elements:
    max_heap.insert(elem)
max_heap.print_heap()
```

### 2. Heap Sort (`heap_sort.py`)

Heap Sort is an efficient comparison-based sorting algorithm that leverages the max heap structure to sort an array in ascending order.

#### Key Functions

- **`heapify(arr, n, i)`**: Maintains the max heap property by moving an element at index `i` downwards.
- **`build_heap(arr)`**: Converts an array into a max heap.
- **`heap_sort(arr)`**: Sorts an array in-place using the heap sort algorithm.

#### Example Usage

```python
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)
```

### 3. Graph (`graphs.py`)

The `Graph` class implements an unweighted, directed graph structure with BFS and DFS algorithms to find paths between nodes. This class is useful for exploring paths in a network and can be customized for various graph-based applications.

#### Key Classes and Methods

- **`Node`**: Represents a graph node with a value and a list of adjacent nodes.
- **`Graph`**: Represents the graph and provides methods for adding nodes and edges, displaying the graph, and performing BFS and DFS.

  - **`add_node(value)`**: Adds a node to the graph.
  - **`add_edge(from_node, to_node)`**: Adds a directed edge between two nodes.
  - **`display_graph()`**: Prints each node and its neighbors.
  - **`bfs(start_value, end_value)`**: Finds a path from `start_value` to `end_value` using breadth-first search.
  - **`dfs(start_value, end_value)`**: Finds a path using depth-first search.
  - **`parse_edges_from_file(filename)`**: Reads a list of edges from a file and returns them as a list of tuples.

#### Example Usage

To run the graph demo, ensure `cities.txt` (a file containing comma-separated pairs of cities) is in the same directory.

```python
graph = Graph()
edges = parse_edges_from_file('cities.txt')
for from_node, to_node in edges:
    graph.add_edge(from_node, to_node)

graph.display_graph()

# Find paths using BFS and DFS
start_city = "CityA"
end_city = "CityB"
print("BFS path:", graph.bfs(start_city, end_city))
print("DFS path:", graph.dfs(start_city, end_city))
```

### cities.txt

This file contains edges for the graph in the format:

```
CityA,CityB
CityB,CityC
CityA,CityC
```

## How to Run the Code

1. **Max Heap Operations**:
   - Run `max_heap.py`.
   - Follow on-screen instructions to insert elements and display the heap.

2. **Heap Sort**:
   - Run `heap_sort.py`.
   - Enter a list of numbers to see the sorted result.

3. **Graph Operations**:
   - Run `graphs.py`.
   - The script loads the graph structure from `cities.txt` and performs BFS and DFS to find paths.

## Notes

- The code assumes that `cities.txt` is in the same directory as `graphs.py`.
- Modify the input arrays or cities in the example usage sections to customize behavior.
  
## Conclusion

This project covers basic implementations of max heap, heap sort, and graph traversals with BFS and DFS, demonstrating essential data structures and algorithms in Python. These structures are versatile and have numerous applications in fields like networking, pathfinding, and data processing.
