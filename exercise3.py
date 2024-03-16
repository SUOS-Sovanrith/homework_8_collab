def remove_all_after(numbers, n):
    if n in numbers:
        index_n = numbers.index(n)
        return numbers[:index_n + 1]
    else:
        return numbers
def main(): 
    input_list = input("Enter a list of numbers: ")
    n = int(input("Enter the border element: "))

    numbers = [int(num) for num in input_list.split(',')]

    print(f"Your new list after removing the elements after {n} is:",remove_all_after(numbers, n))

if __name__ == "__main__":
    main()