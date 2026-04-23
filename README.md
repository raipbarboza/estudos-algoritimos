# estudos-algoritimos

Estudos práticos de algoritmos e lógica de programação baseados no livro **Entendendo Algoritmos** de Aditya Y. Bhargava, com implementações em Python.

---

## Sobre o livro

**Entendendo Algoritmos: Um guia ilustrado para programadores e outros curiosos** é um dos melhores pontos de entrada para algoritmos — sem páginas de provas matemáticas, com ilustrações e exemplos práticos em Python. O livro cobre desde pesquisa binária e notação Big O até grafos, programação dinâmica e algoritmos gulosos.

---

## Estrutura do repositório

Os arquivos `.py` serão adicionados gradualmente conforme o estudo de cada capítulo.

| Pasta | Tema | Ficheiro |
|-------|------|----------|
| `cap01-introducao` | Pesquisa binária e notação Big O | `pesquisa_binaria.py` |
| `cap02-ordenacao` | Ordenação por seleção - arrays e listas encadeadas | `ordenacao_selecao.py` |
| `cap03-recursao` | Recursão - funções que chamam a si mesmas | `fatorial_recursivo.py` |
| `cap04-quicksort` | Dividir e conquistar - Quicksort | `quicksort.py` |
| `cap05-tabelas-hash` | Tabelas hash - dicionários em Python | `tabela_hash.py` |
| `cap06-pesquisa-em-largura` | Grafos e busca em largura (BFS) | `bfs_grafos.py` |
| `cap07-dijkstra` | Algoritmo de Dijkstra - caminhos mínimos | `dijkstra.py` |
| `cap08-algoritmos-gulosos` | Algoritmos gulosos - cobertura de conjuntos | `conjuntos_guloso.py` |
| `cap09-programacao-dinamica` | Programação dinâmica - problema da mochila | `mochila_dp.py` |
| `cap10-knn` | K-vizinhos mais próximos (KNN) - classificação | `knn_classificacao.py` |
| `extras` | Jogos e exemplos extras | `jogo_adivinhacao.py` |

---

## Progresso

| Capítulo | Tema | Status |
|----------|------|--------|
| 01 | Introdução a algoritmos — pesquisa binária e notação Big O | ⬜ Pendente |
| 02 | Ordenação por seleção — arrays e listas encadeadas | ⬜ Pendente |
| 03 | Recursão | ⬜ Pendente |
| 04 | Quicksort — dividir e conquistar | ⬜ Pendente |
| 05 | Tabelas hash | ⬜ Pendente |
| 06 | Pesquisa em largura (BFS) e grafos | ⬜ Pendente |
| 07 | Algoritmo de Dijkstra | ⬜ Pendente |
| 08 | Algoritmos gulosos | ⬜ Pendente |
| 09 | Programação dinâmica | ⬜ Pendente |
| 10 | K-vizinhos mais próximos (KNN) | ⬜ Pendente |

**Legenda:** ⬜ Pendente / 🟡 Em andamento / ✅ Concluído

---

## Conexão com os projetos principais

Os algoritmos estudados aqui têm aplicação direta nos projetos de dados ESG:

| Algoritmo | Aplicação no CarbonTrack BR |
|-----------|-----------------------------|
| Pesquisa binária | Busca eficiente em grandes datasets de emissões |
| Tabelas hash | Cruzamento rápido CVM × ISE por CNPJ |
| BFS / Grafos | Mapeamento de cadeia de fornecedores (Scope 3) |
| KNN | Classificação de empresas por perfil de risco ESG |
| Programação dinâmica | Otimização de portfólios de crédito de carbono |

---

## Como executar

```bash
git clone https://github.com/raipbarboza/estudos-algoritimos.git
cd estudos-algoritimos

# Executar um exemplo (quando os arquivos forem adicionados)
python cap01-introducao/pesquisa_binaria.py
