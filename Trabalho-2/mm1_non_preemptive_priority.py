from decimal import Decimal, getcontext
def priority_non_preemptive_metrics(arrival_rates, service_rate):
    """
    arrival_rates: lista com λ de cada classe de prioridade [λ1, λ2, ..., λn]
    service_rate: taxa de serviço μ 
    
    Retorna dict com métricas por classe.
    """
    getcontext().prec = 15
    
    arrival_rates = [Decimal(str(lam)) for lam in arrival_rates]
    service_rate = Decimal(str(service_rate))
    
    lambda_total = sum(arrival_rates)
    rho_total = lambda_total / service_rate
    
    if rho_total >= 1:
        return {"Erro": "Sistema instável: soma das taxas de utilização >= 1."}
    
     # Calcula ρ_i para cada classe
    rho_i = [lam / service_rate for lam in arrival_rates]
    
    # Calcula σ_i (soma acumulada dos ρ até a classe i)
    sigma = []
    for i in range(len(rho_i)):
        sigma.append(sum(rho_i[:i+1]))
        
    results = {}
    for i in range(len(arrival_rates)):
        lambda_i = arrival_rates[i]
        
        # σ_{i-1} (soma até a classe anterior)
        sigma_prev = Decimal('0') if i == 0 else sigma[i-1]
        
        # σ_i (soma até a classe atual)
        sigma_current = sigma[i]
        
        # Wq_i = (ρ_total/μ) / [(1 - σ_{i-1}) * (1 - σ_i)]
        numerator = rho_total / service_rate
        denominator = (Decimal('1') - sigma_prev) * (Decimal('1') - sigma_current)
        Wq_i = numerator / denominator
        
        W_i = Wq_i + (Decimal('1') / service_rate)
        Lq_i = lambda_i * Wq_i
        L_i = lambda_i * W_i
        
        results[f"Classe {i+1}"] = {
            "Taxa de Chegada (λ)": float(lambda_i),
            "Tempo Médio na Fila (Wq)": float(Wq_i),
            "Tempo Médio no Sistema (W)": float(W_i),
            "Número Médio na Fila (Lq)": float(Lq_i),
            "Número Médio no Sistema (L)": float(L_i)
        }
    return results

'''
Modelo M/M/1 sem interrupção

Exemplo 1)

Quantas classes de prioridade existem?: 3
Digite a taxa de chegada (λ) da classe 1: 0.2
Digite a taxa de chegada (λ) da classe 2: 0.6
Digite a taxa de chegada (λ) da classe 3: 1.2
Digite a taxa de serviço (μ): 3

tem que dar:

w1 = 0,5714
wq1 = 0,23809
l1 = 0,11428
lq1 = 0,047619

w2 = 0,65800
wq2 = 0,32467
l2 = 0,39480
lq2 = 0,19480 

w3 = 1,24242
wq3 = 0,90909
l3 = 1,4909
lq3 = 1,0909 

'''