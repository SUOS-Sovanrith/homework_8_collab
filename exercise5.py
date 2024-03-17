


def reverse_ascending(numbers):

    #we create 2 lists here total is to store the final 
    #and subconsequences is for each of the subsequence in the list
    total = []
    subsequences = []

    #check if the list input is blank or not
    if numbers == []:
        return []

    #loop throught the numbers list
    for x in numbers:

        #check if the subsequences list is empty so that we know have we start the subsequence yet
        #check if the value of x is bigger than the last item or not, if yes then it means that the numbers is ascending subsequence
        if subsequences == [] or x > subsequences[-1]:

            #after either one of the condition of the two is true then we start to add the number in the subsequence list
            subsequences.append(x)

        #if the it reaches the number that is not the ascending subsequence than we add the subsequences list to our result and reverse it
        else:
            total += reversed(subsequences)
            #here we start the new subsequence list from the last one
            subsequences = [x]

    #after we loop through all the numbers we check here to see if there are remaining number in the subsequence list
    #if there are remaining number we reverse it and add in out total list
    total += reversed(subsequences)
    
    return total








        


