import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definição dos caminhos dos arquivos
caminho = "/home/sifapsc/scripts/scripts_everton/comparacoes"

arquivo_merge = "/dados_merge.csv"
arquivo_samet = "/dados_samet.csv"
arquivo_norte = "/DAILY_IFLORI152_2023.csv"
arquivo_centro = "/DAILY_IFLORI114_2023.csv"
arquivo_sul = "/DAILY_IFLORI172_2023.csv"

# Leitura dos arquivos CSV
merge = pd.read_csv(f"{caminho}{arquivo_merge}")
samet = pd.read_csv(f"{caminho}{arquivo_samet}")
norte = pd.read_csv(f"{caminho}{arquivo_norte}")
centro = pd.read_csv(f"{caminho}{arquivo_centro}")
sul = pd.read_csv(f"{caminho}{arquivo_sul}")

# Convertendo a coluna DATA para datetime
norte["DATA"] = pd.to_datetime(norte["DATA"])
centro["DATA"] = pd.to_datetime(centro["DATA"])
sul["DATA"] = pd.to_datetime(sul["DATA"])

# Extração dos dados relevantes
tempo_norte = norte["DATA"]
tempo_centro = centro["DATA"]
tempo_sul = sul["DATA"]

# Temperatura e Precipitação das EdBC
tmed_norte, prec_norte = norte["TMED"], norte["CHUVA"]
tmed_centro, prec_centro = centro["TMED"], centro["CHUVA"]
tmed_sul, prec_sul = sul["TMED"], sul["CHUVA"]

# MERGE e SAMeT
samet_norte, merge_norte = samet["NORTE"], merge["NORTE"]
samet_centro, merge_centro = samet["CENTRO"], merge["CENTRO"]
samet_sul, merge_sul = samet["SUL"], merge["SUL"]

# Definir os labels do eixo X
ticks_labels = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']

# Criar os ticks na posição do primeiro dia de cada mês
ticks_positions = [tempo_norte[tempo_norte.dt.month == i].iloc[0] for i in range(1, 13) if i in tempo_norte.dt.month.values]

# Criando os gráficos
fig, axs = plt.subplots(3, 2, figsize=(14, 12))

# Função para aplicar os labels corretamente
def formatar_eixo_x(ax, tempo):
    ax.set_xticks(ticks_positions)
    ax.set_xticklabels(ticks_labels, rotation=45)
    ax.set_xlim(tempo.min(), tempo.max())

# Gráficos de linha (Temperatura Média vs SAMeT)
axs[0, 0].plot(tempo_norte, tmed_norte, label="TMED Norte", color="blue")
axs[0, 0].plot(tempo_norte, samet_norte, label="SAMeT Norte", color="red", linestyle="dashed")
axs[0, 0].set_title("TMED Norte vs SAMeT Norte")
axs[0, 0].legend()
formatar_eixo_x(axs[0, 0], tempo_norte)

axs[1, 0].plot(tempo_centro, tmed_centro, label="TMED Centro", color="blue")
axs[1, 0].plot(tempo_centro, samet_centro, label="SAMeT Centro", color="red", linestyle="dashed")
axs[1, 0].set_title("TMED Centro vs SAMeT Centro")
axs[1, 0].legend()
formatar_eixo_x(axs[1, 0], tempo_centro)

axs[2, 0].plot(tempo_sul, tmed_sul, label="TMED Sul", color="blue")
axs[2, 0].plot(tempo_sul, samet_sul, label="SAMeT Sul", color="red", linestyle="dashed")
axs[2, 0].set_title("TMED Sul vs SAMeT Sul")
axs[2, 0].legend()
formatar_eixo_x(axs[2, 0], tempo_sul)

# Gráficos de barras (Precipitação vs MERGE)
axs[0, 1].bar(tempo_norte, prec_norte, label="CHUVA Norte", color="blue", alpha=0.6)
axs[0, 1].bar(tempo_norte, merge_norte, label="MERGE Norte", color="red", alpha=0.6)
axs[0, 1].set_title("Precipitação Norte vs MERGE")
axs[0, 1].legend()
formatar_eixo_x(axs[0, 1], tempo_norte)

axs[1, 1].bar(tempo_centro, prec_centro, label="CHUVA Centro", color="blue", alpha=0.6)
axs[1, 1].bar(tempo_centro, merge_centro, label="MERGE Centro", color="red", alpha=0.6)
axs[1, 1].set_title("Precipitação Centro vs MERGE")
axs[1, 1].legend()
formatar_eixo_x(axs[1, 1], tempo_centro)

axs[2, 1].bar(tempo_sul, prec_sul, label="CHUVA Sul", color="blue", alpha=0.6)
axs[2, 1].bar(tempo_sul, merge_sul, label="MERGE Sul", color="red", alpha=0.6)
axs[2, 1].set_title("Precipitação Sul vs MERGE")
axs[2, 1].legend()
formatar_eixo_x(axs[2, 1], tempo_sul)

# Ajustando layout
plt.tight_layout()

# Salvando o gráfico como PNG
plt.savefig("comparacoes_3.png", dpi=300)

# Exibindo o gráfico
plt.show()

