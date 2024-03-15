# Tarea-1_VLSI
Este proyecto se enfoca en el diseño y la simulación de circuitos integrados utilizando la tecnología específica del transistor mínimo. Se dividirá en dos partes principales: la determinación de resistencias y capacitancias mínimas, y el diseño de un inversor óptimo.

En la primera parte, se realizarán cálculos y simulaciones para determinar las resistencias de canal de transistores mínimos NMOS y PMOS, así como la capacitancia equivalente de compuerta. Esto proporcionará una estimación inicial de las características del proceso que se utilizarán a lo largo del curso.

En la segunda parte, se diseñará un inversor mínimo con margen de ruido simétrico, utilizando herramientas de simulación para verificar su funcionamiento y analizar su desempeño bajo diferentes condiciones. Se realizarán iteraciones para encontrar una solución empírica razonable de la relación PMOS/NMOS y se llevarán a cabo pruebas adicionales para evaluar el comportamiento del inversor.

## Parte 1:
Para la primera parte se determinaron la resistencia del transistor de tipo N y el de tipo P de tamaño mínimo, se realizó de la siguiente manera:

$$\ R = \frac{V_{DD}}{2 \cdot I_{DSAT}} \ $$ 

Para el N quedaría de la siguiente manera:
$$\frac{1.8 \text{V}}{2 \cdot 475 \times 10^{-6} \text{A/um} \cdot 0.36 \mu m} = 5263.16  \Omega$$


Para el P quedaría de la siguiente manera:
$$\frac{1.8 \text{V}}{2 \cdot 170 \times 10^{-6} \text{A/um} \cdot 0.72 \mu m} = 6965.94  \Omega$$

Utilizando la otra formula:

$$R = \frac{V_{DD}}{I_H + I_L}$$

Para determinar la resistencia del N se hace de la siguiente manera:

$$\frac{1.8 \text{V}}{{475 \times 10^{-6} \text{A/um}} \cdot 0.36 \mu m}  = 10526.31 \Omega$$

Y la del P quedria:

$$\frac{1.8 \text{V}}{{170 \times 10^{-6} \text{A/um}} \cdot 0.72 \mu m} = 14705.88 \Omega$$

Ahora para determinar la resistencia unitaria se debe de multiplicar por por el ancho usado en este caso 0.36 \mu m para el N y 0.76 para el P 

$$R_{\text{nueff}} = 10526.31 \Omega \cdot 0.36 \mu m$$

$$R_{\text{nueff}} = 3789.47 \frac{\Omega}{\mu m}$$

$$R_{\text{pueff}} = 14705.88 \\Omega \cdot 0.72 \mu m$$

$$R_{\text{pueff}} = 11176.47 \frac{\Omega}{\mu m}$$

Ahora bien para calcular las capacitancias se puede determinar de la siguiente manera, siendo la más pesimista

$$C_{gs} = W_{dib} \cdot L_{dib} \cdot C_{OX}$$

La capacitancia del N queda de la siguiente manera:

$$0.36 \mu m \cdot 0.18 \mu m \cdot 8.46 \times 10^{-15} \text{A/um} = 5.48 \times 10^{-16} F $$

Y la del P:

$$0.72 \mu m \cdot 0.18 \mu m \cdot 8.91 \times 10^{-15} \text{A/um} = 11.55 \times 10^{-16} F $$

Para calcular los tiempos se utiliza la siguiente formula:

$$\tau = 3 \cdot R \cdot C$$

Para el N:

$$3 \cdot 10526.31 \Omega \cdot 5.48 \times 10^{-16} F = 17.3 \ \text{ps}$$

Para el P:

$$3 \cdot 14705.88 \Omega \cdot 11.55 \times 10^{-16} F = 25.48 \ \text{ps}$$

## Parte 2:
Con respecto al inversor, se diseñó uno a nivel de esquemático, de un tamaño mínimo permitido por la tecnología propuesta. El funcionamiento del mismo se puede ver en las siguientes figuras, donde en la primera se logra apreciar el funcioamiento del inversor en un único pulso, mostrando así con más detalle el comportamiento del voltaje de salida.

