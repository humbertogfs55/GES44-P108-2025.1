import math

# Modelo M/M/s>1
def mmc_queue_metrics(arrival_rate, service_rate, num_servers):
    """
    Calcular as métricas chave para uma fila M/M/c.

    Parâmetros:
        arrival_rate (float): λ, a taxa média de chegada.
        service_rate (float): μ, a taxa média de serviço.
        num_servers (int): c, o número de servidores.

    Retorna:
        dict: Um dicionário contendo as métricas calculadas.
    """
    if service_rate * num_servers <= arrival_rate:
        return {"Erro": "O sistema é instável (λ >= c * μ)."}

    # Intensidade de tráfego por servidor (ρ)
    # ρ = λ / (c * μ)
    rho = arrival_rate / (num_servers * service_rate)

    # Probabilidade de não haver clientes no sistema (P0)
    sum_terms = sum((arrival_rate / service_rate) ** n /
                    math.factorial(n) for n in range(num_servers))
    last_term = ((arrival_rate / service_rate) ** num_servers /
                 math.factorial(num_servers)) * (1 / (1 - rho))
    P0 = 1 / (sum_terms + last_term)

    # Probabilidade de formação de fila (P_queue)
    P_queue = (P0 * ((arrival_rate / service_rate) ** num_servers) /
               math.factorial(num_servers)) * (1 / (1 - rho))

    # Número médio na fila (Lq)
    L_q = P_queue * rho / (1 - rho)

    # Número médio no sistema (L)
    L = L_q + arrival_rate / service_rate

    # Tempo médio de espera na fila (Wq)
    W_q = L_q / arrival_rate

    # Tempo médio no sistema (W)
    W = W_q + 1 / service_rate

    return {
        "\nTaxa de Ocupação (ρ)": rho,
        "Probabilidade de Fila (P_queue)": P_queue,
        "Número Médio na Fila (Lq)": L_q,
        "Número Médio no Sistema (L)": L,
        "Tempo Médio na Fila (Wq)": W_q,
        "Tempo Médio no Sistema (W)": W,
    }

'''
Modelo M/M/s>1

Exemplo 01)

Po =0,143
p = 30/2*20 = 0,75
lambda = 30 clientes por hora
mi = 20 clientes por hora
S = 2

a) 
Lq = (0,143*(1,5)^2 * 0,75)/(2!*(1-0,75)^2)
Lq = 1,9305 clientes

b)
Wq = 1,9305/30 
Wq = 0,064 horas 

c)
L = 1,9305 + (30/20)
L = 3,4305 clientes 

d)
W = 3,4305/30
W = 0,114 horas

e)
P(W > 0,2) = taca na formula la
P(W > 0,2) = 0,1689

f) 
P1 = (1,5^1/1!)*0,143 
P1 = 0,2145

P(Wq > 0,1) = [1 - 0,3575] * e^(-2*20*(1-0,75)*0,1)
P(Wq > 0,1) = 0,2364

g)
P3 = ((1,5)^3/(2!*(2^3-2))) * 0,143
P3 = 0,1206

----------------------------------------------------------------
Exemplo 02) 

lambda = 0,6 clientes por minuto
mi = 0,5 clientes por minuto
S = 3
Po = 0,294

a) 
P = 0,6/3*0,5
P = 0,4 

b) 
L = 0,094 + 1,2 
L = 1,29 clientes

c)
Lq = (0,294*(1,2^3)*0,4)/(3!*(1-0,4)^2)
Lq = 0,094 clientes

d) Po = 0,294 
'''