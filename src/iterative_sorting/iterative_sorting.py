# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_i = i
        smallest_i = current_i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(current_i+1, len(arr)):
            if arr[x] < arr[smallest_i]:
                smallest_i = x
        # TO-DO: swap
        arr[current_i], arr[smallest_i] = arr[smallest_i], arr[current_i]
    print(arr)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    index_length = len(arr) - 1
    sorted = True
    while sorted:
        sorted = False
        for i in range(0, index_length):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = True
    print(arr)
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr