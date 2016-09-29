##Quicksort - first element of array as pivot 

def partition(array, left, right):
    if right - left > 1:
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
    
