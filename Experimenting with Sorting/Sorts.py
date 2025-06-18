import time


def bubble_sort(lst):
    n = len(lst)
    tmp = lst[:]
    start = time.time()
    
    # Outer loop for each pass
    for i in range(n - 1):
        # Flag to track if any swap happens
        swapped = False
        
        # Inner loop for comparing adjacent elements
        for j in range(n - 1 - i):  # Optimized by reducing the comparison range in each iteration
            if tmp[j] > tmp[j + 1]:
                # Swap if elements are in wrong order
                tmp[j], tmp[j + 1] = tmp[j + 1], tmp[j]
                swapped = True  # Mark swapped as True since a swap occurred
        
        # If no swap happened in the inner loop, the list is already sorted
        if not swapped:
            break  # Exit the loop early
    
    diff = time.time() - start
    print(f"Sorting took {diff} seconds")
    return tmp  # Return the sorted list


def insertion_sort(lst):
    start = time.time()
    n = len(lst)
    for x in range(1, n):
        y = x
        while y > 0 and lst[y] < lst[y - 1]:
            lst[y], lst[y - 1] = lst[y - 1], lst[y]
            y -= 1
    diff = time.time() - start
    print(diff)

def merge_sort(array):
    if len(array) <= 1:
        return array

    middle_index = len(array) // 2
    left_array = merge_sort(array[:middle_index])
    right_array = merge_sort(array[middle_index:])

    return merge(left_array, right_array)

def merge(left, right):
    left_index, right_index = 0, 0
    sorted_array = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])
    return sorted_array

def read_array_from_file(path):
    try:
        with open(path, 'r') as file:
            contents = file.read()
            numbers = [int(num) for num in contents.split()]
        return numbers
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def read_from_arrays(array):
    for elem in array:
        path = f"Algorithms/Experimenting with Sorting/Data/{elem}.txt"  # Adjust directory path as needed
        numbers = read_array_from_file(path)
        if numbers is not None:
            numbers1 = numbers.copy()
            numbers2 = numbers.copy()
            numbers3 = numbers.copy()
            print(f"File Started {elem}")
            # print("Bubble Sort")
            # bubble_sort(numbers)
            # print("")
            # print("InsertionSort")
            # insertion_sort(numbers1)
            # print("")
            # print("Merge Sort")
            # start = time.time()
            # _ = merge_sort(numbers2)
            # diff = time.time() - start
            # print(diff)c
            print("Heap Sort")
            heapSort(numbers)
            print("")
            if elem == "RandomNumbersLarge" or elem == "RandomNumbersSmall":
                print("Quick Sort")
                start = time.time()
                quickSort(numbers1, min(numbers1), max(numbers1))
                diff = time.time() - start
                print(diff)
                print("")
                
            print("Counting Sort")
            countingSort(numbers2)
            print("")
            print("Bucket Sort")
            bucketSort(numbers3)
            print("")
            print("")

file_names = ["SortedRandomNumbersSmall",
              "RandomNumbersSmall",
              "ReversedRandomNumbersSmall",
              "SortedRandomNumbersLarge",
              "RandomNumbersLarge",
              "ReversedRandomNumbersLarge"]


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    start = time.time()
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        
    diff = time.time() - start
    print(diff)
    
    
def quickSort(arr, low, high):
    while low < high:
        # Hoare partitioning
        pivot = partitionHoare(arr, low, high)
        # Recursively sort the smaller part, iterate for the larger
        if pivot - low < high - pivot:
            quickSort(arr, low, pivot)
            low = pivot + 1
        else:
            quickSort(arr, pivot + 1, high)
            high = pivot


def partitionHoare(arr, low, high):
    pivot = arr[low]
    left = low - 1
    right = high + 1
    while True:
        # Move left until an element greater than
        # the pivot is found
        left += 1
        while arr[left] < pivot:
            left += 1
        
        # Move right until an element less than
        # the pivot is found
        right -= 1
        while arr[right] > pivot:
            right -= 1

        # If two pointers met.
        if left >= right:
            return right
        
        # Swap elements left and right
        arr[left], arr[right] = arr[right], arr[left]



def countingSort(arr):
    start = time.time()
    # Find the maximum number to know the range of the array
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m  # Initialize count array with all zeros
    
    # Store the count of each element
    for a in arr:
        count[a] += 1

    # Store the cummulative count
    for i in range(1, m):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array, 
    # place the elements in output array
    output = [0] * len(arr)
    for a in reversed(arr):
        output[count[a] - 1] = a
        count[a] -= 1
    diff = time.time() - start
    print(diff)
    return output

def bucketSort(arr):
    start = time.time()
    # Create buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Find the maximum and minimum elements to scale the elements to [0, 1)
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val

    # Handle the edge case where all elements are the same
    if range_val == 0:
        return arr

    # Insert elements into their respective buckets
    for i in range(len(arr)):
        # Scale the element to the [0, 1) range based on the min and max values
        index = int(((arr[i] - min_val) / range_val) * (bucket_count - 1))
        buckets[index].append(arr[i])

    # Sort the elements of each bucket and concatenate
    sorted_array = []
    for i in range(bucket_count):
        sorted_bucket = sorted(buckets[i])
        sorted_array.extend(sorted_bucket)
    diff = time.time() - start
    print(diff)
    return sorted_array




read_from_arrays(file_names)
