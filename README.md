# AirDraw
Aplicación de visión por computadora que permite dibujar en pantalla con movimientos de la mano mediante el seguimiento de los dedos en tiempo real usando una cámara web


AirDraw/
│
├── main.py
├── webcam.py
├── hand_tracker.py
├── gesture_detector.py
├── canvas.py
├── particle_system.py
└── renderer.py


| Archivo               | Responsabilidad                |
| --------------------- | ------------------------------ |
|  main.py              | Orquestar la aplicación        |
|  webcam.py            | Abrir y gestionar la webcam    |
| `hand_tracker.py`     | Detectar la mano con MediaPipe |
| `gesture_detector.py` | Detectar gestos (pinch, etc.)  |
| `canvas.py`           | Gestionar el lienzo de dibujo  |
| `particle_system.py`  | Gestionar partículas           |
| `renderer.py`         | Dibujar todo en pantalla       |
