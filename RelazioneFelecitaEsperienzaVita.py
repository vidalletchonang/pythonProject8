import pandas as pd
import matplotlib.pyplot as plt

# Carica il dataset
data_path = "WorldHappyness2023.csv"
df = pd.read_csv(data_path, delimiter=';')

# Seleziona i primi 10 paesi
top_countries = df.sort_values(by="Healthy life expectancy", ascending=False).head(10)

# Visualizza i dati mediante un grafico a dispersione
plt.figure(figsize=(12, 6))
plt.scatter(top_countries["Ladder score"], top_countries["Healthy life expectancy"], color='blue', s=100)

# Aggiungi etichette per ciascun punto
for i, row in top_countries.iterrows():
    plt.text(row["Ladder score"], row["Healthy life expectancy"], row["Country name"], fontsize=8, ha='left')

plt.title('Relazione tra Ladder score e Healthy life expectancy (Top 10 Paesi)')
plt.xlabel('Ladder score')
plt.ylabel('Healthy life expectancy')
plt.grid(True)
plt.show()


