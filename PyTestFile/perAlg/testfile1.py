import timeit
from random import randint

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def expmod1(a, n, m):
    return (a ** n) % m

def expmod2(a, n, m):
    temp = (a * a) % m
    for x in range(0, n-2):
        temp = (temp * a) % m
    return temp

def expmod3(a, n, m):
    if n == 0:
        return 1
    else:
        d = expmod3(a, n // 2, m)
        # Note that: In here, when the number is huge,
        # Avoiding using math.floor; it will cause the
        # inaccurate float number.
        if n % 2 == 0:
            return (d * d) % m
        else:
            return (d * d * a) % m

# The differences appear, because they use different methods to deal with large number

def flt(n):
    while (True):
        if (expmod3(2,n-1, n) == 1):
            return n
        else:
            n = n + 1


def insert_sort(a):
    for x in range(1, len(a)):
        temp = a[x]
        j = x - 1
        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = temp
    return a

def merge(a, b):
    d = len(a) + len(b)
    c = list(range(d))
    i, j = 0, 0
    for k in range(0, d):
        if i == len(a):
            c[k:d] = b[j:len(b)]
            return c
        elif j == len(b):
            c[k:d] = a[i:len(a)]
            return c

        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
    return c

def merge_sort(a, m, n):
    if n-m == 1:
        return [a[m]]
    else:
        p = (m+n) // 2
        b = merge_sort(a, m, p)
        c = merge_sort(a, p, n)
        d = merge(b, c)
        return d

def mergesort(a):
    return merge_sort(a, 0, len(a))

if __name__ == '__main__':

#if __name__ == '__main__':
    #a = [3,11,93,22,5,31,3,19,13,45,17,13,75,7,2]
    a = [randint(0,100000) for i in range(10000)]

def t1():
    return mergesort(a)

def t2():
    return insert_sort(a)

def t3():
    return a.sort()

timer1 = timeit.Timer('t1()', 'from __main__ import t1')
print('merge sort：', timer1.timeit(5))

timer2 = timeit.Timer('t2()', 'from __main__ import t2')
print('insert sort：', timer2.timeit(5))

timer3 = timeit.Timer('t3()', 'from __main__ import t3')
print('list built-in sort：', timer2.timeit(5))


'''
merge sort： 0.1439364070247393
insert sort： 2.4740234309865627
'''
