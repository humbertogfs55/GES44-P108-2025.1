import math

def priority_non_preemptive_metrics(arrival_rates, service_rate, t=1.0):
    """
    arrival_rates: lista com os λ de cada classe de prioridade [λ1, λ2, ..., λn]
    service_rate: taxa de serviço (μ)
    t: valor de tempo para calcular P(W > t) e P(Wq > t)

    Retorna um dicionário com as métricas por classe.
    """
    rho_total = sum(lam / service_rate for lam in arrival_rates)

    if rho_total >= 1:
        return {"Erro": "Sistema instável: a soma das taxas de chegada excede ou iguala a taxa de serviço."}

    P0 = 1 - rho_total  # Probabilidade do sistema estar vazio
    results = {}

    for i, lam_i in enumerate(arrival_rates):
        rho_i = sum(arrival_rates[j] / service_rate for j in range(i + 1))  # soma das prioridades >= classe i
        Wq = (1 / service_rate) * rho_i / ((1 - rho_total) ** 2)
        W = Wq + 1 / service_rate
        Lq = lam_i * Wq
        L = lam_i * W
        P_W_greater_t = math.exp(-service_rate * t) * math.exp(-lam_i * t)
        P_Wq_greater_t = math.exp(-service_rate * t * (1 - rho_total))

        results[f"Classe {i + 1}"] = {
            "Taxa de Chegada (λ)": lam_i,
            "Taxa de Ocupação (ρ)": rho_total,
            "Número Médio no Sistema (L)": round(L, 4),
            "Número Médio na Fila (Lq)": round(Lq, 4),
            "Tempo Médio no Sistema (W)": round(W, 4),
            "Tempo Médio na Fila (Wq)": round(Wq, 4),
            "Probabilidade de o Sistema Ocioso (P(n=0))": round(P0, 4),
            "Probabilidade de o Sistema Ocupado (P(n>0))": round(1 - P0, 4),
            "Probabilidade de W > t": round(P_W_greater_t, 4),
            "Probabilidade de Wq > t": round(P_Wq_greater_t, 4)
        }

    return results
