import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df = pd.read_excel(r'C:\Users\tayur\OneDrive\Documentos\Asistencia\Tratamientos\Graficos\Libro.xlsx')

# Assuming the DataFrame has columns for the x-axis and y-axis values
x_values = df['tiempo']
y0_values = df["pulso"]
y1_values = df['v1']
y2_values = df['v2']
y3_values = df['v3']
# Create a plot
plt.plot(x_values, y0_values, color="b", label="Vin")
plt.plot(x_values, y1_values, color="r", label="Relación de 1.5/1")
plt.plot(x_values, y2_values, color="c", label="Relación de 2/1")
plt.plot(x_values, y3_values, color="m", label="Relación de 2.5/1")
# Add labels and a title
plt.xlabel('Tiempo')
plt.ylabel('Voltaje')
plt.title('Tiempos de retardo')
plt.legend(loc="upper right")

# Display the plot
plt.show()
