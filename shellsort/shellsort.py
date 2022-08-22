

def shellsort(arr):
    N = len(arr)

    # We find the shell size to start with.
    # This assumes we use the sequence
    # 1,4,13,40,... 3n + 1,...
    h = 1 
    while h < N // 3:
        h = 3 * h + 1
    
    # Now for each shell size h, we h-sort the array.
    while h > 0:
        for i in range(h, N):
            j = i
            # Swap the adjacent elements in the shell as needed.
            while j >= h and arr[j] < arr[j-h]:
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j -= h
        h = h // 3
    return arr
