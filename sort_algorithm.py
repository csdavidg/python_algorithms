# Selection sort algorithm
def selection_sort(A):
    N = len(A)
    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if A[j] < A[min_index]:
                min_index = j

        A[i], A[min_index] = A[min_index], A[i]


# Similar or equal to bubble sort
def insertion_sort(A):
    N = len(A)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if A[j-1] <= A[j]:
                break
            A[j], A[j-1] = A[j-1], A[j]


def merge_sort(A):
    aux = [None] * len(A)

    def rsort(lo, hi):
        if hi <= lo:
            return

        mid = (lo+hi) // 2
        rsort(lo, mid)
        rsort(mid+1, hi)
        merge(lo, mid, hi)

    def merge(lo, mid, hi):
        aux[lo:hi+1] = A[lo:hi+1]

        left = lo
        right = mid+1

        for i in range(lo, hi+1):
            if left > mid:
                A[i] = aux[right]
                right += 1
            elif right > hi:
                A[i] = aux[left]
                left += 1
            elif aux[right] < aux[left]:
                A[i] = aux[right]
                right += 1
            else:
                A[i] = aux[left]
                left += 1

    rsort(0, len(A)-1)


"""

A = [2,4,1,6,8,5,3,7]
merge_sort(A)
for val  in A:
    print(val)
"""


def partition(A, lo, hi, idx):
    """Partition using A[idx] as value."""
    if lo == hi:
        return lo

    A[idx], A[lo] = A[lo], A[idx]    # swap into position
    i = lo
    j = hi + 1
    while True:
        while True:
            i += 1
            if i == hi:
                break
            if A[lo] < A[i]:
                break

        while True:
            j -= 1
            if j == lo:
                break
            if A[j] < A[lo]:
                break

        if i >= j:
            break
        A[i], A[j] = A[j], A[i]

    A[lo], A[j] = A[j], A[lo]
    return j


def quick_sort(A):

    def qsort(lo, hi):
        if hi <= lo:
            return

        pivot_idx = lo
        location = partition(A, lo, hi, pivot_idx)

        qsort(lo, location-1)
        qsort(location+1, hi)

    qsort(0, len(A)-1)

A = [2,4,1,6,8,5,3,7]
quick_sort(A)
for val  in A:
    print(val)