def mm1_finite_population_metrics(arrival_rate, service_rate, population_size):
    if service_rate <= arrival_rate:
        return {"Erro": "O sistema é instável (λ >= μ)."}
    
    # Initialize state probabilities
    probabilities = [1.0]  # P0 starts at 1.0 and is adjusted later
    normalization_constant = 1.0

    # Calculate state probabilities
    for n in range(1, population_size + 1):
        p_n = probabilities[n - 1] * (arrival_rate * (population_size - (n - 1))) / service_rate
        probabilities.append(p_n)
        normalization_constant += p_n

    # Normalize probabilities
    probabilities = [p / normalization_constant for p in probabilities]

    # Performance metrics
    avg_customers_in_system = sum(n * probabilities[n] for n in range(population_size + 1))
    avg_customers_in_queue = avg_customers_in_system - (1 - probabilities[0])
    throughput = arrival_rate * (1 - probabilities[population_size])
    avg_time_in_system = avg_customers_in_system / throughput
    avg_waiting_time = avg_customers_in_queue / throughput

    return {
        "Probabilidades Normalizadas": probabilities,
        "Número Médio no Sistema (L)": avg_customers_in_system,
        "Número Médio na Fila (Lq)": avg_customers_in_queue,
        "Taxa de Processamento (T)": throughput,
        "Tempo Médio no Sistema (W)": avg_time_in_system,
        "Tempo Médio na Fila (Wq)": avg_waiting_time,
        "Probabilidade de Inatividade (P_0)": probabilities[0]
    }
