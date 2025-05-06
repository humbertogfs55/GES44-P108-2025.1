import math

def mmc_queue_metrics(arrival_rate, service_rate, num_servers):
    """
    Calculate key metrics for an M/M/c queue.

    Parameters:
        arrival_rate (float): λ, the average arrival rate.
        service_rate (float): μ, the average service rate.
        num_servers (int): c, the number of servers.

    Returns:
        dict: A dictionary containing the calculated metrics.
    """
    if service_rate * num_servers <= arrival_rate:
        return {"Erro": "O sistema é instável (λ >= c * μ)."}

    # Traffic intensity per server
    rho = arrival_rate / (num_servers * service_rate)

    # Probability of no customers in the system (P0)
    sum_terms = sum((arrival_rate / service_rate) ** n / math.factorial(n) for n in range(num_servers))
    last_term = ((arrival_rate / service_rate) ** num_servers / math.factorial(num_servers)) * (1 / (1 - rho))
    P0 = 1 / (sum_terms + last_term)

    # Probability of queue formation (P_queue)
    P_queue = (P0 * ((arrival_rate / service_rate) ** num_servers) / math.factorial(num_servers)) * (1 / (1 - rho))

    # Average number in queue (Lq)
    L_q = P_queue * rho / (1 - rho)

    # Average number in the system (L)
    L = L_q + arrival_rate / service_rate

    # Average waiting time in the queue (Wq)
    W_q = L_q / arrival_rate

    # Average time in the system (W)
    W = W_q + 1 / service_rate

    return {
        "Taxa de Ocupação (ρ)": rho,
        "Probabilidade de Fila (P_queue)": P_queue,
        "Número Médio na Fila (Lq)": L_q,
        "Número Médio no Sistema (L)": L,
        "Tempo Médio na Fila (Wq)": W_q,
        "Tempo Médio no Sistema (W)": W,
    }
