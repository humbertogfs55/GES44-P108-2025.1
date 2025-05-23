from mm1_queue import mm1_queue_metrics
from mmc_queue import mmc_queue_metrics
from mm1k_queue import mm1k_queue_metrics
from mm1_finitePopulation import mm1_finite_population_metrics
from mmck_queue import mmc_k_queue_metrics


def display_menu():
    print("\n--- Teoria das Filas ---")
    print("1. Modelo M/M/1")
    print("2. Modelo M/M/1 População finita")
    print("3. Modelo M/M/c")
    print("4. Modelo M/M/1/K")
    print("5. Modelo M/M/c/K")
    print("6. Sair")
    print("------------------------")


def handle_mm1():
    print("\n--- Modelo M/M/1 ---")
    arrival_rate = float(input("Digite a taxa de chegada (λ): "))
    service_rate = float(input("Digite a taxa de serviço (μ): "))
    waiting_time = float(
        input("Digite o tempo t para cálculo de P(W > t) e P(Wq > t): "))
    metrics = mm1_queue_metrics(arrival_rate, service_rate, waiting_time)
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")


def handle_mm1_finite():
    print("\n--- Modelo M/M/1 População finita ---")
    arrival_rate = float(input("Digite a taxa de chegada (λ): "))
    service_rate = float(input("Digite a taxa de serviço (μ): "))
    population_size = int(input("Digite o tamanho da população (N): "))
    metrics = mm1_finite_population_metrics(
        arrival_rate, service_rate, population_size)
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            if isinstance(value, list):
                print(f"{metric}: {', '.join(f'{v:.4f}' for v in value)}")
            else:
                print(f"{metric}: {value:.4f}")


def handle_mmc():
    print("\n--- Modelo M/M/c ---")
    arrival_rate = float(input("Digite a taxa de chegada (λ): "))
    service_rate = float(input("Digite a taxa de serviço (μ): "))
    num_servers = int(input("Digite o número de servidores (c): "))
    metrics = mmc_queue_metrics(arrival_rate, service_rate, num_servers)
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")


def handle_mm1k():
    print("\n--- Modelo M/M/1/K ---")
    arrival_rate = float(input("Digite a taxa de chegada (λ): "))
    service_rate = float(input("Digite a taxa de serviço (μ): "))
    max_capacity = int(input("Digite a capacidade máxima do sistema (K): "))
    metrics = mm1k_queue_metrics(arrival_rate, service_rate, max_capacity)
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")


def handle_mmc_k():
    print("\n--- Modelo M/M/c/K ---")
    arrival_rate = float(input("Digite a taxa de chegada (λ): "))
    service_rate = float(input("Digite a taxa de serviço (μ): "))
    num_servers = int(input("Digite o número de servidores (c): "))
    max_capacity = int(input("Digite a capacidade máxima do sistema (K): "))
    metrics = mmc_k_queue_metrics(
        arrival_rate, service_rate, num_servers, max_capacity)
    if "Erro" in metrics:
        print(metrics["Erro"])
    else:
        for metric, value in metrics.items():
            if isinstance(value, list):
                print(f"{metric}: {', '.join(f'{v:.4f}' for v in value)}")
            else:
                print(f"{metric}: {value:.4f}")


def main():
    while True:
        display_menu()
        choice = input("Escolha uma opção (1-5): ").strip()
        if choice == "1":
            handle_mm1()
        elif choice == "2":
            handle_mm1_finite()
        elif choice == "3":
            handle_mmc()
        elif choice == "4":
            handle_mm1k()
        elif choice == "5":
            handle_mmc_k()
        elif choice == "6":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
