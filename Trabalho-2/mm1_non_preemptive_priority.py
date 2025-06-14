from decimal import Decimal, getcontext

getcontext().prec = 10

def priority_non_preemptive_metrics(arrival_rates, service_rate):
    arrival_rates = [Decimal(str(lam)) for lam in arrival_rates]
    service_rate = Decimal(str(service_rate))
    
    rho_list = [lam / service_rate for lam in arrival_rates]
    rho_total = sum(rho_list)
    
    if rho_total >= 1:
        return {"Erro": "Sistema instável: soma das taxas de utilização >= 1."}
    
    results = {}
    for i, rho_i in enumerate(rho_list):
        sum_rho_before = sum(rho_list[:i])
        sum_rho_up_to_i = sum(rho_list[:i+1])
        
        denominator = (1 - sum_rho_before) * (1 - sum_rho_up_to_i)
        if denominator == 0:
            return {"Erro": f"Divisão por zero para classe {i+1}."}
        
        Wq_i = (rho_total / service_rate) / denominator  # Tempo médio na fila
        Lq_i = arrival_rates[i] * Wq_i
        W_i = Wq_i + (Decimal('1') / service_rate)
        L_i = arrival_rates[i] * W_i
        
        results[f"Classe {i+1}"] = {
            "Taxa de Chegada (λ)": float(arrival_rates[i]),
            "Tempo Médio na Fila (Wq)": float(Wq_i),
            "Tempo Médio no Sistema (W)": float(W_i),
            "Número Médio na Fila (Lq)": float(Lq_i),
            "Número Médio no Sistema (L)": float(L_i)
        }
    return results
