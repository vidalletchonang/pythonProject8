import pandas as pd

# Carico il dataset
data_path = "WorldHappyness2023.csv"
df = pd.read_csv(data_path, delimiter=';')

# 1. Classificazione dei Paesi in base al punteggio complessivo
df_ranked = df.sort_values(by="Ladder score", ascending=False)
print("Classifica dei Paesi in base al punteggio complessivo:")
print(df_ranked[["Country name", "Ladder score"]])



