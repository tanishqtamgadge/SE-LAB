## Function to find students who play both cricket and badminton
def both_cricket_badminton(cricket, badminton):
    both = []
    for student in cricket:
        if student in badminton:
            both.append(student)
    return both

# Function to find students who play either cricket or badminton but not both
def either_cricket_or_badminton(cricket, badminton):
    either = []
    for student in cricket:
        if student not in badminton:
            either.append(student)
    for student in badminton:
        if student not in cricket:
            either.append(student)
    return either

# Function to find students who play neither cricket nor badminton
def neither_cricket_nor_badminton(all_students, cricket, badminton):
    neither = []
    for student in all_students:
        if student not in cricket and student not in badminton:
            neither.append(student)
    return neither

# Function to find students who play cricket and football but not badminton
def cricket_football_not_badminton(cricket, football, badminton):
    result = []
    for student in cricket:
        if student in football and student not in badminton:
            result.append(student)
    return result

# Input data
all_students = ['John', 'Emily', 'Alice', 'Bob', 'Eve', 'Charlie', 'Dave', 'Frank', 'Grace']
cricket = ['John', 'Alice', 'Bob', 'Charlie']
badminton = ['Alice', 'Eve', 'Frank', 'Grace']
football = ['John', 'Bob', 'Dave', 'Grace']

# Part a: List of students who play both cricket and badminton
print("a) Students who play both cricket and badminton:", both_cricket_badminton(cricket, badminton))

# Part b: List of students who play either cricket or badminton but not both
print("b) Students who play either cricket or badminton but not both:", either_cricket_or_badminton(cricket, badminton))

# Part c: Number of students who play neither cricket nor badminton
print("c) Number of students who play neither cricket nor badminton:", len(neither_cricket_nor_badminton(all_students, cricket, badminton)))

# Part d: Number of students who play cricket and football but not badminton
print("d) Students who play cricket and football but not badminton:", cricket_football_not_badminton(cricket, football, badminton))
