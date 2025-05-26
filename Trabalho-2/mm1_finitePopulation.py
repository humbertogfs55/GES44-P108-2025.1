# Modelo M/M/1/N (população finita)
def mm1_finite_population_metrics(arrival_rate, service_rate, population_size, waiting_cost, service_cost):
    if service_rate <= arrival_rate:
        return {"Erro": "O sistema é instável (λ >= μ)."}

    # Inicializa as probabilidades de estado
    probabilities = [1.0]  # P0 começa em 1.0 e será ajustado mais tarde
    normalization_constant = 1.0

    # Calcula as probabilidades de estado
    for n in range(1, population_size + 1):
        p_n = probabilities[n - 1] * \
            (arrival_rate * (population_size - (n - 1))) / service_rate
        probabilities.append(p_n)
        normalization_constant += p_n

    # Normaliza as probabilidades
    probabilities = [p / normalization_constant for p in probabilities]

    # Métricas de desempenho
    avg_customers_in_system = sum(
        n * probabilities[n] for n in range(population_size + 1))
    avg_customers_in_queue = avg_customers_in_system - (1 - probabilities[0])
    throughput = arrival_rate * (1 - probabilities[population_size])
    avg_time_in_system = avg_customers_in_system / throughput
    avg_waiting_time = avg_customers_in_queue / throughput
    
    # Custo Total (CT) 
    CT = waiting_cost * avg_customers_in_system + service_cost * 1 

    return {
        "\nProbabilidades Normalizadas": probabilities,
        "Número Médio no Sistema (L)": avg_customers_in_system,
        "Número Médio na Fila (Lq)": avg_customers_in_queue,
        "Taxa de Processamento (T)": throughput,
        "Tempo Médio no Sistema (W)": avg_time_in_system,
        "Tempo Médio na Fila (Wq)": avg_waiting_time,
        "Probabilidade de Inatividade (P_0)": probabilities[0],
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