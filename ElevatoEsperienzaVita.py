import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


# Leggi il dataset
data_path = "WorldHappyness2023.csv"
df = pd.read_csv(data_path, delimiter=';')

# Converti la colonna "Healthy life expectancy" in formato numerico
df["Healthy life expectancy"] = df["Healthy life expectancy"].str.replace(',', '.').astype(float)

# Filtra i paesi con Healthy life expectancy più elevato
top_countries_health = df.sort_values(by="Healthy life expectancy", ascending=False).head(10)

# Carica il dataset del mondo
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Unisci il dataset del mondo con i dati dei paesi selezionati
merged_df = gpd.GeoDataFrame(pd.merge(top_countries_health, world, left_on='Country name', right_on='name', how='left'))

# Crea una mappa
fig, ax = plt.subplots(figsize=(10, 15))
world.plot(ax=ax, color='lightgrey')  # Mappa del mondo di sfondo
merged_df.plot(ax=ax, color='red', markersize=50, alpha=0.7)  # Paesi con Healthy life expectancy più elevato

# Aggiungi numeri e etichette per i paesi sulla mappa
for index, row in merged_df.iterrows():
    if row['geometry']:
        centroid_x, centroid_y = row['geometry'].centroid.xy
        plt.text(centroid_x[0], centroid_y[0], f"{row['Country name']} - {row['Healthy life expectancy']:.2f}", fontsize=8, ha='right')

plt.title('Top Paesi con Healthy life expectancy più Elevato')
plt.show()