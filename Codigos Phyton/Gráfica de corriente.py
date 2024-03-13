import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo .txt omitiendo las primeras dos filas y especificando el separador
df = pd.read_csv('pmos.txt', skiprows=2, sep=',', skipinitialspace=True)

# Renombrar las columnas para eliminar los espacios y los caracteres especiales
df.columns = df.columns.str.replace(r'[^a-zA-Z0-9]+', '_')

# Tomar el valor absoluto de las columnas (excepto 'XVAL')
df[df.columns[1:]] = df[df.columns[1:]].abs()

# Escalar los datos en el eje y multiplicándolos por un factor de 1e6
factor_escala = 1e6
df[df.columns[1:]] *= factor_escala

# Crear un rango de valores de 0 a 1 para el eje x
valores_x = np.linspace(0, 1, len(df))

# Configurar la gráfica
plt.figure(figsize=(10, 6))  # Tamaño de la gráfica
for columna in df.columns[1:]:  # Ignorar la columna 'XVAL'
    plt.plot(valores_x, df[columna], label=columna)

plt.xlabel('Voltaje')
plt.ylabel('Corriente (µA)')  # Añadir la unidad de microamperios
plt.title('Corriente vs Voltaje NMOS')
plt.legend()
plt.grid(True)
plt.ylim(0, 230)  # Establecer el rango del eje y, ajusta según tus datos escalados
plt.show()