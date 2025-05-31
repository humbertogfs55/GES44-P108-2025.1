def mm1n_queue_metrics(arrival_rate, service_rate, population_size, waiting_cost, service_cost):
    '''
    Modelo M/M/1 com população finita
    
    Parâmetros:
        arrival_rate (float): λ - taxa de chegada.
        service_rate (float): μ - taxa de serviço.
        population_size (int): N - tamanho da população (capacidade do sistema).
        waiting_cost (float): CE - custo de espera por cliente.
        service_cost (float): CA - custo de atendimento por cliente.
        
    Retorna:
        dict: Métricas da fila M/M/1/N
    '''
    
    if service_rate <= arrival_rate:
        return {"Erro": "O sistema é instável (λ >= μ)."}

    # Inicializa as probabilidades de estado
    probabilities = [1.0]  # P0 começa em 1.0 e será ajustado mais tarde
    normalization_constant = 1.0

    # Calcula as probabilidades de estado
    for n in range(1, population_size + 1):
        p_n = probabilities[n - 1] * (arrival_rate * (population_size - (n - 1))) / service_rate
        probabilities.append(p_n)
        normalization_constant += p_n

    # Normaliza as probabilidades
    probabilities = [p / normalization_constant for p in probabilities]

    # Número médio de clientes no sistema (L)
    L = sum(n * probabilities[n] for n in range(population_size + 1))
    
    # Número médio de clientes na fila (Lq)
    Lq = L - (1 - probabilities[0])
    
    # Taxa de processamento (T)
    lambda_eff = arrival_rate * (population_size - L)
    
    # Tempo médio no sistema (W) 
    W = L / lambda_eff
    
    # Tempo médio na fila (Wq)
    Wq = Lq / lambda_eff
    
    # Custo Total (CT) 
    CT = waiting_cost * L + service_cost * 1 

    return {
        "\nProbabilidades Normalizadas": probabilities,
        "Número Médio no Sistema (L)": L,
        "Número Médio na Fila (Lq)": Lq,
        "Taxa de Processamento (T)": lambda_eff,
        "Tempo Médio no Sistema (W)": W,
        "Tempo Médio na Fila (Wq)": Wq,
        "Probabilidade de Inatividade (P0)": probabilities[0],
        "Custo Total (CT)": CT
    }

'''
Modelo M/M/1 com população finita

Exemplo 1)

lambda = 0,01/h
mi = 0,125/h
N = 10

Po = 0,322

Lq = 10 - ((0,01 + 0,125)/0,01) * (1 - 0,322) = 0,8463 máquinas

Wq = 0,8463/(0,01 * (10 - 1,5244)) = 9,9856 horas

L = 10 - (0,125/0,01) * (1 - 0,322) = 1,5244 máquinas

W = 1,5244 / 0,01 * (10 - 1,5244) = 17,9896 horas

CT = CE * L + CA * S
CT = 100 * 1,5244 + 20 * 1
CT = 172,44

------------------------------------------------------------
Exemplo 2)

lambda = 0,0333/h
mi = 0,3333/h
N = 5

a) N - L = 4,360 robos

b) W = 4,400 horas

c) Po = 0,5640 

'''