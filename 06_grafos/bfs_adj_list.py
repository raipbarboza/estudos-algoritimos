"""BFS em grafo não ponderado representado por lista de adjacência."""


from collections import deque


def bfs(adj: dict[int, list[int]], inicio: int) -> list[int]:
    """Retorna vértices na ordem da primeira visita (nível a nível)."""
    visitados: set[int] = set()
    ordem: list[int] = []
    q: deque[int] = deque([inicio])
    visitados.add(inicio)
    while q:
        u = q.popleft()
        ordem.append(u)
        for v in adj.get(u, []):
            if v not in visitados:
                visitados.add(v)
                q.append(v)
    return ordem


if __name__ == "__main__":
    g = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    print(bfs(g, 2))  # exemplo de ordem a partir do 2
