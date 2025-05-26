# Modelo M/M/1/N (população finita)
<<<<<<< HEAD
def mm1_finite_population_metrics(arrival_rate, service_rate, population_size, waiting_cost, service_cost):
=======
def mm1_finite_population_metrics(arrival_rate, service_rate, population_size):
>>>>>>> 72fd703979bb5b07f5bcbc56b66cd8150cf82705
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
