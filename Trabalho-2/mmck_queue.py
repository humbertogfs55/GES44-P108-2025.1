import math

# Modelo M/M/s>1/K
def mmc_k_queue_metrics(arrival_rate, service_rate, num_servers, max_capacity):
    """
    Calcula as métricas chave para uma fila M/M/s/K.

    Parâmetros:
        arrival_rate (float): λ, taxa média de chegada.
        service_rate (float): μ, taxa média de serviço.
        num_servers (int): s, número de servidores.
        max_capacity (int): K, capacidade máxima do sistema.

    Retorna:
        dict: Métricas de desempenho do sistema.
    """

    if service_rate <= 0 or arrival_rate <= 0 or num_servers <= 0 or max_capacity <= 0:
        return {"Erro": "Todos os parâmetros devem ser maiores que zero."}

    rho = arrival_rate / (num_servers * service_rate)  # Intensidade de tráfego

    # Cálculo de P0
    sum_1 = sum((arrival_rate / service_rate) ** n / math.factorial(n) for n in range(num_servers + 1))
    sum_2 = sum(
        ((arrival_rate / service_rate) ** num_servers) /
        (math.factorial(num_servers) * (num_servers ** (n - num_servers)))
        for n in range(num_servers + 1, max_capacity + 1)
    )
    P0 = 1 / (sum_1 + sum_2)

    # Probabilidades Pn
    Pn = []
    for n in range(max_capacity + 1):
        if n <= num_servers:
            p = ((arrival_rate / service_rate) ** n) / math.factorial(n) * P0
        else:
            p = ((arrival_rate / service_rate) ** num_servers) / (
                math.factorial(num_servers) * (num_servers ** (n - num_servers))
            ) * P0
        Pn.append(p)

    # Probabilidade de bloqueio (P_K)
    P_block = Pn[max_capacity]

    # Taxa efetiva de chegada
    arrival_rate_eff = arrival_rate * (1 - P_block)

    # Número médio de clientes na fila (Lq)
    Lq_numerator = ((arrival_rate / service_rate) ** num_servers) * rho * P0
    Lq_denominator = math.factorial(num_servers) * ((1 - rho) ** 2)
    part_bracket = (1 - rho ** (max_capacity - num_servers + 1)) - (max_capacity - num_servers) * rho ** (max_capacity - num_servers) * (1 - rho)
    Lq = Lq_numerator / Lq_denominator * part_bracket

    # Tempo médio de espera na fila
    Wq = Lq / arrival_rate_eff if arrival_rate_eff > 0 else 0

    # Número médio de clientes no sistema
    L = sum(n * Pn[n] for n in range(max_capacity + 1))

    # Tempo médio no sistema
    W = L / arrival_rate_eff if arrival_rate_eff > 0 else 0
    
    # Tempo médio de serviço
    service_time = 1 / service_rate

    # Número médio de servidores ocupados
    busy_servers = num_servers * (1 - sum(Pn[n] for n in range(num_servers)))

    return {
        "\nTaxa de Ocupação (ρ)": rho,
        "Probabilidade de 0 clientes (P0)": P0,
        "Probabilidade de Bloqueio (P_K)": P_block,
        "Taxa Efetiva de Chegada (lambda_eff)": arrival_rate_eff,
        "Número Médio na Fila (Lq)": Lq,
        "Tempo Médio na Fila (Wq)": Wq,
        "Número Médio no Sistema (L)": L,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio de Serviço (1/mi)": service_time,
        "Número Médio de Servidores Ocupados": busy_servers,
        "Distribuição de Probabilidades (Pn)": Pn
    }
