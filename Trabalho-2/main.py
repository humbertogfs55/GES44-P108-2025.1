from mm1_queue import mm1_queue_metrics
from mmc_queue import mmc_queue_metrics
from mm1k_queue import mm1k_queue_metrics
from mmck_queue import mmc_k_queue_metrics
from mm1n_queue import mm1n_queue_metrics
from mmcn_queue import mmcn_queue_metrics
from mg1_queue import mg1_queue_metrics

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

console = Console()

def parse_float(value):
    return float(value.replace(',', '.'))

def display_menu():
    console.print(Panel("""
[bold cyan]--- Teoria das Filas ---[/bold cyan]
1. Modelo M/M/1
2. Modelo M/M/c
3. Modelo M/M/1/K
4. Modelo M/M/c/K
5. Modelo M/M/1/N (População finita)
6. Modelo M/M/c/N (população finita)
7. Modelo M/G/1
8. Sair
""", title="[bold green]Menu Principal"))

def print_metrics(metrics):
    table = Table(title="[bold green]Resultados")
    table.add_column("Métrica", justify="left", style="cyan", no_wrap=True)
    table.add_column("Valor", justify="right", style="yellow")

    for metric, value in metrics.items():
        if isinstance(value, list):
            val = ", ".join(f"{v:.4f}" for v in value)
        else:
            val = f"{value:.4f}"
        table.add_row(metric, val)
    console.print(table)

def handle_mm1():
    console.print("\n[bold cyan]--- Modelo M/M/1 ---[/bold cyan]")
    arrival_rate = parse_float(Prompt.ask("Digite a taxa de chegada (λ)"))
    service_rate = parse_float(Prompt.ask("Digite a taxa de serviço (μ)"))
    waiting_time_w = parse_float(Prompt.ask("Digite o tempo t1 para cálculo de P(W > t)"))
    waiting_time_wq = parse_float(Prompt.ask("Digite o tempo t2 para cálculo de P(Wq > t)"))

    metrics = mm1_queue_metrics(arrival_rate, service_rate, waiting_time_w, waiting_time_wq)
    if "Erro" in metrics:
        console.print(f"[bold red]{metrics['Erro']}")
    else:
        print_metrics(metrics)

def handle_mmc():
    console.print("\n[bold cyan]--- Modelo M/M/c ---[/bold cyan]")
    arrival_rate = parse_float(Prompt.ask("Digite a taxa de chegada (λ)"))
    service_rate = parse_float(Prompt.ask("Digite a taxa de serviço (μ)"))
    num_servers = int(Prompt.ask("Digite o número de servidores (c)"))
    waiting_time_w = parse_float(Prompt.ask("Digite o tempo t1 para cálculo de P(W > t)"))
    waiting_time_wq = parse_float(Prompt.ask("Digite o tempo t2 para cálculo de P(Wq > t)"))
    num_clients = int(Prompt.ask("Digite o número de clientes no sistema (N)"))

    metrics = mmc_queue_metrics(arrival_rate, service_rate, num_servers, waiting_time_w, waiting_time_wq, num_clients)
    if "Erro" in metrics:
        console.print(f"[bold red]{metrics['Erro']}")
    else:
        print_metrics(metrics)

def handle_mm1k():
    console.print("\n[bold cyan]--- Modelo M/M/1/K ---[/bold cyan]")
    arrival_rate = parse_float(Prompt.ask("Digite a taxa de chegada (λ)"))
    service_rate = parse_float(Prompt.ask("Digite a taxa de serviço (μ)"))
    max_capacity = int(Prompt.ask("Digite a capacidade máxima do sistema (K)"))
    waiting_cost = parse_float(Prompt.ask("Digite o custo de espera (CE)"))
    service_cost = parse_float(Prompt.ask("Digite o custo de atendimento (CA)"))
    num_clients = int(Prompt.ask("Digite o número de clientes no sistema (N)"))

    metrics = mm1k_queue_metrics(arrival_rate, service_rate, max_capacity, waiting_cost, service_cost, num_clients)
    if "Erro" in metrics:
        console.print(f"[bold red]{metrics['Erro']}")
    else:
        print_metrics(metrics)

