def priority_preemptive_metrics(arrival_rates, service_rate):
    """
    arrival_rates: lista com λ de cada classe de prioridade [λ1, λ2, ..., λn]
    service_rate: taxa de serviço μ

    Retorna dict com métricas por classe.
    """

    rho_total = sum(lam / service_rate for lam in arrival_rates)
    if rho_total >= 1:
        return {"Erro": "Sistema instável: soma das taxas de chegada excede ou iguala capacidade do servidor."}

    results = {}
    for i, lam_i in enumerate(arrival_rates):
        rho_i = sum(arrival_rates[j] / service_rate for j in range(i + 1))
        rho_i_minus_1 = sum(arrival_rates[j] / service_rate for j in range(i)) if i > 0 else 0

        Wq = rho_i_minus_1 / (service_rate * (1 - rho_i))
        W = Wq + 1 / service_rate
        Lq = lam_i * Wq
        L = lam_i * W

        P0 = 1 - rho_total
        P_occupied = 1 - P0
        # Para fila preemptiva, a probabilidade de W > t e Wq > t podem ser aproximadas
        import math
        t = 1  # valor padrão para cálculo de probabilidades
        P_W_greater_t = math.exp(-service_rate * (1 - rho_i) * t)
        P_Wq_greater_t = math.exp(-service_rate * (1 - rho_i) * t)  # mesma aproximação

        results[f"Classe {i + 1}"] = {
            "Taxa de Chegada (λ)": lam_i,
            "Taxa de Ocupação (ρ)": rho_total,
            "Número Médio no Sistema (L)": round(L, 4),
            "Número Médio na Fila (Lq)": round(Lq, 4),
            "Tempo Médio no Sistema (W)": round(W, 4),
            "Tempo Médio na Fila (Wq)": round(Wq, 4),
            "Probabilidade de o Sistema Ocioso (P(n=0))": round(P0, 4),
            "Probabilidade de o Sistema Ocupado (P(n>0))": round(P_occupied, 4),
            "Probabilidade de W > t": round(P_W_greater_t, 4),
            "Probabilidade de Wq > t": round(P_Wq_greater_t, 4),
        }

    return results
