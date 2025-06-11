def mm1_preemptive_priority_metrics(service_rates, arrival_rates):
    rhos = [l / service_rates for l in arrival_rates]
    total_lambda = sum(arrival_rates)
    
    L_list = []
    Lq_list = []
    
    for i in range(len(arrival_rates)):
        # sum of rhos for all classes with priority >= current class i
        sum_rho = sum(rhos[:i+1])
        if sum_rho >= 1:
            raise ValueError(f"Sistema instável para classe {i+1}: soma dos rho = {sum_rho:.3f} >= 1")
        
        W_i = 1 / (service_rates * (1 - sum_rho))
        Wq_i = W_i - (1 / service_rates)
        
        L_i = arrival_rates[i] * W_i
        Lq_i = arrival_rates[i] * Wq_i
        
        L_list.append(L_i)
        Lq_list.append(Lq_i)
    
    L = sum(L_list)
    Lq = sum(Lq_list)
    W = L / total_lambda
    Wq = Lq / total_lambda
    
    return {
        "L": L,
        "Lq": Lq,
        "W": W,
        "Wq": Wq,
        "per_class": [
            {
                "class": i+1,
                "L": L_list[i],
                "Lq": Lq_list[i],
                "W": L_list[i]/arrival_rates[i],
                "Wq": Lq_list[i]/arrival_rates[i]
            }
            for i in range(len(arrival_rates))
        ]
    }