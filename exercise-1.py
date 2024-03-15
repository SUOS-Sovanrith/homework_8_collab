def replace_last(numbers):
    if len(numbers) == 0 and len(numbers) == 1:
        return numbers
    else:
        replace_last = numbers[-1:] + numbers [:-1]
        return replace_last

def main():
    numbers = input("Enter you list of number:").split()

    print(f"Here is your list with the last digit in the front:",replace_last(numbers))


if __name__ == "__main__":
    main()


