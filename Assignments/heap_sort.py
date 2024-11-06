import math

def heapify(arr, n, i):
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
        heapify(arr, n, largest)

def build_heap(arr):
    """
    Convert an array into a heap.
    
    Parameters:
    arr (list): The array to be converted into a heap.
    """
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    """
    Perform heap sort on the given array.
    
    Parameters:
    arr (list): The array to be sorted.
    """
    n = len(arr)
    build_heap(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

def main():
    """
    Main function to demonstrate heap sort.
    """
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    heap_sort(arr)
    print("Sorted array:", arr)
    
    
     # Prompt the user to enter a stream of numbers
    user_input = input("\nEnter a stream of numbers separated by spaces: ")
    user_elements = list(map(int, user_input.split()))
    
    heap_sort(user_elements)
    print(user_elements)

if __name__ == "__main__":
    main()