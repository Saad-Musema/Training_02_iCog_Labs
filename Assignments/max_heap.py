import math

class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def insert(self, data):
        self.heap.append(data)
        self.heapify_iterative(len(self.heap) - 1)
        
    # This is the task from our in training tasks 
    def heapify_up(self, index):
        parent_index = math.floor(index / 2)
        
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            
            self.heapify_up(parent_index)
            
    def get_height(self):
        return math.floor(math.log2(len(self.heap))) if self.heap else -1
    
    
    # This is Task number 1
    def heapify_iterative(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    
    def heapify_down(arr, n, i):
        # Assume the current node at index i is the largest
        largest = i
        left = 2 * i + 1  
        right = 2 * i + 2  

        # Checks if the left child exists and is greater than the current largest
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if the right child exists and is greater than the current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest is not the current node, swap and continue heapifying down
        if largest != i:
            MaxHeap.heapify_down(arr, n, largest)
            
            
    def heapify(arr):
        n = len(arr)
        
        # STars from the last non-leaf node and applies heapify_down on each node
        for i in range((n // 2) - 1, -1, -1):
            MaxHeap.heapify_down(arr, n, i)
            
      # Recursively heapify the affected subtree

        
    def print_heap(self):
        print(self.heap)
        
if __name__ == "__main__":

    max_heap = MaxHeap()
    
    # Insert elements
    elements = [10, 20, 5, 30, 25, 40, 70, 80]
    for elem in elements:
        print(f"Inserting {elem} into the heap:")
        max_heap.insert(elem)
        max_heap.print_heap()
            
            

        
        