def exc(array, pos, tar):
    # This is for exchanging the position of arrays
    if pos > tar:
        return exc(array, tar, pos)
    elif pos == tar:
        return array
    if pos < 0 or tar < 0:
        pass

    temp1 = array.pop(pos)
    temp2 = array.pop(tar - 1)
    array.insert(pos, temp2)
    array.insert(tar, temp1)
    return array


def insert_sort(array):
    index = len(array)
    for x in range(1, index):
        for y in range(x-1, -1, -1):
            if array[x] < array[y]:
                exc(array, y, x)
            else:
                pass
    return array


if __name__ == '__main__':
    L = [3, 8, 5, 25, 9, 17, 10, 11]
    print(insert_sort(L))
