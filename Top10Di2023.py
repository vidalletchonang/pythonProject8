import pandas as pd
import matplotlib.pyplot as plt

# Carica il dataset
data_path = "WorldHappyness2023.csv"
df = pd.read_csv(data_path, delimiter=';')

# Funzione per convertire stringhe in float
def convert_to_float(value):
    try:
        return float(value.replace(',', '.'))
    except ValueError:
        return None

# Applica la conversione alla colonna "Ladder score"
df["Ladder score"] = df["Ladder score"].apply(convert_to_float)

# Estrai i dati delle colonne "Country name" e "Ladder score"
country_ladder_data = df[["Country name", "Ladder score"]]

# Seleziona i primi 10 paesi
top_countries = country_ladder_data.head(10)

# Visualizza i dati mediante un grafico a barre
plt.figure(figsize=(12, 6))
plt.bar(top_countries["Country name"], top_countries["Ladder score"], color='skyblue')
plt.title('Top 10 Ladder per Paese in 2023')
plt.xlabel('Paese')
plt.ylabel('Punteggio Ladder')
plt.xticks(rotation=45, ha='right')  # Rotazione delle etichette sull'asse x per maggiore leggibilità
plt.tight_layout()
plt.show()

