# ges44-P108-2025.1
Repositório da matéria de P108 para entrega de trabalhos.

</br>

## Trabalho 2 - Simulação de Filas (M/M/1, M/G/1, M/M/c, etc.)

Este projeto contém simulações de sistemas de filas clássicos, como M/M/1, M/G/1, M/M/c, incluindo variações com prioridades preemptivas e não-preemptivas. O foco do **Trabalho 2** é implementar e analisar o desempenho desses modelos de fila utilizando Python.

## 🛠️ Requisitos

Antes de executar os scripts, você precisa ter instalado:

- **Python 3.8 ou superior**
- **pip** (gerenciador de pacotes do Python)
- **Git** (para clonar o repositório)

## ▶️ Como Executar

1. **Clone o repositório, usando o git:**

  ```bash
   git clone https://github.com/humbertogfs55/GES44-P108-2025.1
  ```

2. **Entre na pasta do Trabalho 2:**

  ```bash
   cd Trabalho-2
  ```

3. **No terminal, execute o script principal:**
   
  ```bash
   python main.py
  ```

## 📋 Menu Interativo

Ao executar main.py, será exibido um menu como este:

  ```python
    --- Teoria das Filas ---
    1. Modelo M/M/1
    2. Modelo M/M/c
    3. Modelo M/M/1/K
    4. Modelo M/M/c/K
    5. Modelo M/M/1/N (População finita)
    6. Modelo M/M/c/N (população finita)
    7. Modelo M/G/1
    8. Modelo M/M/1 Prioridade Nao Preemptiva
    9. Modelo M/M/1 Prioridade Preemptiva
    10. Modelo M/G/1 Prioridade Nao Preemptiva
    11. Modelo M/G/1 Prioridade Preemptiva
    12. Modelo M/M/c Prioridade Nao Preemptiva
    13. Modelo M/M/c Prioridade Preemptiva
    14. Sair
  ```

Basta digitar o **número da opção desejada** e inserir os parâmetros solicitados (como taxa de chegada, taxa de serviço, número de servidores, etc.). 

👉 O programa irá então calcular e exibir os resultados do modelo escolhido.
