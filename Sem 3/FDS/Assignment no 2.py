# Function to calculate the average score of the class
def average_score(marks):
    total = sum(marks)
    count = len(marks)
    return total / count if count > 0 else 0

# Function to find the highest and lowest score in the class
def highest_lowest_score(marks):
    return max(marks), min(marks)

# Function to count the number of students who were absent (represented by -1)
def count_absent(marks):
    return marks.count(-1)

# Function to find the mark with the highest frequency
from collections import Counter
def highest_frequency_mark(marks):
    marks_without_absent = [mark for mark in marks if mark != -1]
    frequency = Counter(marks_without_absent)
    most_common = frequency.most_common(1)  # Returns a list of tuples (mark, frequency)
    return most_common[0] if most_common else None

# Main function to input marks and compute required statistics
def main():
    # Input the number of students
    N = int(input("Enter the number of students: "))
    
    marks = []
    
    # Input the marks scored by N students
    print("Enter the marks of students (-1 for absent):")
    for i in range(N):
        mark = int(input(f"Student {i+1}: "))
        marks.append(mark)
    
    # Filtering out absent students for average, highest, and lowest calculations
    present_marks = [mark for mark in marks if mark != -1]
    
    # a) Average score of the class
    avg = average_score(present_marks)
    print(f"\nAverage score of the class: {avg:.2f}")
    
    # b) Highest and lowest score of the class
    if present_marks:
        highest, lowest = highest_lowest_score(present_marks)
        print(f"Highest score in the class: {highest}")
        print(f"Lowest score in the class: {lowest}")
    else:
        print("No students present to calculate highest and lowest score.")
    
    # c) Count of students who were absent for the test
    absent_count = count_absent(marks)
    print(f"Number of students absent for the test: {absent_count}")
    
    # d) Display mark with the highest frequency
    most_frequent_mark = highest_frequency_mark(marks)
    if most_frequent_mark:
        mark, freq = most_frequent_mark
        print(f"Mark with the highest frequency: {mark} (appeared {freq} times)")
    else:
        print("No marks available to calculate frequency.")

if __name__ == "__main__":
    main()
