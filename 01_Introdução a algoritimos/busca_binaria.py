def busca_binaria(lista, item):
    """
    Busca um item em uma lista ORDENADA usando o algoritmo de busca binária.
    
    Como funciona: a cada tentativa, elimina metade da lista restante.
    É como procurar uma palavra no dicionário - você não olha página por página!
    
    Complexidade: O(log n) - muito mais rápido que busca linear O(n)
    
    Args:
        lista: Lista ORDENADA de elementos (crescente)
        item: Valor que queremos encontrar
    
    Returns:
        Índice do item se encontrado, None caso contrário
    """
    
    # PASSO 1: Definir os limites da busca
    # "baixo" é o índice do início da nossa "zona de busca"
    # Começa em 0 (primeiro elemento da lista)
    baixo = 0
    
    # "alto" é o índice do fim da nossa "zona de busca"  
    # Começa no último índice (len - 1 porque índices começam em 0)
    # Ex: lista com 5 elementos → último índice é 4
    alto = len(lista) - 1
    
    # PASSO 2: Loop principal - continua ENQUANTO ainda houver elementos para buscar
    # Quando baixo > alto, significa que a "zona de busca" está vazia (não encontrou)
    while baixo <= alto:
        
        # PASSO 3: Calcular o ponto do meio (o "chute")
        # // é divisão inteira (descarta decimal)
        # Ex: (0 + 4) // 2 = 4 // 2 = 2 (terceiro elemento)
        meio = (baixo + alto) // 2
        
        # PASSO 4: "Chutar" o valor que está no meio da lista
        chute = lista[meio]
        
        # PASSO 5: Verificar se acertou!
        # Se o chute for igual ao item que procuramos... VITÓRIA!
        if chute == item:
            return meio  # Retorna a POSIÇÃO (índice) onde o item está
        
        # PASSO 6: Se chutou ALTO demais (chute > item)
        # Significa que o item está na METADE ESQUERDA da lista
        # Então ajustamos o limite SUPERIOR (alto) para uma posição antes do meio
        # Ex: lista [1,3,5,7,9], buscando 3, chute=5 (muito alto)
        #     nova zona: [1,3] (alto vira 1, índice do 3)
        if chute > item:
            alto = meio - 1  # Descarta metade direita inteira!
        
        # PASSO 7: Se chutou BAIXO demais (chute < item)  
        # Significa que o item está na METADE DIREITA da lista
        # Então ajustamos o limite INFERIOR (baixo) para uma posição depois do meio
        # Ex: lista [1,3,5,7,9], buscando 7, chute=5 (muito baixo)
        #     nova zona: [7,9] (baixo vira 3, índice do 7)
        else:
            baixo = meio + 1  # Descarta metade esquerda inteira!
    
    # PASSO 8: Se saiu do loop (baixo > alto), o item não existe na lista
    # Retorna None (nada) indicando que não encontrou
    return None


# ============ TESTES PARA VISUALIZAR O FUNCIONAMENTO ============

# Lista ORDENADA (requisito fundamental para busca binária!)
# Se a lista não estiver ordenada, o algoritmo NÃO funciona!
minha_lista = [1, 3, 5, 7, 9]

print("=== BUSCA BINÁRIA - PASSO A PASSO ===\n")

# TESTE 1: Buscar o número 3 (que EXISTE na lista)
print("TESTE 1: Buscando o número 3")
print("-" * 40)
print(f"Lista: {minha_lista}")
print(f"Procurando por: 3\n")

# Simulação mental do que acontece:
# Iteração 1: baixo=0, alto=4, meio=2, chute=5 → 5 > 3? SIM → alto=1
# Iteração 2: baixo=0, alto=1, meio=0, chute=1 → 1 > 3? NÃO → baixo=1  
# Iteração 3: baixo=1, alto=1, meio=1, chute=3 → ACERTOU! Retorna índice 1

resultado = busca_binaria(minha_lista, 3)
print(f"Resultado: índice {resultado} (valor {minha_lista[resultado]})")
print("Explicação: O número 3 está na posição 1 da lista!\n")


# TESTE 2: Buscar o número -1 (que NÃO EXISTE)
print("TESTE 2: Buscando o número -1")
print("-" * 40)
print(f"Lista: {minha_lista}")
print(f"Procurando por: -1\n")

# Simulação mental:
# Iteração 1: baixo=0, alto=4, meio=2, chute=5 → 5 > -1? SIM → alto=1
# Iteração 2: baixo=0, alto=1, meio=0, chute=1 → 1 > -1? SIM → alto=-1
# Iteração 3: baixo=0, alto=-1 → baixo > alto? SIM → Sai do loop! Retorna None

resultado = busca_binaria(minha_lista, -1)
print(f"Resultado: {resultado}")
print("Explicação: O número -1 não existe na lista!\n")


# ============ BÔNUS: COMPARAÇÃO COM BUSCA LINEAR ============

print("\n=== POR QUE A BUSCA BINÁRIA É TÃO RÁPIDA? ===\n")

# Para uma lista de 1 MILHÃO de elementos:
tamanho = 1_000_000

print(f"Lista com {tamanho:,} elementos:")
print(f"- Busca LINEAR (um por um): até {tamanho:,} tentativas")
print(f"- Busca BINÁRIA (divide e conquista): apenas cerca de 20 tentativas!")
print(f"  (porque 2²⁰ ≈ 1.048.576, que é > {tamanho:,})")

print("\n✨ MAGIC: A cada tentativa, ELIMINAMOS METADE da lista restante!")


# ============ EXEMPLO VISUAL ============

print("\n=== VISUALIZANDO AS ELIMINAÇÕES ===\n")

lista_exemplo = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
print(f"Lista completa: {lista_exemplo}")
print(f"Procurando: 17\n")

print("Iteração 1: [1,3,5,7,9,11,13,15,17,19,21,23,25] (13 elementos)")
print("             ↑                       ↑")
print("           baixo=0                  alto=12")
print("             meio = (0+12)//2 = 6 → chute = 13")
print("             13 > 17? NÃO! → Descartamos metade ESQUERDA!\n")

print("Iteração 2: [17,19,21,23,25] (5 elementos)")
print("             ↑           ↑")
print("           baixo=7      alto=12")
print("             meio = (7+12)//2 = 9 → chute = 19")
print("             19 > 17? SIM! → Descartamos metade DIREITA!\n")

print("Iteração 3: [17] (1 elemento)")
print("             ↑")
print("           baixo=7, alto=7")
print("             meio = (7+7)//2 = 7 → chute = 17")
print("             ACERTOU! Retorna índice 7\n")

print("✅ Em apenas 3 tentativas encontramos o 17 entre 13 números!")