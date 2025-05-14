import math

# Modelo M/M/s>1
def mmc_queue_metrics(arrival_rate, service_rate, num_servers):
    """
    Calcular as métricas chave para uma fila M/M/c.

    Parâmetros:
        arrival_rate (float): λ, a taxa média de chegada.
        service_rate (float): μ, a taxa média de serviço.
        num_servers (int): c, o número de servidores.

    Retorna:
        dict: Um dicionário contendo as métricas calculadas.
    """
    if service_rate * num_servers <= arrival_rate:
        return {"Erro": "O sistema é instável (λ >= c * μ)."}

    # Intensidade de tráfego por servidor (ρ)
    # ρ = λ / (c * μ)
    rho = arrival_rate / (num_servers * service_rate)

    # Probabilidade de não haver clientes no sistema (P0)
    sum_terms = sum((arrival_rate / service_rate) ** n /
                    math.factorial(n) for n in range(num_servers))
    last_term = ((arrival_rate / service_rate) ** num_servers /
                 math.factorial(num_servers)) * (1 / (1 - rho))
    P0 = 1 / (sum_terms + last_term)

    # Probabilidade de formação de fila (P_queue)
    P_queue = (P0 * ((arrival_rate / service_rate) ** num_servers) /
               math.factorial(num_servers)) * (1 / (1 - rho))

    # Número médio na fila (Lq)
    L_q = P_queue * rho / (1 - rho)

    # Número médio no sistema (L)
    L = L_q + arrival_rate / service_rate

    # Tempo médio de espera na fila (Wq)
    W_q = L_q / arrival_rate

    # Tempo médio no sistema (W)
    W = W_q + 1 / service_rate

    return {
        "\nTaxa de Ocupação (ρ)": rho,
        "Probabilidade de Fila (P_queue)": P_queue,
        "Número Médio na Fila (Lq)": L_q,
        "Número Médio no Sistema (L)": L,
        "Tempo Médio na Fila (Wq)": W_q,
        "Tempo Médio no Sistema (W)": W,
    }
