"""Busca linear: percorre o vetor até achar o alvo. O(n)."""


def busca_linear(arr: list[int], alvo: int) -> int | None:
    for i, x in enumerate(arr):
        if x == alvo:
            return i
    return None


if __name__ == "__main__":
    v = [3, 1, 4, 1, 5]
    print(busca_linear(v, 4))  # 2
    print(busca_linear(v, 9))  # None
