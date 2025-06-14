from decimal import Decimal, getcontext
def priority_preemptive_metrics(arrival_rates, service_rate):
    """
    arrival_rates: lista com λ de cada classe de prioridade [λ1, λ2, ..., λn]
    service_rate: taxa de serviço μ
    s: número de canais (servidores)

    Retorna dict com métricas por classe.
    """
    
    getcontext().prec = 10  

    service_rate = Decimal(service_rate)
    arrival_rates = [Decimal(lam) for lam in arrival_rates]

    rho_total = sum(lam / service_rate for lam in arrival_rates)
    if rho_total >= 1:
        return {"Erro": "Sistema instável: soma das taxas de chegada excede ou iguala capacidade do servidor."}

    results = {}
    for i, lam_i in enumerate(arrival_rates):
        sum_lam_i = sum(arrival_rates[j] for j in range(i + 1))
        sum_lam_i_minus_1 = sum(arrival_rates[j] for j in range(i)) if i > 0 else Decimal('0')
        
        
        denominator = (Decimal('1') - (sum_lam_i_minus_1 / (service_rate))) * \
                      (Decimal('1') - (sum_lam_i / (service_rate)))
        
        W = (Decimal('1') / service_rate) / denominator
        Wq = W - (Decimal('1') / service_rate)
        L = sum_lam_i * W
        Lq = L - (sum_lam_i / service_rate)

        results[f"Classe {i + 1}"] = {
            "Taxa de Chegada (λ)": round(lam_i,5),
            "Taxa de Ocupação (ρ)": round(rho_total,5),
            "Número Médio no Sistema (L)": round(L, 5),
            "Número Médio na Fila (Lq)": round(Lq, 5),
            "Tempo Médio no Sistema (W)": round(W, 5),
            "Tempo Médio na Fila (Wq)": round(Wq, 5)
        }

    return results

'''
Modelo M/M/1 com interrupção

Exemplo 1)

Quantas classes de prioridade existem?: 3
Digite a taxa de chegada (λ) da classe 1: 0.2
Digite a taxa de chegada (λ) da classe 2: 0.6
Digite a taxa de chegada (λ) da classe 3: 1.2
Digite a taxa de serviço (μ): 3
Digite o numero de canais: 1

tem que dar:

w1 = 0,3571
wq1 = 0,0238
l1 = 0,07142
lq1 = 0,004753 

w2 = 0,4870
wq2 = 0,1537
l2 = 0,3896
lq2 = 0,1229 

w3 = 1,3636
wq3 = 1,0303
l3 = 2,7272
lq3 = 2,0605 

'''