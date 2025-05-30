import math

# Modelo M/M/1
def mm1_queue_metrics(arrival_rate, service_rate, waiting_time_w, waiting_time_wq):
    if service_rate <= arrival_rate:
        return {"Erro": "O sistema é instável (λ >= μ)."}

    # Intensidade de tráfego (ρ)
    # ρ = λ / μ
    rho = arrival_rate / service_rate

    # Número médio de clientes no sistema (L)
    # L = ρ / (1 - ρ)
    L = rho / (1 - rho)

    # Número médio de clientes na fila (Lq)
    # Lq = ρ^2 / (1 - ρ)
    L_q = (rho ** 2) / (1 - rho)

    # Tempo médio que um cliente passa no sistema (W)
    # W = 1 / (μ - λ)
    W = 1 / (service_rate - arrival_rate)

    # Tempo médio de espera na fila (Wq)
    # Wq = ρ / (μ - λ)
    W_q = rho / (service_rate - arrival_rate)

    # Probabilidade de que um cliente não precise esperar (P0)
    # P_0 = 1 - ρ
    P_0 = 1 - rho

    # Probabilidade do sistema estar ocioso (P(n=0)) = P_0
    P_0_final = P_0

    # Probabilidade do sistema estar ocupado (P(n > 0)) = 1 - P_0
    P_occupied = 1 - P_0_final

    # t >= 0
    if waiting_time_w < 0 or waiting_time_wq < 0:
        return {"Erro": "Os tempos de espera devem ser maiores ou iguais a zero."}
    
    
    # Probabilidade de W > t (P(W > t))
    P_W_greater_t = math.exp(-service_rate * (1 - rho) * waiting_time_w)

    # Probabilidade de W_q > t (P(W_q > t))
    P_Wq_greater_t = rho * math.exp(-service_rate * (1 - rho) * waiting_time_wq)


    results = {
        "\nProbabilidade de Não Esperar (P_0)": P_0,
        "Taxa de Ocupação (ρ)": rho,
        "Número Médio no Sistema (L)": L,
        "Número Médio na Fila (Lq)": L_q,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio na Fila (Wq)": W_q,
        "Probabilidade de o Sistema Ocioso (P(n=0))": P_0_final,
        "Probabilidade de o Sistema Ocupado (P(n>0))": P_occupied,
        "Probabilidade de W > t": P_W_greater_t,
        "Probabilidade de Wq > t": P_Wq_greater_t,
    }

    return results

'''
Modelo M/M/1

# Exemplo 1)

lambda = 330/30 = 11 motores/mês

Taxa de ocupação (p = 0,88) = lambda/mi 
mi = lambda/0,88 --> mi=12,5 motores/mês

a) Distribuição de frequência relativa p/ o nº de equipamentos danificados:

b) Tempo médio do motor fora de serviço (dias):
W = 1/(mi - lambda)
W = 1/(12,5 - 11) 
W = 0,667 (20 dias)

c) Nº médio de motores aguardando reparo:
lq = (lambda^2)/(mi(mi - lambda))
lq = (11^2)/(12,5(12,5 - 11))
lq = 6,45 motores

d) Tempo médio que o motor aguarda a manutenção:
wq = (lambda)/(mi(mi - lambda))
wq = (11)/(12,5/(12,5 - 11))
wq = 0,5666 (17,6 dias)

e) Nº médio de motores fora de serviço (dias):
L = (lambda)/(mi - lambda)
L = 11/(12,5 - 11) 
L = 7,33 motores

f) Probabilidade do sistema ocioso:
P(n=0) = 1-p = 1 - 0,88 = 0,12

g) Probabilidade do sistema ocupado:
p = 0,88

h) Probabilidade W>1:
P(W > 1) = e^(-u(1-p))^t 
P(W > 1) = e^(-12,5(1-0,88))^1 
P(W > 1) = 0,2231

i) Probabilidade Wq>1:
P(Wq > 1) = p * e^(-u(1-p))^t 
P(Wq > 1) = 0,88 * e^(-12,5(1-0,88))^1 
P(Wq > 1) = 0,1964

---------------------------------------------------------------------------
Exemplo 02)

lambda = 60/20 = 3 clientes
mi = 60/15 = 4 clientes
taxa de ocupação = 3/4 = 0,75

a) P(n=0) = 1 - 0,75 = 0,25

b) 
L = (lambda)/(mi - lambda)
L = 3/4-3 = L=3 clientes

Lq = (lambda^2)/(mi(mi - lambda))
Lq = (3^2)/(4(4-3))
Lq = 9/4 = 2,25 clientes

c) 
W = 1/(mi - lambda)
W = 1/(4-3)
W = 1 hora

d) 
Wq = (lambda)/(mi(mi - lambda))
Wq = 3/4(4-3)
Wq = 3/4 = 0,75 horas * 60 = 45 minutos

e) 
P(Wq > 1) = p * e^(-u(1-p))^t 
P(Wq > 1) = 0,75 * e^(-4(1-0,75))^1
P(Wq > 1) =  0,2759

f)
P(W > 1) = e^(-u(1-p))^t 
P(W > 1) = e^(-4(1-0,75))^1
P(W > 1) = 0,3679

g) 
W = 1/(mi - lambda)
1,25 = 1/(4 - lambda)
lambda = 3,2 clientes por hora
'''