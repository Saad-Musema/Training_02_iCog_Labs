import math

class MaxHeap:
    """
    A class to represent a Max Heap.
    """

    def __init__(self):
        """
        Initialize an empty heap.
        """
        self.heap = []
        
    def insert(self, data):
        """
        Insert a new element into the heap.
        
        Parameters:
        data (int): The data to be inserted into the heap.
        """
        self.heap.append(data)
        self.heapify_iterative(len(self.heap) - 1)
        
    def heapify_up(self, index):
        """
        Heapify the element at the given index upwards to maintain the heap property.
        
        Parameters:
        index (int): The index of the element to heapify.
        """
        parent_index = (index - 1) // 2
        
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)
            
    def get_height(self):
        """
        Get the height of the heap.
        
        Returns:
        int: The height of the heap.
        """
        return math.floor(math.log2(len(self.heap))) if self.heap else -1
    
    def heapify_iterative(self, index):
        """
        Heapify the element at the given index upwards iteratively to maintain the heap property.
        
        Parameters:
        index (int): The index of the element to heapify.
        """
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    
    @staticmethod
    def heapify_down(arr, n, i):
        """
        Heapify the element at the given index downwards to maintain the heap property.
        
        Parameters:
        arr (list): The array representation of the heap.
        n (int): The size of the heap.
        i (int): The index of the element to heapify.
        """
        largest = i
        left = 2 * i + 1  
        right = 2 * i + 2  

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            MaxHeap.heapify_down(arr, n, largest)
            
    @staticmethod
    def heapify(arr):
        """
        Convert an array into a heap.
        
        Parameters:
        arr (list): The array to be converted into a heap.
        """
        n = len(arr)
        for i in range((n // 2) - 1, -1, -1):
            MaxHeap.heapify_down(arr, n, i)
        
    def print_heap(self):
        """
        Print the elements of the heap.
        """
        print(self.heap)
        
def main():
    """
    Main function to demonstrate heap operations and interact with the user.
    """
    max_heap = MaxHeap()
    
    # Demonstrate how it works by itself
    elements = [10, 20, 5, 30, 25, 40, 70, 80]
    print("Demonstrating heap operations with predefined elements:")
    for elem in elements:
        print(f"Inserting {elem} into the heap:")
        max_heap.insert(elem)
        max_heap.print_heap()
    
    # Prompt the user to enter a stream of numbers
    user_input = input("\nEnter a stream of numbers separated by spaces: ")
    user_elements = list(map(int, user_input.split()))
    
    for elem in user_elements:
        max_heap.insert(elem)
    
    while True:
        print("\nChoose an operation:")
        print("1. Insert a number")
        print("2. Print the heap")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            num = int(input("Enter the number to insert: "))
            max_heap.insert(num)
        elif choice == '2':
            max_heap.print_heap()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()