import math

def mm1k_queue_metrics(arrival_rate, service_rate, max_capacity):
    """
    Calculate key metrics for an M/M/1/K queue.

    Parameters:
        arrival_rate (float): λ, the average arrival rate.
        service_rate (float): μ, the average service rate.
        max_capacity (int): K, the maximum capacity of the system.

    Returns:
        dict: A dictionary containing the calculated metrics.
    """
    if service_rate <= 0 or arrival_rate <= 0:
        return {"Erro": "Taxas de chegada e serviço devem ser maiores que zero."}

    rho = arrival_rate / service_rate  # Traffic intensity

    # Calculate P0 (normalization constant)
    P0_inv = sum((rho**n) / math.factorial(n) for n in range(max_capacity + 1))
    P0 = 1 / P0_inv

    # Calculate Pn for all n
    Pn = [P0 * (rho**n) / math.factorial(n) for n in range(max_capacity + 1)]

    # Blocking probability (P_block = Pk)
    P_block = Pn[max_capacity]

    # Effective arrival rate
    lambda_eff = arrival_rate * (1 - P_block)

    # Average number of customers in the system (L)
    L = sum(n * Pn[n] for n in range(max_capacity + 1))

    # Average time in the system (W)
    W = L / lambda_eff if lambda_eff > 0 else 0

    # Average number of customers in the queue (Lq)
    L_q = L - (1 - P_block)

    # Average waiting time in the queue (Wq)
    W_q = W - (1 / service_rate)

    return {
        "Taxa de Ocupação (ρ)": rho,
        "Probabilidade de Bloqueio (P_block)": P_block,
        "Número Médio no Sistema (L)": L,
        "Número Médio na Fila (Lq)": L_q,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio na Fila (Wq)": W_q,
    }
