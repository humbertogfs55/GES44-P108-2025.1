import math

# Modelo M/M/1/K
<<<<<<< HEAD
def mm1k_queue_metrics(arrival_rate, service_rate, max_capacity, waiting_cost, service_cost):
=======
def mm1k_queue_metrics(arrival_rate, service_rate, max_capacity):
>>>>>>> 72fd703979bb5b07f5bcbc56b66cd8150cf82705
    """
    Calcular as métricas chave para uma fila M/M/1/K.

    Parâmetros:
        arrival_rate (float): λ, a taxa média de chegada.
        service_rate (float): μ, a taxa média de serviço.
        max_capacity (int): K, a capacidade máxima do sistema.

    Retorna:
        dict: Um dicionário contendo as métricas calculadas.
    """
    if service_rate <= 0 or arrival_rate <= 0:
        return {"Erro": "Taxas de chegada e serviço devem ser maiores que zero."}

    rho = arrival_rate / service_rate  # Intensidade de tráfego

    # Calcular P0 (constante de normalização)
    P0_inv = sum((rho**n) / math.factorial(n) for n in range(max_capacity + 1))
    P0 = 1 / P0_inv

    # Calcular Pn para todos os n
    Pn = [P0 * (rho**n) / math.factorial(n) for n in range(max_capacity + 1)]

    # Probabilidade de bloqueio (P_block = Pk)
    P_block = Pn[max_capacity]

    # Taxa efetiva de chegada
    lambda_eff = arrival_rate * (1 - P_block)

    # Número médio de clientes no sistema (L)
    L = sum(n * Pn[n] for n in range(max_capacity + 1))

    # Tempo médio no sistema (W)
    W = L / lambda_eff if lambda_eff > 0 else 0

    # Número médio de clientes na fila (Lq)
    L_q = L - (1 - P_block)

    # Tempo médio de espera na fila (Wq)
    W_q = W - (1 / service_rate)
    
    # Custo Total (CT) 
    CT = waiting_cost * L + service_cost * 1

    return {
        "\nTaxa de Ocupação (ρ)": rho,
        "Probabilidade de Bloqueio (P_block)": P_block,
        "Número Médio no Sistema (L)": L,
        "Número Médio na Fila (Lq)": L_q,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio na Fila (Wq)": W_q,
        "Custo Total (CT)": CT,
    }
