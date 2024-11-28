# Função recursiva para resolver o problema das Torres de Hanói.
# Recebe o número de discos (n) e os índices das torres origem, auxiliar e destino (0, 1, 2 por padrão).
def hanoi(n, origem=0, auxiliar=1, destino=2):
    # Verifica se ainda existem discos a serem movidos.
    if n > 0:
        # Move n - 1 discos da torre de origem para a torre auxiliar, usando a torre de destino como auxílio.
        hanoi(n - 1, origem, destino, auxiliar)
        # Registra o movimento do disco da torre de origem para a torre de destino.
        movimentos.append((origem, destino))
        # Move os n - 1 discos da torre auxiliar para a torre de destino, usando a torre de origem como auxílio.
        hanoi(n - 1, auxiliar, origem, destino)

# Função para resolver o problema das Torres de Hanói e listar os passos.
# Recebe a quantidade de discos e uma lista com os nomes dos pinos/torres.
def resolver_hanoi(quantidade_discos, nomes_pinos):
    global discos, movimentos
    # Inicializa a configuração inicial das torres com os discos empilhados na torre de origem.
    discos = [list(range(int(quantidade_discos), 0, -1)), [], []]
    movimentos = []
    # Chama a função hanoi para encontrar os movimentos necessários.
    hanoi(int(quantidade_discos))
    # Chama a função listar_passos para exibir os movimentos com os nomes das torres.
    listar_passos(nomes_pinos)

# Função para listar os passos dos movimentos com os nomes das torres.
# Recebe a lista de nomes dos pinos/torres.
def listar_passos(nomes_pinos):
    for i, (origem, destino) in enumerate(movimentos, start=1):
        print(f'Passo {i}: Mova o disco da torre {nomes_pinos[origem]} para a torre {nomes_pinos[destino]}')

# Solicita ao usuário a quantidade de discos e os nomes das torres.
quantidade_discos = int(input("Digite a quantidade de discos: "))
nome_pino_origem = input("Digite o nome do pino de origem: ")
nome_pino_auxiliar = input("Digite o nome do pino auxiliar: ")
nome_pino_destino = input("Digite o nome do pino de destino: ")

# Cria uma lista com os nomes das torres 
nomes_pinos = [nome_pino_origem, nome_pino_auxiliar, nome_pino_destino]

# Chama a função resolver_hanoi para encontrar os movimentos e exibi-los.
resolver_hanoi(quantidade_discos, nomes_pinos)
