# randomizator - gmacias-
Randomizer es un programa simple en Python diseñado para generar una lista de números aleatorios no repetidos dentro de un rango específico.

### Indice
* [Que es Randomizer?](#que-es-Randomizer)
* [Que utilizamos?](#que-utilizamos)
* [Como funciona?](#como-funciona)
* [Como utilizamos la función?](#como-utilizamos-la-función)
* [Ejemplos:](#Ejemplos)

## ¿Qué es Randomizer?

Randomizer es como tu propio asistente personal para tomar decisiones difíciles, ¡como elegir qué hacer o a quién asignar tareas! 
Es un pequeño programa en Python que se encarga de generar una lista de números al azar dentro de un rango que tú determines. 
Es perfecto para situaciones en las que necesitas un poco de ayuda para hacer elecciones al azar, como formar grupos o decidir quién comienza un juego.

## ¿Qué utilizamos?

El programa utiliza el lenguaje de programación Python y algunas funciones de las bibliotecas estándar. Aquí hay algunas de las funciones utilizadas:

| Función               | Descripción                                    |
|-----------------------|------------------------------------------------|
| `abs()`               | Devuelve el valor absoluto de un número.       |
| `isinstance()`        | Comprueba si un objeto es una instancia de una clase o tipo específico. |
| `input()`             | Lee la entrada del usuario desde la consola.   |
| `print()`             | Imprime mensajes en la consola.                |
| `range()`             | Genera una secuencia de números en un rango especificado. |
| `join()`              | Une elementos de una lista en una cadena usando un separador. |

## ¿Cómo funciona?

Randomizer opera mediante el uso de cuatro variables principales para personalizar su comportamiento:

1. **limite_1**: Este valor representa el límite inferior del rango de números del cual se seleccionarán los elementos. Es el punto de inicio de la secuencia numérica.

2. **limite_2**: Este valor establece el límite superior del rango. Todos los números seleccionados estarán dentro de este rango inclusive. Define el final de la secuencia numérica.

3. **numeros_por_mostrar**: Indica cuántos números aleatorios no repetidos se seleccionarán de la secuencia generada.

4. **separador**: Es un carácter especial que determina cómo se formateará la salida final que muestra los números seleccionados. Por defecto, se utiliza la coma y un espacio (`, `), pero puede cambiarse según las preferencias del usuario.

El proceso de ejecución del programa sigue estos pasos:

- Se genera una secuencia de números mediante la función `range()` dentro del rango especificado por **limite_1** y **limite_2**.

- Se verifica que haya suficientes números en la secuencia para seleccionar la cantidad especificada por **numeros_por_mostrar**.

- Utilizando la función `random.sample()`, se seleccionan aleatoriamente los números requeridos sin permitir repeticiones.

- Los números seleccionados se unen en una lista utilizando el separador especificado y se muestra el resultado.

Este enfoque garantiza la aleatoriedad, la no repetición y la flexibilidad en la generación de números dentro del rango definido por el usuario.

## ¿Cómo utilizamos la función?

Para aprovechar al máximo el Generador Utilitario de Números Aleatorios, sigue estos pasos:

1. **Clonar el Repositorio:**
   - Abre tu terminal y ejecuta el siguiente comando para clonar el repositorio:

     ```bash
     git clone https://github.com/gjmacias/randomizator
     cd randomizator
     ```
   - Esto descargará el código fuente del generador en tu máquina.

2. **Asignar Permisos de Ejecución:**

   - Asigna permisos de ejecución al script con uno de los siguientes comandos:

     ```bash
     chmod +x randomizer.py   ||   chmod 755 randomizer.py
     ```
   
   Esto permite que el sistema ejecute el script.

3. **Ejecutar el Generador:**
   - Inicia el programa escribiendo:

     ```bash
     python randomizer.py   ||   ./randomizer
     ```
   - Asegúrate de tener Python instalado en tu sistema. Si no lo tienes, puedes obtenerlo en el sitio web de Python
   - Experimenta con diferentes combinaciones para adaptar el generador a tus necesidades.

## Ejemplos:

      Please, insert first limit: 1
      Please, insert second limit: 10
      Please, insert the quantity of numbers to show: 5
      Enter the separator (default ', '): 
      Select numbers : 5, 3, 8, 1, 10
---
      Please, insert first limit: -100
      Please, insert second limit: 100
      Please, insert the quantity of numbers to show: 10
      Enter the separator (default ', '): |
      Select numbers : 68|89|-35|-25|-46|-95|-60|38|-14|-10
---
      Please, insert first limit: 20
      Please, insert second limit: 50
      Please, insert the quantity of numbers to show: 3
      Enter the separator (default ', '):  
      Select numbers : 36, 23, 26

¡Ahora estás listo para explorar y disfrutar de los números sorpresa! 🎲

# Quizás pueda interesarte!

### - Para ver mi progresion en 42 🌠
[AQUÍ](https://github.com/gjmacias/42BCN)

### - Mi perfil de 42 👾
[AQUÍ](https://profile.intra.42.fr/users/gmacias-)

### - Mis proyectos personales 🧐
[AQUÍ](https://github.com/gjmacias/autoproyectos)

# Contacto 📥

◦ Email: gmacias-@student.42barcelona.com

[1]: https://www.42barcelona.com/ "42 BCN"
