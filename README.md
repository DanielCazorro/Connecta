# Connecta

Este es un juego de Conecta 4 implementado en Python, utilizando un tablero de una sola columna.

## Descripción

El juego consiste en colocar fichas en una columna. El objetivo es conectar cuatro fichas del mismo jugador de forma vertical, horizontal o diagonal en el tablero.

## Estructura del proyecto

- `linear_board.py`: Contiene la clase `LinearBoard`, que representa el tablero de una sola columna.
- `linear_board_test.py`: Pruebas unitarias para la funcionalidad del tablero.
- `list_utils.py`: Funciones de utilidad para buscar elementos en listas.
- `list_utils_test.py`: Pruebas unitarias para las funciones de utilidad.
- `settings.py`: Archivo con constantes relacionadas con las reglas del juego.

## Funcionalidades

- `LinearBoard`: Clase que representa el tablero de Conecta 4.
  - `add(char)`: Agrega una ficha al tablero.
  - `is_full()`: Verifica si el tablero está lleno.
  - `is_victory(char)`: Verifica si hay victoria para un jugador.
  - `is_tie(char1, char2)`: Verifica si el juego termina en empate.
- Funciones de utilidad en `list_utils.py` para buscar elementos en listas.

## Ejecución de pruebas

Para ejecutar las pruebas unitarias, usa el siguiente comando:
``pytest``
Asegúrate de tener pytest instalado en tu entorno.

## Configuración del juego

Puedes ajustar las reglas del juego en settings.py, donde puedes cambiar el tamaño del tablero (BOARD_LENGTH) y la cantidad de fichas necesarias para la victoria (VICTORY_STRIKE).

## Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de mejorar el juego, agregar funcionalidades o resolver problemas reportados.