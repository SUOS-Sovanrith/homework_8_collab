numbers = [1,2,3,4,5]

def reverse_ascending(numbers):
    numbers.sort()
    numbers.reverse()
    new_numbers = numbers
    return new_numbers

print(reverse_ascending(numbers))

