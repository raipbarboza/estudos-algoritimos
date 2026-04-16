"""Fila FIFO com collections.deque — O(1) nas pontas."""


from collections import deque


class Fila:
    def __init__(self) -> None:
        self._d: deque[int] = deque()

    def enfileirar(self, x: int) -> None:
        self._d.append(x)

    def desenfileirar(self) -> int:
        return self._d.popleft()

    def vazia(self) -> bool:
        return len(self._d) == 0


if __name__ == "__main__":
    q = Fila()
    q.enfileirar(1)
    q.enfileirar(2)
    print(q.desenfileirar(), q.desenfileirar())  # 1 2
