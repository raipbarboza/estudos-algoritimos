"""Insertion sort: bom para listas pequenas ou quase ordenadas. O(n^2) pior caso."""


def insertion_sort(arr: list[int]) -> list[int]:
    a = arr[:]
    for i in range(1, len(a)):
        chave = a[i]
        j = i - 1
        while j >= 0 and a[j] > chave:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = chave
    return a


if __name__ == "__main__":
    print(insertion_sort([5, 2, 4, 6, 1, 3]))
