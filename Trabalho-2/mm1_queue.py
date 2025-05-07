import math


def mm1_queue_metrics(arrival_rate, service_rate, waiting_time):
    if service_rate <= arrival_rate:
        return {"Erro": "O sistema é instável (λ >= μ)."}
  
    # Traffic intensity (ρ)
    # ρ = λ / μ
    rho = arrival_rate / service_rate

    # Average number of customers in the system (L)
    # L = ρ / (1 - ρ)
    L = rho / (1 - rho)

    # Average number of customers in the queue (Lq)
    # Lq = ρ^2 / (1 - ρ) 
    L_q = (rho ** 2) / (1 - rho)

    # Average time a customer spends in the system (W)
    # W = 1 / (μ - λ)
    W = 1 / (service_rate - arrival_rate)

    # Average waiting time in the queue (Wq)
    # Wq = ρ / (μ - λ)
    W_q = rho / (service_rate - arrival_rate)

    # Probability that a customer does not have to wait (P0)
    # P_0 = 1 - ρ
    P_0 = 1 - rho
    
    # Probabilidade do sistema ocioso (P(n=0)) = P_0
    P_0_final = P_0

    # Probabilidade do sistema ocupado (P(n > 0)) = 1 - P_0
    P_occupied = 1 - P_0_final


    # t >= 0
    if waiting_time >= 0:
        # Probabilidade de W > t (P(W > t))
        P_W_greater_t = math.exp(-service_rate * (1 - rho) * waiting_time)
        
        # Probabilidade de W_q > t (P(W_q > t))
        P_Wq_greater_t = rho * math.exp(-service_rate * (1 - rho) * waiting_time) 
    else:
        return {"Erro": "O tempo de espera (t) deve ser maior ou igual a zero"}
    
   
    results = {
        "Probabilidade de Não Esperar (P_0)": P_0,
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