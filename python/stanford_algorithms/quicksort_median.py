##Quicksort - median of first, last and middle elements of array as pivot  

def median_of_three(array, f, l):
    m = f + (l - f)/2
    if array[f] <= array[m] <= array[l] or array[l] <= array[m] <= array[f]:
        return m
    elif array[m] <= array[f] <= array[l] or array[l] <= array[f] <= array[m]:
        return f
    else:
        return l

def partition(array, left, right):
    if right - left > 1:
        temp = median_of_three(array, left, right-1)
        array[left], array[temp] = array[temp], array[left]
        pivot = array[left]
        i = left+1
        for j in xrange(left+1, right):
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i = i + 1
        array[left], array[i-1] = array[i-1], array[left]
        partition(array, left, i-1)
        partition(array, i, right)
    

def quicksort(array):
    partition(array, 0, len(array))


def read_array():
    f = open("quicksort.txt", "r+")
    array = []
    for line in f:
        array.append(int(line))
    f.close()
    return array


if __name__ == "__main__":
    array = read_array()
    quicksort(array)



