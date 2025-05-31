def mg1_queue_metrics(arrival_rate, service_rate, sigma_squared):
    """
    Calcula as métricas para o modelo de fila M/G/1.

    Parâmetros:
    - arrival_rate (λ): Taxa média de chegada
    - service_rate (μ): Taxa média de serviço
    - sigma_squared (σ²): Variância do tempo de serviço
    """

    # Taxa de utilização (ρ)
    rho = arrival_rate / service_rate

    # Verificação de estabilidade
    if rho >= 1:
        raise ValueError("O sistema é instável (ρ ≥ 1).")

    # Probabilidade de 0 clientes no sistema (P0)
    P0 = 1 - rho

    # Número médio de clientes na fila (Lq)
    Lq = (arrival_rate**2 * sigma_squared + rho**2) / (2 * (1 - rho))

    # Tempo médio de espera na fila (Wq)
    Wq = Lq / arrival_rate

    # Tempo médio total no sistema (W)
    W = Wq + 1 / service_rate

    # Número médio total de clientes no sistema (L)
    L = rho + Lq

    return {
        "\nProbabilidade de Não Esperar (P0)": P0,
        "Taxa de Ocupação (ρ)": rho,
        "Número Médio no Sistema (L)": L,
        "Número Médio na Fila (Lq)": Lq,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio na Fila (Wq)": Wq,
    }


'''
Modelo M/G/1:

Exemplo 1)

lambda = 4 carros/hora
mu = 60/10 = 6 carros/hora
variancia = (1/mu^2) = 1/6^2 = 1/36 = 0,02778

rho = lambda / mu = 4 / 6 = 0,6667
P0 = 1 - rho = 1 - 0,6667 = 0,3333
Lq = 1,333 carros
L = 0,667 carros
Wq = 0,333 horas
W = 0,167 horas

-----------------------------------
Exemplo 2)

lambda = 25 clientes/hora
tempo de servico = 90 segundos = 1,5 minutos = 0,025 horas
mu = 1/0,025 = 40 clientes/hora

rho = lambda/mu = 25/40 = 0,625 
P0 = 1 - rho = 1 - 0,625 = 0,375
L = 1,667 clientes
Lq = 1,042 clientes
W = 0,067 horas
Wq = 0,042 horas


Para tempo fixo de serviço:

lambda = 25 clientes/hora
tempo de servico = 90 segundos = 1,5 minutos = 0,025 horas
mu = 1/0,025 = 40 clientes/hora
variancia = 0 

rho = lambda/mu = 25/40 = 0,625 
P0 = 1 - rho = 1 - 0,625 = 0,375
L = 1,146 clientes
Lq = 0,521 clientes
W = 0,046 horas = 2,77 minutos
Wq = 0,021 horas = 1,25 minutos
'''
