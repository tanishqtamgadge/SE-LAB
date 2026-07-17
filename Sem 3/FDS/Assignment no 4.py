# Function for Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Function for Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Function to display the top five scores
def display_top_five(arr):
    # Display the last five elements of the sorted array (top scores)
    top_five = arr[-5:] if len(arr) >= 5 else arr
    print("Top five scores:")
    for score in reversed(top_five):
        print(score)

# Example usage
percentages = [75.5, 88.3, 90.6, 82.1, 67.8, 91.2, 78.9, 85.0, 94.5, 72.4]

# Selection Sort
print("Using Selection Sort:")
selection_sorted = percentages.copy()
selection_sort(selection_sorted)
print("Sorted percentages:", selection_sorted)
display_top_five(selection_sorted)

# Bubble Sort
print("\nUsing Bubble Sort:")
bubble_sorted = percentages.copy()
bubble_sort(bubble_sorted)
print("Sorted percentages:", bubble_sorted)
display_top_five(bubble_sorted)

