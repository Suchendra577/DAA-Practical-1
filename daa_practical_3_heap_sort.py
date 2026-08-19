import time

def heapify(arr, n, i):
    """
    To heapify a subtree rooted with node i, which is an index in arr[].
    n is the size of the heap.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child = 2*i + 1
    right = 2 * i + 2  # right child = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Main function to perform Heap Sort on array arr.
    """
    n = len(arr)

    # Build a maxheap. Start from the last non-leaf node and heapify upwards.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0) # Call max heapify on the reduced heap

    return arr

if __name__ == "__main__":
    print("=" * 50)
    print("DAA Practical 3: Heap Sort Algorithm")
    print("=" * 50)
    
    try:
        # Get user input for the array
        input_str = input("Enter numbers separated by spaces: ")
        user_array = list(map(int, input_str.split()))

        if not user_array:
            print("No numbers provided.")
        else:
            print(f"\nOriginal array: {user_array}")

            start_time = time.time()
            sorted_array = heap_sort(user_array)
            end_time = time.time()

            print(f"Sorted array:   {sorted_array}")
            print(f"Execution time: {end_time - start_time:.6f} seconds")
            print("-" * 50)
            print("Time Complexity:  O(N log N) [Best / Average / Worst]")
            print("Space Complexity: O(1) [Auxiliary Space]")
    except ValueError:
        print("Invalid input! Please enter integers separated by spaces.")