def handle_mmck():
    console.print("\n[bold cyan]--- Modelo M/M/c/K ---[/bold cyan]")
    arrival_rate = parse_float(Prompt.ask("Digite a taxa de chegada (λ)"))
    service_rate = parse_float(Prompt.ask("Digite a taxa de serviço (μ)"))
    num_servers = int(Prompt.ask("Digite o número de servidores (c)"))
    max_capacity = int(Prompt.ask("Digite a capacidade máxima do sistema (K)"))
    waiting_cost = parse_float(Prompt.ask("Digite o custo de espera (CE)"))
    service_cost = parse_float(Prompt.ask("Digite o custo de atendimento (CA)"))
    num_clients = int(Prompt.ask("Digite o número de clientes no sistema (N)"))

    metrics = mmc_k_queue_metrics(arrival_rate, service_rate, num_servers, max_capacity, waiting_cost, service_cost, num_clients)
    if "Erro" in metrics:
        console.print(f"[bold red]{metrics['Erro']}")
    else:
        print_metrics(metrics)

def handle_mm1n():
    console.print("\n[bold cyan]--- Modelo M/M/1/N (população finita) ---[/bold cyan]")
    arrival_rate = parse_float(Prompt.ask("Digite a taxa de chegada (λ)"))
    service_rate = parse_float(Prompt.ask("Digite a taxa de serviço (μ)"))
    population_size = int(Prompt.ask("Digite o tamanho da população (N)"))
    waiting_cost = parse_float(Prompt.ask("Digite o custo de espera (CE)"))
    service_cost = parse_float(Prompt.ask("Digite o custo de atendimento (CA)"))

    metrics = mm1n_queue_metrics(arrival_rate, service_rate, population_size, waiting_cost, service_cost)
    if "Erro" in metrics:
        console.print(f"[bold red]{metrics['Erro']}")
    else:
        print_metrics(metrics)

def handle_mmcn():
    console.print("\n[bold cyan]--- Modelo M/M/s/N (população finita) ---[/bold cyan]")
    arrival_rate = parse_float(Prompt.ask("Digite a taxa de chegada (λ)"))
    service_rate = parse_float(Prompt.ask("Digite a taxa de serviço (μ)"))
    num_servers = int(Prompt.ask("Digite o número de servidores (s)"))
    population_size = int(Prompt.ask("Digite o tamanho da população (N)"))
    waiting_cost = parse_float(Prompt.ask("Digite o custo de espera (CE)"))
    service_cost = parse_float(Prompt.ask("Digite o custo de atendimento (CA)"))

    metrics = mmcn_queue_metrics(arrival_rate, service_rate, num_servers, population_size, waiting_cost, service_cost)
    if "Erro" in metrics:
        console.print(f"[bold red]{metrics['Erro']}")
    else:
        print_metrics(metrics)

def handle_mg1():
    console.print("\n[bold cyan]--- Modelo M/G/1 ---[/bold cyan]")
    arrival_rate = parse_float(Prompt.ask("Digite a taxa de chegada (λ)"))
    service_rate = parse_float(Prompt.ask("Digite a taxa de serviço (μ)"))
    sigma_squared = parse_float(Prompt.ask("Digite a variância do tempo de serviço (σ²)"))

    metrics = mg1_queue_metrics(arrival_rate, service_rate, sigma_squared)
    if "Erro" in metrics:
        console.print(f"[bold red]{metrics['Erro']}")
    else:
        print_metrics(metrics)

def main():
    while True:
        display_menu()
        choice = Prompt.ask("Escolha uma opção (1-8)")
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
            console.print("[bold green]Saindo do programa. Até logo!")
            break
        else:
            console.print("[bold red]Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
