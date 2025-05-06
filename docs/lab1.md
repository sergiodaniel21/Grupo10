# Laboratorio 1: Algoritmo Genético

## Inicialización

La función objetivo a optimizar es una parábola invertida con un máximo en `x = 31`:

$$
f(x) = -\frac{35}{961}(x - 31)^2 + 40
$$

El objetivo del algoritmo genético es encontrar el valor de `x` que maximiza `f(x)`. Cada solución (cromosoma) se representa como una cadena binaria de 6 bits, lo que permite representar enteros de 0 a 63. La población inicial consta de 4 cromosomas aleatorios.

## Ejemplo de población inicial:

| Cromosoma (binario) | Valor decimal |
| ------------------- | ------------- |
| 010100              | 20            |
| 001101              | 13            |
| 111011              | 59            |
| 001001              | 9             |

## Evaluación de la población

Se evalúa cada cromosoma aplicando la función `f(x)`:

| Genotipo | x  | f(x)  |
| -------- | -- | ----- |
| 010100   | 20 | 35.59 |
| 001101   | 13 | 28.20 |
| 111011   | 59 | 11.44 |
| 001001   | 9  | 22.37 |

## Selección

La tercera etapa del algoritmo genético consiste en la selección de los **progenitores**, es decir, la elección de los **mejores individuos** de la población actual que serán utilizados para producir la siguiente generación. Esta etapa es clave para asegurar que las **características más favorables** de las soluciones actuales sean heredadas por los nuevos individuos.

¿Qué se selecciona?
En nuestro caso, cada individuo está representado por un código binario de 6 cifras, que simboliza una posible solución al problema. A cada uno se le asigna un puntaje a través de una función de evaluación, que nos dice qué tan buena es esa solución.


$$
f(x) = -\frac{35}{961}(x - 31)^2 + 40
$$

![Grafica de la funcion objetivo](https://i.imgur.com/eKSNbHq.png)

En este caso, los mejores genotipos son:

| Genotipo | f(x)  |
| -------- | ----- |
| 010100   | 35.59 |
| 001101   | 28.20 |

Estos dos serán los progenitores que participarán en la etapa de cruce para generar la nueva generación.


## Cruce

El cruce es como el "apareamiento" en la naturaleza, donde dos padres combinan sus genes para crear nuevos hijos con características de ambos:

![Padres](https://i.imgur.com/qrniDwT.png)

En el cruce, los puntos donde se dividen los cromosomas de los padres se eligen al azar, lo que significa que cada vez puede ser en una posición diferente. Esto permite crear combinaciones diversas en los hijos. En este algoritmo, a partir de dos padres, se generan cuatro hijos.

**Primer punto de cruce:**

![Punto_de_cruce_1](https://i.imgur.com/CCKqZMp.png)

**Segundo punto de cruce:**

![Punto_de_cruce_2](https://i.imgur.com/owAEA2o.png)


## Mutación

En este caso, la mutación tiene una probabilidad del 20% (probabilidad de mutación de `𝑝=0.2`) de ocurrir en cada bit del cromosoma.

| Cromosoma (binario) | x  | p    | f(x)  |
| ------------------- | -- | ---- | ----- |
| 011101              | 29 | 0.5  | 39.85 |
| 010100              | 20 | 0.1  | 35.59 |
| 101101              | 45 | 0.15 | 32.86 |
| 001001              | 9  | 0.23 | 22.37 |

````
