##Counts the number of inversions (reversals of position from sorted order) 
##in the input file whilst sorting the array using mergesort.

def merge_and_count_split_inv(b, c):
    sorted_list = []
    count = 0
    i = 0
    j = 0
    len_b = len(b)
    len_c = len(c)
    while i < len_b and j < len_c:
        if b[i] <= c[j]:
            sorted_list.append(b[i])
            i += 1
        else:
            sorted_list.append(c[j])
            j += 1
            count += len_b - i
    sorted_list += b[i:]
    sorted_list += c[j:]
    return sorted_list, count

def sort_and_count(array):
    if len(array) == 1:
        return array, 0
    else:
        middle = len(array) // 2
        b, x = sort_and_count(array[:middle])
        c, y = sort_and_count(array[middle:])
        d, z = merge_and_count_split_inv(b, c)
    return d, (x + y + z)

def read_array():
    f = open("IntegerArray.txt", "r+")
    array = []
    for line in f:
        array.append(int(line))
    f.close()
    return array

if __name__ == "__main__":
    array = read_array()
    print sort_and_count(array)[1]




