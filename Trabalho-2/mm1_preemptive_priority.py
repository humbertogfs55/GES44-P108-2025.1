from decimal import Decimal
def priority_preemptive_metrics(arrival_rates, service_rate, s):
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
        sum_lam_i = sum(arrival_rates[j] for j in range(i + 1))
        sum_lam_i_minus_1 = sum(arrival_rates[j] for j in range(i)) if i > 0 else Decimal('0')
        
        denominator = (Decimal('1') - (sum_lam_i_minus_1/ service_rate * s) * (Decimal('1') - (sum_lam_i/ service_rate * s)))
        W = (Decimal('1') / service_rate) / denominator
        L = lam_i * W
        Lq = L - lam_i / service_rate
        Wq = W - Decimal('1') / service_rate

        results[f"Classe {i + 1}"] = {
            "Taxa de Chegada (λ)": round(lam_i,5),
            "Taxa de Ocupação (ρ)": round(rho_total,5),
            "Número Médio no Sistema (L)": round(L, 5),
            "Número Médio na Fila (Lq)": round(Lq, 5),
            "Tempo Médio no Sistema (W)": round(W, 5),
            "Tempo Médio na Fila (Wq)": round(Wq, 5)
        }

    return results
