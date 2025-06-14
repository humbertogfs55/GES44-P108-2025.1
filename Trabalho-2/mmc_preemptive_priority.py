from decimal import Decimal, getcontext
from math import factorial

def mmc_priority_preemptive_metrics(arrival_rates, service_rate, s):
    """
    arrival_rates: lista com λ de cada classe de prioridade [λ1, λ2, ..., λn]
    service_rate: taxa de serviço μ
    s: número de servidores

    Retorna dict com métricas por classe.
    """
    getcontext().prec = 10

    service_rate = Decimal(service_rate)
    arrival_rates = [Decimal(lam) for lam in arrival_rates]
    s = int(s)

    lambda_total = sum(arrival_rates)
    rho_total = lambda_total / (service_rate * s)
    
    if rho_total >= 1:
        return {"Erro": "Sistema instável: soma das taxas de chegada excede ou iguala capacidade do servidor."}

    def erlang_c(lambd, mu, s):
        """Probabilidade de espera usando fórmula de Erlang C"""
        a = lambd / mu
        sum_terms = sum((a**k / Decimal(factorial(k))) for k in range(s))
        last_term = (a**s / Decimal(factorial(s))) * (s * mu) / (s * mu - lambd)
        return last_term / (sum_terms + last_term)

    results = {}
    for i, lam_i in enumerate(arrival_rates):
        sum_lam_i = sum(arrival_rates[j] for j in range(i + 1))
        sum_lam_i_minus_1 = sum(arrival_rates[j] for j in range(i)) if i > 0 else Decimal('0')

        rho = lam_i / (service_rate * s)
        rho_eff = sum_lam_i / (service_rate * s)

        Pw = erlang_c(sum_lam_i, service_rate, s)

        priority_penalty = Decimal(i + 1)

        Wq = (Pw / (s * service_rate - sum_lam_i)) * priority_penalty
        W = Wq + Decimal('1') / service_rate

        Lq = lam_i * Wq
        L = lam_i * W

        results[f"Classe {i + 1}"] = {
            "Taxa de Chegada (λ)": round(lam_i, 5),
            "Taxa de Ocupação da Classe (ρ)": round(rho, 5),
            "Taxa de Ocupação Efetiva (ρ_eff)": round(rho_eff, 5),
            "Carga de Classes Superiores (λ_superiores)": round(sum_lam_i_minus_1, 5),
            "Número Médio no Sistema (L)": round(L, 5),
            "Número Médio na Fila (Lq)": round(Lq, 5),
            "Tempo Médio no Sistema (W)": round(W, 5),
            "Tempo Médio na Fila (Wq)": round(Wq, 5)
        }

    return results

"""
Modelo MMC com interrupção:

# Exemplo 1)

Quantas classes de prioridade existem?: 3
Digite a taxa de chegada (λ) da classe 1: 0.2
Digite a taxa de chegada (λ) da classe 2: 0.6
Digite a taxa de chegada (λ) da classe 3: 1.2
Digite a taxa de serviço (μ): 3
Digite o número de servidores (c): 2

p0 = 0,9355
lq1 = 0,000074156
l1 = 0,06674
w1 = 0,33370
wq1 = 0,000367

lq2 = 0,00634
l2 = 0,27300
w2 = 0,34126
wq2 = 0,00793

lq3 = 0,13084
l3 = 0,79751
w3 = 0,39875
wq3 = 0,06542
"""