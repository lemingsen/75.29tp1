# Teoría de Algoritmos 1 - 2c 2021 Trabajo Práctico 1

## Lineamientos básicos
* El trabajo se realizará en forma individual.

* Se debe entregar el informe en formato pdf en el aula virtual de la materia.

* El informe debe presentar carátula con datos del autor y fecha de entrega. Debe incluir número de hoja en cada página.

* En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: Karatsuba!
Dado los siguientes números (completado por su número de padrón):

    a35b411c 
    2d98ef55

con:

    a: dígito del padrón correspondiente a la unidad
    b: dígito del padrón correspondiente a la centena
    c: los dos dígitos del padrón de la izquierda mod 7
    d: dígito del padrón correspondiente a la decena
    e: dígito del padrón correspondiente a la unidad de mil
    f: los dos dígitos del padrón de la derecha mod 9

    Ejemplo. Padrón: 95473

    33544114
    27985155

Se pide:

1. Resuelva la multiplicación paso a paso utilizando el algoritmo de Karatsuba.

2. Cuente la cantidad de sumas y multiplicaciones que realiza y relaciónelo con la complejidad temporal del método.

3. Comparar lo obtenido con el método de multiplicación tradicional. ¿Observa alguna mejora? Analice.

4. ¿Por qué se puede considerar al algoritmo de Karatsuba como de “división y conquista”?

## Parte 2: Cuestión de complejidad…
Dado la siguiente relación de recurrencia

    a T(n/b) + O(c)
Con:

    a: 1 + (los dos dígitos del padrón de la izquierda mod 9)
    b: 2 + (los dos dígitos del padrón de la izquierda mod 7)
    c: “n” si su padrón es múltiplo de 4, 
    sino “nlogn” si su padrón es múltiplo de 3,
    sino “n2”  
Se pide:

Responda y complete: 
1. ¿Qué le falta a la relación de recurrencia para que se pueda aplicar el teorema maestro?

2. Calcular la complejidad temporal utilizando el teorema maestro.

3. Explique paso a paso cómo llega a la misma.