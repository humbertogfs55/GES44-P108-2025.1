from decimal import Decimal, getcontext
getcontext().prec = 10

def priority_preemptive_metrics(arrival_rates, service_rate):
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
        
        numerator = rho_total * rho_i
        denominator = (1 - sum_rho_before) * (1 - sum_rho_up_to_i)
        
        if denominator == 0:
            return {"Erro": f"Divisão por zero para classe {i+1}."}
        
        Lq_i = numerator / denominator
        Wq_i = Lq_i / arrival_rates[i]
        L_i = Lq_i + rho_i
        W_i = Wq_i + (Decimal('1') / service_rate)
        
        results[f"Classe {i+1}"] = {
            "Lq": float(Lq_i),
            "L": float(L_i),
            "W": float(W_i),
            "Wq": float(Wq_i)
        }
    return results
