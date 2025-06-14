from decimal import Decimal, getcontext, ROUND_HALF_UP
from math import factorial

def mmc_priority_non_preemptive_metrics(arrival_rates, service_rate, servers):
    getcontext().prec = 30

    arrival_rates = [Decimal(str(lam)) for lam in arrival_rates]
    mu = Decimal(str(service_rate))
    servers = int(servers)

    lambda_total = sum(arrival_rates)
    rho = lambda_total / (mu * servers)

    if rho >= 1:
        return {"Erro": "Sistema instável: rho >= 1."}

    sum_terms = sum((lambda_total / mu) ** n / Decimal(factorial(n)) for n in range(servers))
    last_term = ((lambda_total / mu) ** servers) / (Decimal(factorial(servers)) * (1 - rho))
    P0 = Decimal(1) / (sum_terms + last_term)

    Lq = (P0 * ((lambda_total / mu) ** servers) * rho) / (Decimal(factorial(servers)) * ((1 - rho) ** 2))
    Wq_base = Lq / lambda_total

    rho_i = [lam / (mu * servers) for lam in arrival_rates]

    sigma = []
    for i in range(len(rho_i)):
        sigma.append(sum(rho_i[:i+1]))

    def arred(x):
        return x.quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)

    results = {}
    for i in range(len(arrival_rates)):
        lambda_i = arrival_rates[i]
        sigma_prev = Decimal('0') if i == 0 else sigma[i-1]

        Wq_i = Wq_base / (1 - sigma_prev)   
        W_i = Wq_i + (Decimal('1') / mu)
        Lq_i = lambda_i * Wq_i
        L_i = lambda_i * W_i

        results[f"Classe {i+1}"] = {
            "Taxa de Chegada (λ)": float(lambda_i),
            "Tempo Médio na Fila (Wq)": float(arred(Wq_i)),
            "Tempo Médio no Sistema (W)": float(arred(W_i)),
            "Número Médio na Fila (Lq)": float(arred(Lq_i)),
            "Número Médio no Sistema (L)": float(arred(L_i))
        }

    return results


"""
Modelo MMC sem interrupção:

# Exemplo 1)

Quantas classes de prioridade existem?: 3
Digite a taxa de chegada (λ) da classe 1: 0.2
Digite a taxa de chegada (λ) da classe 2: 0.6
Digite a taxa de chegada (λ) da classe 3: 1.2
Digite a taxa de serviço (μ): 3
Digite o número de servidores (c): 2

lq1 = 0,09574
l1 = 0,07241
w1 = 0,36207
wq1 = 0,02874

lq2 = 0,01989
l2 = 0,21989
w2 = 0,36649
wq2 = 0,03316

lq3 = 0,05769
l3 = 0,45769
w3 = 0,38141
wq3 = 0,04808
"""