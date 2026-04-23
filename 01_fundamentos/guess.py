

# Jogo de Adivinhação - O computador escolhe um número aleatório entre 0 e 100, e o jogador tem que adivinhar qual é.
# para fixar conteudo sobre algoritimos, estruturas de controle, loops, tratamento de exceções e interação com o usuário.

import random

# Gera número secreto entre 0 e 100
numero_secreto = random.randint(0, 100)

# Controla as tentativas do jogador
tentativas = 0
max_tentativas = 10

print("=== Jogo de Adivinhação ===")
print(f"Adivinhe o número entre 0 e 100!")
print(f"Você tem {max_tentativas} tentativas.\n")

# Loop principal do jogo
while tentativas < max_tentativas:
    tentativas_restantes = max_tentativas - tentativas
    
    try:
        # Tenta converter a entrada do usuário para número inteiro
        chute = int(input(f"[{tentativas_restantes} tentativas restantes] Seu chute: "))
    except ValueError:
        # Se o usuário não digitar um número, exibe erro e continua
        print("Digite apenas números inteiros!\n")
        continue
    
    # Valida se o número está dentro do intervalo permitido
    if chute < 0 or chute > 100:
        print("Digite um número entre 0 e 100!\n")
        continue
    
    # Conta esta tentativa
    tentativas += 1

    # Verifica se o chute está correto
    if chute == numero_secreto:
        print(f"\nParabéns! Você acertou em {tentativas} tentativa(s)!")
        break  # Sai do loop se acertar
    elif chute < numero_secreto:
        # Chute foi menor que o número secreto
        print("Muito baixo! Tente um número maior.\n")
    else:
        # Chute foi maior que o número secreto (única possibilidade restante)
        print("Muito alto! Tente um número menor.\n")
else:
    # Executa apenas se o loop terminou sem break (acabaram as tentativas)
    print(f"\nGame over! O número era {numero_secreto}.")

# mapa mental do código:
# Usuário digita algo
#          ↓
#     [TENTA converter]
#          ↓
#     Deu certo? ──NÃO──→ [Entra no except]
#          ↓                    ↓
#         SIM              Mostra erro
#          ↓                    ↓
#     Continua             [CONTINUE]
#          ↓                    ↓
#     Próximo código    Volta ao início do while