from decimal import Decimal, getcontext
from math import factorial

def mmc_priority_non_preemptive_metrics(arrival_rates, service_rate, servers):
    """
    arrival_rates: lista com λ de cada classe de prioridade [λ1, λ2, ..., λn]
    service_rate: taxa de serviço μ
    servers: número de servidores s
    
    Retorna dict com métricas por classe com base na fórmula correta de W_i.
    """
    getcontext().prec = 30 
    arrival_rates = [Decimal(str(lam)) for lam in arrival_rates]
    mu = Decimal(str(service_rate))
    s = int(servers)

    lambda_total = sum(arrival_rates)
    r = lambda_total / mu

    if lambda_total >= s * mu:
        return {"Erro": "Sistema instável: λ_total ≥ s * μ"}
    
    s_fact = Decimal(factorial(s))
    
    # Cálculo da soma de r^j / j! de j=0 até s-1
    sum_rj_by_jfact = sum([(r ** j) / Decimal(factorial(j)) for j in range(s)])
    r_pow_s = r ** s

    results = {}

    for i in range(len(arrival_rates)):
        lambda_i = arrival_rates[i]

        # Somatórios acumulados
        soma_ate_i_minus_1 = sum(arrival_rates[:i]) if i > 0 else Decimal(0)
        soma_ate_i = sum(arrival_rates[:i+1])

        termo1 = (s_fact * (s * mu - lambda_total) / r_pow_s) * sum_rj_by_jfact + s * mu
        termo2 = (Decimal(1) - soma_ate_i_minus_1 / (s * mu))
        termo3 = (Decimal(1) - soma_ate_i / (s * mu))

        try:
            Wq_i = Decimal(1) / (termo1 * termo2 * termo3)
        except ZeroDivisionError:
            return {"Erro": f"Divisão por zero na classe {i+1}. Verifique os parâmetros."}

        Wi = Wq_i + (Decimal(1) / mu)
        Lq_i = lambda_i * Wq_i
        L_i = lambda_i * Wi

        results[f"Classe {i+1}"] = {
            "Taxa de Chegada (λ)": float(lambda_i),
            "Tempo Médio no Sistema (W)": float(Wi),
            "Tempo Médio na Fila (Wq)": float(Wq_i),
            "Número Médio na Fila (Lq)": float(Lq_i),
            "Número Médio no Sistema (L)": float(L_i)
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

w1 = 0,36207
wq1 = 0,02874
lq1 = 0.0057 
l1 = 0,07241

w2 = 0,36649
wq2 = 0,03316
lq2 = 0,01989
l2 = 0,21989

w3 = 0,38141
wq3 = 0,04808
lq3 = 0,05769
l3 = 0,45769

--------------

Exemplo 3)

Quantas classes de prioridade existem?: 2
Digite a taxa de chegada (λ) da classe 1: 10
Digite a taxa de chegada (λ) da classe 2: 20
Digite a taxa de serviço (μ): 7.5
Digite o número de servidores (c): 5

w1 =  0.1535
wq1 = 0.0201
lq1 = 0.2015
l1 = 1.5348

w2 = 0.2341
wq2 = 0.1007
lq2 = 2.0150
l2 = 4.6816 
"""