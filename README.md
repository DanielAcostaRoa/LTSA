# Local Tangent Space Alignment (LTSA)
Local Tangent Space Alignment (LTSA) es un algoritmo de reducción de dimensión y aprendizaje de variedad que apróxima el espacio local tangente a cada punto de un conjunto de entrenamiento para posteriormente alinear los subespacios reconstruyendo de esta forma la variedad.

## Algoritmo
El algoritmo recibe de entrada un conjunto de puntos X que describen una variedad de dimensión d en un espacio de dimensión m. Para cada punto se calculan los k-vecinos mas cercanos y se apróxima la geometría local de ese punto mediante el cálculo del plano tangente. Posteriormente se pega cada uno de los espacios tangentes minimizando el error de reconstrucción.

![im6](https://user-images.githubusercontent.com/30848298/29102954-51aff27e-7c82-11e7-9c01-1d746989e85c.png)

### Resultados

Observemos en la imagen un ejemplo de una curva en el espacio tridimensional. Mediante la aplicación del algoritmo LTSA observamos la gráfica que compara las coordenadas reales contra las coordenadas estimadas por el LTSA, observamos una buena aproximación de las coordenadas.

![im3](https://user-images.githubusercontent.com/30848298/29102260-75c1414a-7c7d-11e7-8b6c-ef115bbe63aa.png)

Aplicamos el algoritmo LTSA una base de datos de imágenes de rostros. La base de datos consta de 600 imágenes de 28x20 pixeles del rostro de una persona vista desde varios ángulos, distinta iluminación y diversos gestos. Cada imagen se considero como un vector de dimensión 560 y se le aplicó el algoritmo LTSA reduciendo la dimensión a dos. Podemos observar en la imágen de abajo como el algoritmo conserva cierta estructura separando las imágenes idéntificando diversos gestos.

![im4](https://user-images.githubusercontent.com/30848298/29103427-18372adc-7c85-11e7-87d6-2a3ed016c9d7.png)

Por último mostramos la estructura encontrada al aplicar el algoritmo LTSA a la base de datos MNIST restringiendo sólo a los dígitos 0s y 1s.

