import math

def mmcn_queue_metrics(arrival_rate, service_rate, num_servers, system_capacity):
    """
    Modelo M/M/s/N

    Parâmetros:
        arrival_rate (float): λ - taxa de chegada.
        service_rate (float): μ - taxa de serviço.
        num_servers (int): s - número de servidores.
        system_capacity (int): N - capacidade total do sistema (clientes no sistema, incluindo em serviço).

    Retorna:
        dict: Métricas da fila M/M/s/N
    """
    rho = arrival_rate / (num_servers * service_rate)

    # Cálculo de P0 (probabilidade do sistema vazio)
    sum1 = sum((arrival_rate / service_rate)**n / math.factorial(n) for n in range(num_servers))
    sum2 = ((arrival_rate / service_rate)**num_servers / math.factorial(num_servers)) * \
           sum((arrival_rate / (num_servers * service_rate))**k for k in range(system_capacity - num_servers + 1))
    P0 = 1 / (sum1 + sum2)

    # Probabilidade de bloqueio (sistema cheio)
    def Pn(n):
        if n < num_servers:
            return ((arrival_rate / service_rate) ** n) / math.factorial(n)
        else:
            return ((arrival_rate / service_rate) ** n) / (math.factorial(num_servers) * num_servers ** (n - num_servers))

    P_block = Pn(system_capacity) * P0

    # Taxa efetiva de chegada (clientes realmente atendidos)
    lambda_eff = arrival_rate * (1 - P_block)

    # Número médio de clientes no sistema (L)
    L = sum(n * Pn(n) * P0 for n in range(system_capacity + 1))

    # Tempo médio no sistema (W)
    W = L / lambda_eff if lambda_eff > 0 else 0

    # Número médio de clientes na fila (Lq)
    Ls = sum(n * Pn(n) * P0 for n in range(num_servers))  # clientes em serviço
    L_q = L - Ls

    # Tempo médio na fila
    W_q = L_q / lambda_eff if lambda_eff > 0 else 0

    return {
        "\nTaxa de Ocupação (ρ)": rho,
        "Probabilidade do Sistema Cheio (P_block)": P_block,
        "Número Médio no Sistema (L)": L,
        "Número Médio na Fila (Lq)": L_q,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio na Fila (Wq)": W_q,
    }

# Exemplo de uso:
resultados = mmcn_queue_metrics(arrival_rate=4, service_rate=2, num_servers=2, system_capacity=5)
for k, v in resultados.items():
    print(f"{k}: {v:.4f}")
