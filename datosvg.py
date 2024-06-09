import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'vgsales.csv'
df = pd.read_csv(url)

print(df.describe())


# Configuración de Seaborn
sns.set_theme(style="whitegrid")

# Número de juegos por plataforma
plt.figure(figsize=(12, 6)) #Crea una nueva figura con un tamaño especifico

# Crea un gráfico de conteo (countplot) utilizando Seaborn, donde
# - 'y' especifica que la variable 'Platform' estará en el eje y.
# - 'data=df' indica que los datos provienen del DataFrame 'df'.
# - 'order=df['Platform'].value_counts().index' ordena las plataformas según su frecuencia, de mayor a menor.
sns.countplot(y='Platform', data=df, order=df['Platform'].value_counts().index) 
# Añade un título al gráfico
plt.title('Número de juegos por plataforma')
# Etiqueta el eje x con el texto 'Número de juegos'
plt.xlabel('Número de juegos')
# Etiqueta el eje y con el texto 'Plataforma'
plt.ylabel('Plataforma')
# Muestra el gráfico
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------

# Número de juegos por género
plt.figure(figsize=(12, 6))
sns.countplot(y='Genre', data=df, order=df['Genre'].value_counts().index)
plt.title('Número de juegos por género')
plt.xlabel('Número de juegos')
plt.ylabel('Género')
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------

# Ventas globales por plataforma

platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x=platform_sales.values, y=platform_sales.index)
plt.title('Ventas globales por plataforma')
plt.xlabel('Ventas globales (millones)')
plt.ylabel('Plataforma')
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------

# Ventas globales por género

# Agrupa el DataFrame por la columna 'Genre' y suma las ventas globales para cada género.
# Luego, ordena estos valores de ventas de manera descendente.
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

# Crea una nueva figura con un tamaño específico (ancho=12, alto=6)
plt.figure(figsize=(12, 6))
# Crea un gráfico de barras utilizando Seaborn, donde
# - 'x=genre_sales.values' especifica que los valores de ventas globales serán la variable en el eje x.
# - 'y=genre_sales.index' especifica que los géneros serán la variable en el eje y.
sns.barplot(x=genre_sales.values, y=genre_sales.index)
plt.title('Ventas globales por género')
plt.xlabel('Ventas globales (millones)')
plt.ylabel('Género')
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------

# Ventas globales a lo largo del tiempo
plt.figure(figsize=(12, 6))
# Agrupa el DataFrame por la columna 'Year' y suma las ventas globales para cada año.
# Luego, crea un gráfico de línea para mostrar la evolución de las ventas globales a lo largo del tiempo.
df.groupby('Year')['Global_Sales'].sum().plot(kind='line')
plt.title('Ventas globales a lo largo del tiempo')
plt.xlabel('Año')
plt.ylabel('Ventas globales (millones)')
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------

# Editoras más exitosas
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=publisher_sales.values, y=publisher_sales.index)
plt.title('Editoras más exitosas')
plt.xlabel('Ventas globales (millones)')
plt.ylabel('Editora')
plt.show()