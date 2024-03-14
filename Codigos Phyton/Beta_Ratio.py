import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df = pd.read_excel(r'C:\Users\tayur\OneDrive\Documentos\Tec\VLSI\Tareas\Tarea1\Book1.xlsx')

# Assuming the DataFrame has columns for the x-axis and y-axis values
x_values = df['tiempo']
#y0_values = df["pulso"]
y1_values = df['v1']
y2_values = df['v2']
y3_values = df['v3']
y4_values = df['v4']
y5_values = df['v5']
y6_values = df['v6']
# Create a plot
plt.plot(x_values, y1_values, color="b", label="Relación p/n: 1")
plt.plot(x_values, y2_values, color="r", label="Relación p/n: 1.5")
plt.plot(x_values, y3_values, color="c", label="Relación p/n: 2")
plt.plot(x_values, y4_values, color="m", label="Relación p/n: 2.5")
plt.plot(x_values, y5_values, color="y", label="Relación p/n: 3")
plt.plot(x_values, y6_values, color="k", label="Relación p/n: 3.5")
# Add labels and a title
plt.xlabel('Vin')
plt.ylabel('Vout')
plt.title('Relación de tamaños p/n')
plt.legend(loc="upper right")

# Display the plot
plt.show()
