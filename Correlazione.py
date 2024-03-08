import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carica il dataset
data_path = "WorldHappyness2023.csv"
df = pd.read_csv(data_path, delimiter=';')

# Funzione per convertire stringhe in float
def convert_to_float(value):
    if isinstance(value, str):
        try:
            return float(value.replace(',', '.'))
        except ValueError:
            return None
    return value

# Applica la conversione alle colonne numeriche
numeric_columns = ["Ladder score", "Logged GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Perceptions of corruption"]
for col in numeric_columns:
    df[col] = df[col].apply(convert_to_float)

# Estrai i dati dei primi 20 paesi
top_20_countries = df.head(20)

# Calcola la correlazione
correlation_matrix = top_20_countries[numeric_columns].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)

# Aggiungi i nomi delle colonne agli assi
plt.xticks(ticks=range(len(numeric_columns)), labels=numeric_columns, rotation=10)
plt.yticks(ticks=range(len(numeric_columns)), labels=numeric_columns, rotation=5)

plt.title('Correlazione tra le colonne per i Top 20 Paesi')
plt.show()
