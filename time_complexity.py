
""" def foo(n):
    sq_root = int(math.sqrt(n))
    for i in range:
        pass """
# NOTE: ^^^ incomplete.


def bar(n):
    s = 0
    for i in range(n):
        for j in range(n):  # time complexity here is O(n^2)
            s += i * j
    return s


def merge_sort(arr):  # time complexity here is O(n log n)
    print(f"SORTING: {arr}")
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    left = merge_sort(left)
    right = merge_sort(right)
# Merge them back together
    # return merge(left, right)
