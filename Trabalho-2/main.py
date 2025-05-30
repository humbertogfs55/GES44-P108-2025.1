from mm1_queue import mm1_queue_metrics
from mmc_queue import mmc_queue_metrics
from mm1k_queue import mm1k_queue_metrics
from mmck_queue import mmc_k_queue_metrics
from mm1n_queue import mm1n_queue_metrics
from mmcn_queue import mmcn_queue_metrics
from mg1_queue import mg1_queue_metrics


def parse_float(value):
    return float(value.replace(',', '.'))


def display_menu():
    print("\n--- Teoria das Filas ---")
    print("1. Modelo M/M/1")
    print("2. Modelo M/M/c")
    print("3. Modelo M/M/1/K")
    print("4. Modelo M/M/c/K")
    print("5. Modelo M/M/1/N (População finita)")
    print("6. Modelo M/M/c/N (população finita)")
    print("7. Modelo M/G/1")
    print("8. Sair")
    print("------------------------")


def handle_mm1():
    print("\n--- Modelo M/M/1 ---")
    
    arrival_rate = parse_float(input("Digite a taxa de chegada (λ): "))
    service_rate = parse_float(input("Digite a taxa de serviço (μ): "))
    waiting_time_w = parse_float(input("Digite o tempo t1 para cálculo de P(W > t): "))
    waiting_time_wq = parse_float(input("Digite o tempo t2 para cálculo de P(Wq > t): "))
    
    metrics = mm1_queue_metrics(arrival_rate, service_rate, waiting_time_w, waiting_time_wq)
    
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")


def handle_mmc():
    print("\n--- Modelo M/M/c ---")
    
    arrival_rate = parse_float(input("Digite a taxa de chegada (λ): "))
    service_rate = parse_float(input("Digite a taxa de serviço (μ): "))
    num_servers = int(input("Digite o número de servidores (c): "))
    waiting_time_w = parse_float(input("Digite o tempo t1 para cálculo de P(W > t): "))
    waiting_time_wq = parse_float(input("Digite o tempo t2 para cálculo de P(Wq > t): "))
    num_clients = int(input("Digite o número de clientes no sistema (N): "))
    
    metrics = mmc_queue_metrics(arrival_rate, service_rate, num_servers, waiting_time_w, waiting_time_wq, num_clients)
    
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")
            
            
def handle_mm1k():
    print("\n--- Modelo M/M/1/K ---")
    
    arrival_rate = parse_float(input("Digite a taxa de chegada (λ): "))
    service_rate = parse_float(input("Digite a taxa de serviço (μ): "))
    max_capacity = int(input("Digite a capacidade máxima do sistema (K): "))
    waiting_cost = parse_float(input("Digite o custo de espera (CE): "))
    service_cost = parse_float(input("Digite o custo de atendimento (CA): "))
    num_clients = int(input("Digite o número de clientes no sistema (N): "))
    
    metrics = mm1k_queue_metrics(arrival_rate, service_rate, max_capacity, waiting_cost, service_cost, num_clients)
    
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            if isinstance(value, list):
                print(f"{metric}: {', '.join(f'{v:.4f}' for v in value)}")
            else:
                print(f"{metric}: {value:.4f}")


def handle_mmck():
    print("\n--- Modelo M/M/c/K ---")
    
    arrival_rate = parse_float(input("Digite a taxa de chegada (λ): "))
    service_rate = parse_float(input("Digite a taxa de serviço (μ): "))
    num_servers = int(input("Digite o número de servidores (c): "))
    max_capacity = int(input("Digite a capacidade máxima do sistema (K): "))
    waiting_cost = parse_float(input("Digite o custo de espera (CE): "))
    service_cost = parse_float(input("Digite o custo de atendimento (CA): "))
    
    metrics = mmc_k_queue_metrics(arrival_rate, service_rate, num_servers, max_capacity, waiting_cost, service_cost)
    
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            if isinstance(value, list):
                print(f"{metric}: {', '.join(f'{v:.4f}' for v in value)}")
            else:
                print(f"{metric}: {value:.4f}")


def handle_mm1n():
    print("\n--- Modelo M/M/1/N (população finita) ---")
    
    arrival_rate = parse_float(input("Digite a taxa de chegada (λ): "))
    service_rate = parse_float(input("Digite a taxa de serviço (μ): "))
    population_size = int(input("Digite o tamanho da população (N): "))
    waiting_cost = parse_float(input("Digite o custo de espera (CE): "))
    service_cost = parse_float(input("Digite o custo de atendimento (CA): "))
    
    metrics = mm1n_queue_metrics(arrival_rate, service_rate, population_size, waiting_cost, service_cost)
    
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            if isinstance(value, list):
                print(f"{metric}: {', '.join(f'{v:.4f}' for v in value)}")
            else:
                print(f"{metric}: {value:.4f}")
                
                
def handle_mmcn():
    print("\n--- Modelo M/M/s/N (população finita) ---")
    
    arrival_rate = parse_float(input("Digite a taxa de chegada (λ): "))
    service_rate = parse_float(input("Digite a taxa de serviço (μ): "))
    num_servers = int(input("Digite o número de servidores (s): "))
    system_capacity = int(input("Digite a capacidade máxima do sistema (N): "))
    
    metrics = mmcn_queue_metrics(arrival_rate, service_rate, num_servers, system_capacity)
    
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")


def handle_mg1():
    print("\n--- Modelo M/G/1 ---")
    
    arrival_rate = parse_float(input("Digite a taxa de chegada (λ): "))
    service_rate = parse_float(input("Digite a taxa de serviço (μ): "))
    sigma_squared = parse_float(input("Digite a variância do tempo de serviço (σ²): "))
    
    metrics = mg1_queue_metrics(arrival_rate, service_rate, sigma_squared)
    
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")


def main():
    while True:
        display_menu()
        choice = input("Escolha uma opção (1-7): ").strip()
        if choice == "1":
            handle_mm1()
        elif choice == "2":
            handle_mmc()
        elif choice == "3":
            handle_mm1k()
        elif choice == "4":
            handle_mmck()
        elif choice == "5":
            handle_mm1n()
        elif choice == "6":
            handle_mmcn()
        elif choice == "7":
            handle_mg1()
        elif choice == "8":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()