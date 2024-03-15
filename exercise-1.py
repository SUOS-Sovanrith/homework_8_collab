def replace_last(numbers):
    replace_last = numbers[-1] + numbers [:-1]
    return replace_last

def main():
    numbers = float(input("Enter you list of number").split())
    print(f"Here is your new list with the last number in the front:",{replace_last(numbers)})

    