<p align="center">
    <img src="https://github.com/Rmarino25/Tarea-1_VLSI/assets/110320407/40297304-6ed0-4d2c-b9e2-d01c9d4f35ec"/>
</p>

En la segunda imagen, se crea un tren de pulsos, mostrando así un funcionamiento "macro" del inversor.

<p align="center">
    <img src="https://github.com/Rmarino25/Tarea-1_VLSI/assets/110320407/dd250a39-cf4c-4e9f-8a62-de82065af6fb"/>
</p>

Simulando diferentes relaciones de tamaño para el inversor, nos da como resultado la siguiente gráfica. El transistor mínimo se encuentra en una relación %%%
Está relación se puede determinar cuando el valor de V_{in} es V_{DD}/2

&&&&&&&&&&&&&&imagen&&&&&&&&&&&&&&&&&&

Ahora bien analizando la corriente que pasa por el transistor de tipo N, podemos graficar la curva característivca de la siguiente manera:

<p align="center">
    <img src="https://github.com/Rmarino25/Tarea-1_VLSI/assets/110353604/ce6679be-bba1-4808-a52b-e00c02c8c602"/>
</p>

Posteriormente, se ejecutaron varias iteraciones, buscando un valor óptimo de la relación de tamaño entre el transistor p y el n. Esta relación se encontró alrededor de 2.8 veces el tamaño del transistor p con respecto al n. Se encontró que al aumentar más la relación de 2.8/1 se reduce el tiempo de subida pero se empieza a aumentar el tiempo de bajada, perdiendo así la idea de que los dos tiempos, tanto el de subida como bajada, sean lo más cercanos posibles. Los tiempos obtenidos tanto en simulación como mediante hspice se pueden ver en las siguientes figuras.

<p align="center">
    <img src="https://github.com/Rmarino25/Tarea-1_VLSI/assets/110320407/737b5224-d381-435d-9fe3-570fca60536c"/>
</p>

<p align="center">
    <img src="https://github.com/Rmarino25/Tarea-1_VLSI/assets/110320407/f30aa16d-900e-4dc8-945f-f7b0db4eb34e"/>
</p>

Seguidamente se realizaron simulaciones sobre las esquinas de varuablidad del proceso, lo que da como resultado:

&&&&&&&&&&&&&&imagen&&&&&&&&&&&&&&&&&&

Con respecto al FO4, se ejecutó el deck de SPICE manteniendo una relación de 2/1 y se encontraron los tiempos de retardo, tanto de bajada como de subida.

<p align="center">
    <img src="https://github.com/Rmarino25/Tarea-1_VLSI/assets/110320407/95561c92-9deb-4d0f-ab96-0c87133ee8c2"/>
</p>

<p align="center">
    <img src="https://github.com/Rmarino25/Tarea-1_VLSI/assets/110320407/8cf57f1d-4042-458b-8551-d7e78e301c2d"/>
</p>

 Ya teniendo los resultados del FO4, se varió la relación de tamaño p/n, obteniedo así diferentes valores de retardo para cada uno. Estos comportamientos se graficaron mediante un script de python, evidenciando la diferencia que existe en los tiempos de retardo.

<p align="center">
    <img src="https://github.com/Rmarino25/Tarea-1_VLSI/assets/110320407/3c271f1d-368f-4707-8a12-c6a5449f3967"/>
</p>

Luego se montó el FO4 optimizado, lo cual hizo que se redujeran los tiempo de subida y bajada, dando como resultado las siguientes figuras:

<p align="center">
    <img src="https://github.com/Rmarino25/Tarea-1_VLSI/assets/110353604/983c4f64-87e3-4cb4-853f-84b6a9fe7dbf"/>
</p>

<p align="center">
    <img src="https://github.com/Rmarino25/Tarea-1_VLSI/assets/110353604/4f2b4426-d4a3-4139-880d-ae37fb767024"/>
</p>


////Conclussss/////

$$\tau = 3 \cdot R \cdot C$$

Para el N:

$$R = \frac{17.3 \ \text{ps}}{3 \times 5.48 \times 10^{-16} F}$$

Para el P:

$$ R = \frac{25.48 \ \text{ps}}{3 \times 11.55 \times 10^{-16} F} $$

### Incluir figuras 
![Logo](figuras/Firma_TEC.png)
