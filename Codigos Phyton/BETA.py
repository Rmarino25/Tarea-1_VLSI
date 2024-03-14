import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('VS.txt')

# Configurar la gráfica
plt.figure(figsize=(10, 6))
for columna in df.columns[1:]:
    plt.plot(df['XVAL'], df[columna], label=columna)

plt.xlabel('XVAL')
plt.ylabel('v(in):v22')
plt.title('Gráfico de Datos PMOS')
plt.legend()
plt.grid(True)
plt.show()