# Local Tangent Space Alignment (LTSA)
Local Tangent Space Alignment (LTSA) es un algoritmo de reducción de dimensión y aprendizaje de variedad que apróxima el espacio local tangente a cada punto de un conjunto de entrenamiento para posteriormente alinear los subespacios reconstruyendo de esta forma la variedad.

## Algoritmo
El algoritmo recibe de entrada un conjunto de puntos X que describen una variedad de dimensión d en un espacio de dimensión m. Para cada punto se calculan los k-vecinos mas cercanos y se apróxima la geometría local de ese punto mediante el cálculo del plano tangente. Posteriormente se pega cada uno de los espacios tangentes minimizando el error de reconstrucción.




![im3](https://user-images.githubusercontent.com/30848298/29102260-75c1414a-7c7d-11e7-8b6c-ef115bbe63aa.png)
