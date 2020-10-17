def exc(array, pos, tar):
    # This is for exchanging the position of arrays
    if pos > tar:
        return exc(array, tar, pos)
    elif pos == tar :
        return array

    if pos < 0 or tar < 0:
        pass

    temp1 = array.pop(pos)
    temp2 = array.pop(tar - 1)
    array.insert(pos, temp2)
    array.insert(tar, temp1)
    return array

def merge(arr1, arr2):

    pass
