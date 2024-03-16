numbers = [5, 7, 10, 4, 2, 7, 8, 1, 3]

def reverse_ascending(numbers):
    result = []
    temp = []

    if numbers == []:
        return []
    
    else:
        for x in numbers:
            if x > numbers[-1]:
                temp.append(x)
            else:
                temp.reverse()
                temp.append(x)
                result = temp
                
    return result








        

print(reverse_ascending(numbers))

