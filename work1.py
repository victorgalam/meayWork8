def foo():
    wrkers = {"alice":["bob","shimi"],'bob':['tom','buy'],"shimi":['assaf','almog']}

def find_minimum(numbers):
    if not numbers:
        return None  # במקרה שהרשימה ריקה
    min_number = numbers[0]
    for number in numbers[1:]:
        if number < min_number:
            min_number = number
    return min_number

# דוגמה לשימוש
numbers = [5, 3, 8, 2, 9, 1]
print(find_minimum(numbers))