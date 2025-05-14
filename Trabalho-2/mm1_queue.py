import math

# Modelo M/M/1
def mm1_queue_metrics(arrival_rate, service_rate, waiting_time):
    if service_rate <= arrival_rate:
        return {"Erro": "O sistema é instável (λ >= μ)."}

    # Intensidade de tráfego (ρ)
    # ρ = λ / μ
    rho = arrival_rate / service_rate

    # Número médio de clientes no sistema (L)
    # L = ρ / (1 - ρ)
    L = rho / (1 - rho)

    # Número médio de clientes na fila (Lq)
    # Lq = ρ^2 / (1 - ρ)
    L_q = (rho ** 2) / (1 - rho)

    # Tempo médio que um cliente passa no sistema (W)
    # W = 1 / (μ - λ)
    W = 1 / (service_rate - arrival_rate)

    # Tempo médio de espera na fila (Wq)
    # Wq = ρ / (μ - λ)
    W_q = rho / (service_rate - arrival_rate)

    # Probabilidade de que um cliente não precise esperar (P0)
    # P_0 = 1 - ρ
    P_0 = 1 - rho

    # Probabilidade do sistema estar ocioso (P(n=0)) = P_0
    P_0_final = P_0

    # Probabilidade do sistema estar ocupado (P(n > 0)) = 1 - P_0
    P_occupied = 1 - P_0_final

    # t >= 0
    if waiting_time >= 0:
        # Probabilidade de W > t (P(W > t))
        P_W_greater_t = math.exp(-service_rate * (1 - rho) * waiting_time)

        # Probabilidade de W_q > t (P(W_q > t))
        P_Wq_greater_t = rho * \
            math.exp(-service_rate * (1 - rho) * waiting_time)
    else:
        return {"Erro": "O tempo de espera (t) deve ser maior ou igual a zero"}

    results = {
        "\nProbabilidade de Não Esperar (P_0)": P_0,
        "Taxa de Ocupação (ρ)": rho,
        "Número Médio no Sistema (L)": L,
        "Número Médio na Fila (Lq)": L_q,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio na Fila (Wq)": W_q,
        "Probabilidade de o Sistema Ocioso (P(n=0))": P_0_final,
        "Probabilidade de o Sistema Ocupado (P(n>0))": P_occupied,
        "Probabilidade de W > t": P_W_greater_t,
        "Probabilidade de Wq > t": P_Wq_greater_t,
    }

    return results
