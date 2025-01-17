import pandas as pd

# Caminho do arquivo corrigido
file_path = r"C:\Users\Public\Documents\AGENTESPERFORMANCE.xlsx"

try:
    # Carregar o arquivo Excel especificando o engine
    df = pd.read_excel(file_path, engine='openpyxl')
    print("Arquivo carregado com sucesso!")
    print(df.head())  # Exibe as primeiras linhas do DataFrame para verificação
except FileNotFoundError:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
except ValueError as ve:
    print(f"Erro no formato do arquivo: {ve}")
except Exception as e:
    print(f"Erro inesperado: {e}")