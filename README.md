# Estudos de algoritmos

Repositório para estudar algoritmos e estruturas de dados, organizado do mais simples ao mais avançado. Os exemplos estão em **Python 3.10+** (usa anotações como `int | None`).

## Pré-requisitos

- [Python 3.10](https://www.python.org/downloads/) ou superior instalado e disponível no `PATH` como `python`.

## Como executar um exemplo

Na raiz do projeto:

```powershell
python 01_fundamentos\busca_linear.py
```

Em sistemas Unix:

```bash
python3 01_fundamentos/busca_linear.py
```

## Estrutura do projeto

| Pasta | Tema | Ficheiro |
|--------|------|----------|
| `01_fundamentos` | Percorrer dados, noção de custo temporal | `busca_linear.py` |
| `02_busca` | Dividir para conquistar em vetor ordenado | `busca_binaria.py` |
| `03_ordenacao` | Ordenação por comparação | `insertion_sort.py` |
| `04_estruturas` | Fila FIFO | `fila.py` |
| `05_recursao_dp` | Recursão com memoização | `fib_memo.py` |
| `06_grafos` | Percursos em grafos (BFS) | `bfs_adj_list.py` |

## Roteiro sugerido (para ir acrescentando código)

1. **Fundamentos:** notação assintótica (O, Ω, Θ), invariantes de loop.
2. **Busca:** variantes de busca binária (primeira/última posição, resposta em espaço contínuo).
3. **Ordenação:** merge sort, quick sort, counting sort; estabilidade e casos de uso.
4. **Estruturas:** pilha, deque, heap, trie, Union-Find.
5. **Recursão e DP:** backtracking, tabelas bottom-up, problemas clássicos (mochila, LIS, distância de edição).
6. **Grafos:** DFS, caminhos mínimos (Dijkstra), ordenação topológica, SCC (avançado).

Cada novo tópico pode ganhar um ficheiro `.py` na pasta correspondente, com um bloco `if __name__ == "__main__":` para testar à mão.

## Licença

Uso livre para estudo pessoal.
