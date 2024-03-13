# Tarea-1_VLSI
Este proyecto se enfoca en el diseño y la simulación de circuitos integrados utilizando la tecnología específica del transistor mínimo. Se dividirá en dos partes principales: la determinación de resistencias y capacitancias mínimas, y el diseño de un inversor óptimo.

En la primera parte, se realizarán cálculos y simulaciones para determinar las resistencias de canal de transistores mínimos NMOS y PMOS, así como la capacitancia equivalente de compuerta. Esto proporcionará una estimación inicial de las características del proceso que se utilizarán a lo largo del curso.

En la segunda parte, se diseñará un inversor mínimo con margen de ruido simétrico, utilizando herramientas de simulación para verificar su funcionamiento y analizar su desempeño bajo diferentes condiciones. Se realizarán iteraciones para encontrar una solución empírica razonable de la relación PMOS/NMOS y se llevarán a cabo pruebas adicionales para evaluar el comportamiento del inversor.

## Parte 1:
Para la primera parte se determinaron la resistencia del transistor de tipo N y el de tipo P de tamaño mínimo, se realizó de la siguiente manera:

$$\ R = \frac{V_{DD}}{2 \cdot I_{DSAT}} \ $$ 

Para el N quedaría de la siguiente manera:
$$\frac{1.8 \text{V}}{2 \cdot 475 \times 10^{-6} \text{A/um} \times 0.36 \mu m} = 5263.16  \Omega$$


Para el P quedaría de la siguiente manera:
$$\frac{1.8 \text{V}}{2 \cdot 170 \times 10^{-6} \text{A/um} \times 0.72 \mu m} = 6965.94  \Omega$$

Utilizando la otra formula:

$$R = \frac{V_{DD}}{I_H + I_L}$$

Para determinar la resistencia del N se hace de la siguiente manera:

$$\frac{1.8 \text{V}}{{475 \times 10^{-6} \text{A/um} + 0}} \times 0.36 \mu m  = 10526.31 \Omega$$

Y la del P quedria:

$$\frac{1.8 \text{V}}{{170 \times 10^{-6} \text{A/um} + 0}} \times 0.72 \mu m = 13931.89 \Omega$$

Ahora para determinar la resistencia unitaria se debe de multiplicar por por el ancho usado en este caso 0.36 \mu m para el N y 0.76 para el P 

$$R_{\text{nueff}} = 10526.31 \Omega \times 0.36 \mu m$$

$$R_{\text{nueff}} = 3789.47 \frac{\Omega}{\mu m}$$

$$R_{\text{pueff}} = 13931.89 \\Omega \times 0.72 \mu m$$

$$R_{\text{pueff}} = 10030.96 \frac{\Omega}{\mu m}$$

Ahora bien para calcular las capacitancias se puede determinar de la siguiente manera, siendo la más pesimista

$$C_{gs} = W_{dib} \times L_{dib} \times C_{OX}$$

La capacitancia del N queda de la siguiente manera:

$$0.36 \mu m \times 0.18 \mu m \times 8.46 \times 10^{-15} \text{A/um} = 5.48 \times 10^{-16} F $$

Y la del P:

$$0.72 \mu m \times 0.18 \mu m \times 8.46 \times 10^{-15} \text{A/um} = 11.55 \times 10^{-16} F $$

Para calcular los tiempos se utiliza la siguiente formula:

$$\tau = 3 \times R \times C$$

Para el N:

$$3 \times 10526.31 \Omega \times 5.48 \times 10^{-16} F = 17.3 \ \text{ps}$$

Para el P:

$$3 \times 13931.89 \Omega \times 11.55 \times 10^{-16} F = 48.07 \ \text{ps}$$

## Parte 2:


\[
\frac{V_{DD}}{2 \cdot I_{DSAT}}
\]
## Datos Relevantes
### Para generar listas
* Punto 1
* Punto 2
* Punto 3
## Solución
### Para insertar código
```python
import time
while True
  print("This is a python code")
  time.sleep(5)
```
## Resultados
### Para insertar una tabla 

|  Info1  |  Info2  |  Info3  |  Info4  |
|  :---  |  ---:  |  :---:  |  ---  |
|  A  |  B  |  C  |  D  |
|  AA  |  BB  |  CC  |  DD  |

## Análisis
### Incluir figuras 
![Logo](figuras/Firma_TEC.png)
