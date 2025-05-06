def mm1_queue_metrics(arrival_rate, service_rate):
    """
    Calculate key metrics for an M/M/1 queue.

    Parameters:
        arrival_rate (float): λ, the average arrival rate.
        service_rate (float): μ, the average service rate.

    Returns:
        dict: A dictionary containing the calculated metrics.
    """
    if service_rate <= arrival_rate:
        return {"Erro": "O sistema é instável (λ >= μ)."}

    # Traffic intensity
    rho = arrival_rate / service_rate

    # Average number of customers in the system
    L = rho / (1 - rho)

    # Average number of customers in the queue
    L_q = (rho ** 2) / (1 - rho)

    # Average time a customer spends in the system
    W = 1 / (service_rate - arrival_rate)

    # Average waiting time in the queue
    W_q = rho / (service_rate - arrival_rate)

    return {
        "Taxa de Ocupação (ρ)": rho,
        "Número Médio no Sistema (L)": L,
        "Número Médio na Fila (Lq)": L_q,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio na Fila (Wq)": W_q,
    }