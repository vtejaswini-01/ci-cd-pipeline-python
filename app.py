def calculate_average(marks):
    return sum(marks) / len(marks)

def find_highest(marks):
    return max(marks)

def find_lowest(marks):
    return min(marks)

def is_pass(average):
    if average >= 40:
        return True
    else:
        return False