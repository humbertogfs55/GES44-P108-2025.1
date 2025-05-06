def mm1_queue_metrics(arrival_rate, service_rate):
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

    # Probability that a customer does not have to wait
    P_0 = 1 - rho

    return {
        "Probabilidade de Não Esperar (P_0)": P_0,
        "Taxa de Ocupação (ρ)": rho,
        "Número Médio no Sistema (L)": L,
        "Número Médio na Fila (Lq)": L_q,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio na Fila (Wq)": W_q
    }
