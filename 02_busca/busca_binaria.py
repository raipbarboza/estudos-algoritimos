"""Busca binária em vetor ordenado. O(log n)."""


def busca_binaria(arr: list[int], alvo: int) -> int | None:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == alvo:
            return mid
        if arr[mid] < alvo:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


if __name__ == "__main__":
    v = [1, 3, 5, 7, 9]
    print(busca_binaria(v, 7))  # 3
    print(busca_binaria(v, 4))  # None
