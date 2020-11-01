#sorting algorithms in python

import time
import argparse
from random import randint


def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)


def run_sorting_algorithm(algorithm, array):
    function_mappings = {
            'merge_sort': merge_sort,
            'quicksort': quicksort,
            }

    def select_function(strs):
        while True:
            try:
                return function_mappings[strs]
            except KeyError:
                raise ValueError('Invalid algorithm, try again.')
    #
    # Execute the code and return the time
    # in seconds that the execution took
    start_time = time.time()
    sorted_array = select_function(algorithm)(array)
    end_time = time.time()
    times = end_time-start_time

    # Finally, display the result of the algorithm, name of the algorithm and the
    # time it took to run
    return f"\nSorted Items: {sorted_array}\n\nAlgorithm: {algorithm}. \nExecution time: {times}"



if __name__ == "__main__":
# Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    
    #array = ['a', 'A', 'b', 'R', 'z']

    parser = argparse.ArgumentParser(prog='sort', description="Sort items")
    # Add the arguments
    parser.add_argument('--sort-type',
                       metavar='sort_type',
                       type=str,
                       help='type of sorting algorithm to use [merge_sort or quicksort]',
                       required=True)


    parser.add_argument('--items',
                        metavar='items',
                        action='store',
                        nargs='?',
                        help='items to sort E.G: \'1,6,2,9,4\'',
                        required=True)

    # Execute the parse_args() method
    args = parser.parse_args()

    # print(args)

    if (args.sort_type != None or args.items != None):
        algorithm = args.sort_type
        array = args.items.split(',')
    else:
        algorithm = "quicksort"
        array = []
        # Call the function using the name of the sorting algorithm
        # and the array just created
    
    print(
            run_sorting_algorithm(algorithm=algorithm, array=array)
            )






