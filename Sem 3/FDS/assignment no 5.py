# Function for Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Function for Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

percentages = [72.3, 88.9, 94.1, 67.5, 76.4, 81.2, 93.3, 89.5, 79.8, 85.7]

# Insertion Sort
print("Using Insertion Sort:")
insertion_sorted = percentages.copy()
insertion_sort(insertion_sorted)
print("Sorted percentages:", insertion_sorted)

# Shell Sort
print("\nUsing Shell Sort:")
shell_sorted = percentages.copy()
shell_sort(shell_sorted)
print("Sorted percentages:", shell_sorted)
