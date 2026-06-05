# AirDraw

## MVP Version

### Descripción del proyecto

Aplicación de visión por computadora que permite dibujar en pantalla mediante movimientos de la mano, utilizando el seguimiento de los dedos en tiempo real a través de una cámara web.

| Archivo               | Responsabilidad                                   |
| --------------------- | ------------------------------------------------- |
| `main.py`             | Orquestar la aplicación                           |
| `webcam.py`           | Abrir y gestionar la webcam                       |
| `hand_tracker.py`     | Detectar la mano con MediaPipe                    |
| `gesture_detector.py` | Detectar gestos                                   |
| `canvas.py`           | Gestionar el lienzo de dibujo                     |
| `renderer.py`         | Renderizar el dibujo sobre la imagen de la cámara |

## Funcionalidades

* Apertura de la cámara web.
* Detección de manos mediante MediaPipe.
* Detección del gesto **Pinch** (pulgar e índice juntos).
* Sistema de dibujo controlado por movimientos de la mano.
* Renderizado en tiempo real.

## Ejecución

Ejecutar el proyecto:

```bash
python main.py
```

Salir de la aplicación:

```text
X
```

## Tecnologías utilizadas

* Python
* OpenCV
* MediaPipe Tasks

## Estado del proyecto

Versión MVP funcional.

## Autor

Desarrollado por Zorcis Calderón.
