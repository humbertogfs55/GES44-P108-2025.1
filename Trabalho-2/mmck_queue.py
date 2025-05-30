import math

# Modelo M/M/s>1/K
def mmc_k_queue_metrics(arrival_rate, service_rate, num_servers, max_capacity, waiting_cost, service_cost):
    """
    Calcula as métricas chave para uma fila M/M/s/K.

    Parâmetros:
        arrival_rate (float): λ, taxa média de chegada.
        service_rate (float): μ, taxa média de serviço.
        num_servers (int): s, número de servidores.
        max_capacity (int): K, capacidade máxima do sistema.
        waiting_cost (float): Custo de espera por cliente.
        service_cost (float): Custo de serviço por cliente.

    Retorna:
        dict: Métricas de desempenho do sistema.
    """

    if service_rate <= 0 or arrival_rate <= 0 or num_servers <= 0 or max_capacity <= 0:
        return {"Erro": "Todos os parâmetros devem ser maiores que zero."}

    # Intensidade de tráfego por servidor (ρ)
    rho = arrival_rate / (num_servers * service_rate)

    def factorial(n):
        return math.factorial(n)

    # Cálculo de P0 (probabilidade de sistema vazio)
    def P0_calc():
        sum1 = sum(((arrival_rate / service_rate) ** n) / factorial(n)
                   for n in range(num_servers))
        sum2 = ((arrival_rate / service_rate) ** num_servers / factorial(num_servers)) * ((1 - rho **
                                                                                           (max_capacity - num_servers + 1)) / (1 - rho)) if rho != 1 else (max_capacity - num_servers + 1)
        return 1 / (sum1 + sum2)

    P0 = P0_calc()

    # Probabilidades Pn
    Pn = []
    for n in range(0, max_capacity + 1):
        if n < num_servers:
            Pn_val = ((arrival_rate / service_rate) ** n / factorial(n)) * P0
        else:
            Pn_val = ((arrival_rate / service_rate) ** n /
                      (factorial(num_servers) * num_servers ** (n - num_servers))) * P0
        Pn.append(Pn_val)

    # Probabilidade de bloqueio (P_K)
    P_block = Pn[max_capacity]

    # Taxa efetiva de chegada
    arrival_rate_eff = arrival_rate * (1 - P_block)

    # Tempo médio de serviço
    service_time = 1 / service_rate

    # Lq: número médio na fila
    Lq_numerator = P0 * ((arrival_rate / service_rate) ** num_servers) * rho * (1 - rho ** (max_capacity -
                                                                                            num_servers) * (max_capacity - num_servers + 1 - (max_capacity - num_servers) * rho)) if rho != 1 else 0
    Lq_denominator = factorial(num_servers) * ((1 - rho) ** 2)
    Lq = Lq_numerator / Lq_denominator if rho != 1 else 0

    # L: número médio no sistema
    L = sum(n * Pn[n] for n in range(max_capacity + 1))

    # W: tempo médio no sistema
    W = L / arrival_rate_eff if arrival_rate_eff != 0 else 0

    # Wq: tempo médio na fila
    Wq = Lq / arrival_rate_eff if arrival_rate_eff != 0 else 0

    # Número médio de servidores ocupados
    busy_servers = sum(min(n, num_servers) * Pn[n]
                       for n in range(max_capacity + 1))

    # Custo Total (CT)
    CT = waiting_cost * L + service_cost * num_servers

    return {
        "\nTaxa de Ocupação (ρ)": rho,
        "Probabilidade de 0 clientes (P0)": P0,
        "Probabilidade de Bloqueio (P_K)": P_block,
        "Taxa Efetiva de Chegada (lambda_eff)": arrival_rate_eff,
        "Número Médio na Fila (Lq)": Lq,
        "Tempo Médio na Fila (Wq)": Wq,
        "Número Médio no Sistema (L)": L,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio de Serviço (1/mi)": service_time,
        "Número Médio de Servidores Ocupados": busy_servers,
        "Custo Total (CT)": CT,
        "Probabilidade de existir n clientes (Pn)": Pn,
    }


'''
Modelo M/M/s>1/K

Exemplo 1)

lambda = 5/h  
mi = 7/h
K = 5

Para s=1)
Po = 0,3295
W = 0,3369 horas
Wq = 0,194 horas
L = 1,5811 clientes
Lq = 0,9106 clientes
P5 = 0,06126 

Para s=2)
Po = 0,3751
W = 0,1611 horas
Wq = 0,01826 horas
L =  0,8011 clientes
Lq =  0,0908 clientes
P5 = 0,0055

------------------------------------
Exemplo 2 - Modelo M/M/s>1/K)

lambda = 1 carro/minuto
mi = 1/6 = 0.16666 carro/minuto
s = 3 boxes
K = 7 carros

rho = 2
P0 = 0.00088
L = 6.0631
Lq = 3,0920
W = 12,2442
Wq = 6,2439
P7 = 0,5048 = (60 * 0,5048) = 30,29 carro/hora
'''
