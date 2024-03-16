def index_power(numbers, n):
    try:
        return pow(numbers[n], n)
    except IndexError:
        return -1
    
def main():
    numbers = []
    
    print("Welcome!")
    print("Provide a list of numbers and an index number, and you will get the index-th power of the element in the array with the index")
    
    # loop for amount input error handling
    while True:
        try:
            amount = int(input("\nEnter number of elements in your list: "))
        except ValueError:
            print("Invalid Input! Must be a whole number.")
        else:
            break
    
    for i in range(0, amount):
    # loop for element input error handling
        while True:
            try:
                element = int(input(f"Enter number {i+1}: "))
            except ValueError:
                print("Invalid Input! Must be an integer.")
            else:
                break
            
        numbers.append(element)
    
    # loop for index number input error handling
    while True:
        try:
            n = int(input("Input the Index number: "))
        except ValueError:
            print("Invalid Input! Must be an integer.")
        else:
            break
        
    print(f"\nThe Result : {index_power(numbers, n)}")
    
    
if __name__ == "__main__":
    main()

