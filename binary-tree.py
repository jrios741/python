def linear_search(ordered_list: list, search_value: int):
    
    for i, element in enumerate(ordered_list):
        if element == search_value:
            print("Found!", element)
            return element
        elif element > search_value:
            print("Nope")
            return None


    
    print("Nope")
    return None

def binary_search(ordered_list: list, search_value: int):

    lower_bound = 0
    upper_bound = len(ordered_list) - 1

    while lower_bound <= upper_bound:
        
        midpoint = (upper_bound + lower_bound) // 2

        midpoint_value = ordered_list[midpoint]

        if search_value < midpoint_value:
            upper_bound = midpoint - 1
        elif search_value > midpoint_value:
            lower_bound = midpoint + 1
        elif search_value == midpoint_value:
            print(search_value)
            return
        
        print("Not found!")
        return


def main():
    
    binary_search([1, 2, 3, 4, 5, 6, 7, 8 , 9], 10)
    return
    

main()