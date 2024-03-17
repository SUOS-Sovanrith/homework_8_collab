def chunking_by(numbers, chunck):
    
    result = []

    test_list = []

    for i in numbers:

        test_list.append(i)

        # check if the length of test_list is equal to chunck

        if len(test_list) == chunck:

            result.append(test_list)    # if true, add those length in test_list to the result list

            test_list = []

    # after done looping the length = chunck, we check if test_list is true or false

    if len(test_list) > 0:

        result.append(test_list)      # if true, we add to the result

        test_list = []

    else:

        return result       # if false, we show the result

    return result

print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))


