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

Python (rojo): curva de crecimiento rápida (como O(n³))

Bison (verde): curva más plana, eficiente y manejable

Esto prueba que Bison es más óptimo para análisis sintáctico usando este tipo de algoritmos.

![image](https://github.com/user-attachments/assets/54f86f02-9a5f-44f6-b32b-ed0ee36c8891)


- Cada punto en la gráfica representa el tiempo estimado que tomaría analizar una cadena de longitud X usando el algoritmo CYK.

- Los tiempos en Python aumentan rápidamente porque el algoritmo analiza muchas combinaciones.

- Los tiempos en Bison aumentan mucho más lentamente, porque su implementación en C es compilada y optimizada.



### Conclusiones

CYK es un algoritmo confiable para análisis de gramáticas, pero su implementación en Python es poco eficiente para cadenas largas debido al uso intensivo de estructuras dinámicas.

Bison, al generar código en C, logra un análisis más rápido y óptimo.

La comparación muestra claramente que Bison es la mejor opción en términos de rendimiento, especialmente cuando se procesan grandes cantidades de texto.
