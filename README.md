# Comparación de rendimientos CYK

### Funcionamiento del algoritmo CYK

El algoritmo CYK es un algoritmo de análisis sintáctico que verifica si una cadena pertenece a un lenguaje definido por una gramática en CNF. Utiliza programación dinámica y construye una tabla triangular de subcadenas.

### Gramática utilizada

S → B A  
B → 'b'  
A → 'a'

Esta gramática acepta cadenas que comienzan con una b seguida de una a, como ba, baa, baaa, etc., dependiendo de ampliaciones a la gramática.

### Implementación en Python

Se desarrolló una función cyk_parser(cadena, gramatica) que aplica el algoritmo CYK sobre una cadena dada y mide el tiempo de ejecución usando el módulo time

### Implementación en Bison

Se desarrolló un parser en Bison usando la misma gramática. La cadena se ingresaba por consola y se analizaba con el parser generado por Bison. También se midió el tiempo de ejecución utilizando la librería <time.h> de C.


### Resultados y comparación

A continuación, se presenta la gráfica de comparación entre los tiempos de ejecución de CYK (Python) y Bison (C):

![image](https://github.com/user-attachments/assets/45cfb1e4-48bf-43e6-acfb-03a3100b05d0)

- Eje X: Tamaño de la cadena

- Eje Y: Tiempo de ejecución (segundos)

Como se puede observar, el algoritmo CYK en Python tiene un crecimiento cúbico en tiempo, mientras que Bison mantiene un comportamiento mucho más eficiente, incluso con cadenas largas.

### Conclusiones

CYK es un algoritmo confiable para análisis de gramáticas, pero su implementación en Python es poco eficiente para cadenas largas debido al uso intensivo de estructuras dinámicas.

Bison, al generar código en C, logra un análisis más rápido y óptimo.

La comparación muestra claramente que Bison es la mejor opción en términos de rendimiento, especialmente cuando se procesan grandes cantidades de texto.
