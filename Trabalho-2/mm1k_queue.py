import math

# Modelo M/M/1/K
def mm1k_queue_metrics(arrival_rate, service_rate, max_capacity, waiting_cost, service_cost):
    """
    Calcular as métricas chave para uma fila M/M/1/K.

    Parâmetros:
        arrival_rate (float): λ, a taxa média de chegada.
        service_rate (float): μ, a taxa média de serviço.
        max_capacity (int): K, a capacidade máxima do sistema.

    Retorna:
        dict: Um dicionário contendo as métricas calculadas.
    """
    if service_rate <= 0 or arrival_rate <= 0:
        return {"Erro": "Taxas de chegada e serviço devem ser maiores que zero."}

    rho = arrival_rate / service_rate  # Intensidade de tráfego

    # Calcular P0 (constante de normalização)
    P0_inv = sum((rho**n) / math.factorial(n) for n in range(max_capacity + 1))
    P0 = 1 / P0_inv

    # Calcular Pn para todos os n
    Pn = [P0 * (rho**n) / math.factorial(n) for n in range(max_capacity + 1)]

    # Probabilidade de bloqueio (P_block = Pk)
    P_block = Pn[max_capacity]

    # Taxa efetiva de chegada
    lambda_eff = arrival_rate * (1 - P_block)

    # Número médio de clientes no sistema (L)
    L = sum(n * Pn[n] for n in range(max_capacity + 1))

    # Tempo médio no sistema (W)
    W = L / lambda_eff if lambda_eff > 0 else 0

    # Número médio de clientes na fila (Lq)
    L_q = L - (1 - P_block)

    # Tempo médio de espera na fila (Wq)
    W_q = W - (1 / service_rate)
    
    # Custo Total (CT) 
    CT = waiting_cost * L + service_cost * 1

    return {
        "\nTaxa de Ocupação (ρ)": rho,
        "Probabilidade de Bloqueio (P_block)": P_block,
        "Número Médio no Sistema (L)": L,
        "Número Médio na Fila (Lq)": L_q,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio na Fila (Wq)": W_q,
        "Custo Total (CT)": CT,
    }

'''
Modelo M/M/1/K

Exemplo 1)

lambda = 0,3 clientes por minuto
mi = 0,5 clientes por minuto
K = 2
s = 1

a) 
Po = (1-0,3*2)/((1-0,3*2)^2+1)
Po = 0,5102

b)
L = (0,3*2/(1-0,3*2)) - (((2+1)*0,3*2^3)/(1-0,3*2^3))
L = 0,6735 clientes

c)
Lq = 0,6735 - (1 - 0,5102)
Lq = 0,1837 clientes

d)
P2 = ((1-0,3*2)/(1-0,3*2^3)) * 0,3*2^2
P2 = 0,1837

e) 
lambda = 0,3 * (1 - 0,1837)
lambda = 0,2449 (tempo de espera na fila)

Wq = Lq/lambda
Wq = 0,1837/0,,2449
Wq = 0,75 minutos

f)
W = L/ lambda
W = 0,6735/0,2449
W = 2,75 minutos
'''