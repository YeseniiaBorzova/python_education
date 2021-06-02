"""Module contains binary search, quick sort and factorial functions"""


def binary_search(arr, elem):
    """function that performs binary search of element and returns its index"""
    start = 0
    end = len(arr) - 1
    mid = 0
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] < elem:
            start = mid + 1
        elif arr[mid] > elem:
            end = mid - 1
        else:
            return mid
    raise ValueError("Element not found")


def partition(arr, l, h):
    """help function that returns partition index to quick sort"""
    i = (l - 1)
    x = arr[h]
    for k in range(l, h):
        if arr[k] <= x:
            i += 1
            arr[i], arr[k] = arr[k], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1


def quick_sort_iter(arr, l, h):
    """function that performs quick sort of array"""
    size = h - l + 1
    stack = [0] * size
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partition(arr, l, h)
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


def factorial(n):
    """function to calculate factorial of number"""
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == "__main__":
    a = [2, 5, 8, 11, 39, 110]
    res = binary_search(a, 39)
    print(res)
    a = [22, 1, 1, 8, 16, 167, 125, 14, 3]
    n = len(a)
    quick_sort_iter(a, 0, n-1)
    print(a)
    print(factorial(6))
