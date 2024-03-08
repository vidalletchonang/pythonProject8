import pandas as pd
import matplotlib.pyplot as plt

# Carico il dataset
data_path = "WorldHappyness2023.csv"
df = pd.read_csv(data_path, delimiter=';')

# Funzione per convertire stringhe in float
def convert_to_float(value):
    try:
        return float(value.replace(',', '.'))
    except ValueError:
        return None

# Applico la conversione alla colonna "Ladder score"
df["Ladder score"] = df["Ladder score"].apply(convert_to_float)

# Estrai i dati delle colonne "Country name" e "Ladder score"
country_ladder_data = df[["Country name", "Ladder score"]]

# Seleziono gli ultimi 10 paesi
bottom_countries = country_ladder_data.tail(20)

# Visualizzo i dati mediante un grafico a barre
plt.figure(figsize=(12, 6))
plt.bar(bottom_countries["Country name"], bottom_countries["Ladder score"], color='salmon')
plt.title('Ultimi 10 Punteggi Ladder per Paese')
plt.xlabel('Paese')
plt.ylabel('Punteggio Ladder')
plt.xticks(rotation=45, ha='right')  # Rotazione delle etichette sull'asse x per maggiore leggibilità
plt.tight_layout()
plt.show()


