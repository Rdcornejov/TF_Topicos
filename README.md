# Programación Concurrente y Distribuida

## Trabajo Final

### Integrantes:

- Jefferson Espinal Atencia (u201919607)
- Marc Diaz Quilia 
- Ronaldo Cornejo Valencia (u201816502)

### Docente: 
Luis Canaval Sánchez

### Ciclo: 2023-02

## Índice

1. Definición del problema y motivación
2. Objetivos	
3. Metodología	
4. Implementación	
5. Resultados	
6. Conclusiones
7. Anexos

## 1. Definición del Problema y motivación
### Definición del Problema
Desarrollar un sistema multi agente en el que cada agente representa un carro. El sistema debe funcionar de tal manera que los carros realicen una acción en base al impacto de otro carro.
### Motivación
La necesidad de simular el comportamiento de los vehículos en un entorno controlado, posiblemente para estudiar y mejorar el flujo de tráfico o para desarrollar sistemas autónomos de transporte.

## 2. Objetivos
* Programar a los agentes transiten por la pista y detecten las colisiones con otros agentes.
* Permitir que los agentes conozcan la posición de los carros cercanos.
* Asegurarse de que los agentes se comporten como tales y no como objetos estáticos sin interacción.

## 3. Metodología
### PADE
Es adecuada para sistemas multiagentes debido a su enfoque específico en la creación y gestión de agentes autónomos que pueden comunicarse y actuar de manera coordinada. Además, proporciona la flexibilidad necesaria para escalar el sistema y ajustar comportamientos de agentes, lo cual es crucial en la simulación de un circuito de carreras.

### QT
Esta librería nos permite crear interfaces gráficas de usuario avanzadas, lo que es esencial para visualizar la simulación del circuito de carreras. Ofrece rendimiento, portabilidad y un modelo de señales y slots para manejar eventos en tiempo real, características fundamentales para desarrollar una aplicación interactiva y multiplataforma que requiere respuestas rápidas y eficientes a las acciones de los agentes.

## 4. Implementación
### a) Archivo carAgent.py
Este archivo nos permite crear los agentes que representan un la clase CarAgent. Esta clase tiene definidos todos sus atributos al momento de inicializar y la manera cómo moverse en el mapa. Además, este agente podrá enviar información sobre su estado a los demás agentes creados por medio de la clase ComportTemporal.

### b) Archivo controlAgent.py 
En este archivo, se crea la clase ControlAgent que representa un objeto agente-servidor que recibe los mensajes (Posición, estado y tamaño) de los agentes CarAgent. Luego de obtener estos mensajes, este agente se encarga de la graficación de los carros, puesto que cada agente CarAgent le brinda sus datos cada 0.2 segundos y este puede actualizar la animación del movimiento, puesto que con la Clase MyTimedBehaviour utiliza la clase Gui para dibujar cada 0.2 segundos. Asimismo, la clase ControlAgent verifica si existe una colisión con los mensajes que son brindados por todos los agentes CarAgent. Al detectar una colisión, los elimina y no los dibuja en la animación. En la función main, simplemente crea los agentes ControlAgent y CarAgent para el funcionamiento de todo el programa.

### c) Archivo gui.py
Este archivo define una clase “Gui” que hereda de “QFrame”, un widget en la biblioteca “PySide6”. Esta es una biblioteca de Python para la creación de aplicaciones gráficas con Qt. Es decir, la clase “Gui” tiene por objetivo ser la interfaz gráfica de usuario para poder visualizar el estado de los agentes involucrados en la simulación del proyecto.

### d) Diagrama de Clases

![image](https://github.com/Rdcornejov/TF_Topicos/assets/66271146/9305fee5-3dd5-4c58-b1f7-92dcc216e60d)

## 5. Resultados

### Visualización Gráfica:

El proyecto parece ser una simulación que implica la visualización de coches en una pista. Con la clase Gui, esperarías ver una ventana gráfica con una imagen de fondo que representa la pista y varios coches representados por imágenes que cambian dependiendo de su dirección (status).

### Interacción de Agentes:

Los agentes ControlAgent y CarAgent están diseñados para simular el comportamiento de coches autónomos en la pista. Los agentes tienen un comportamiento predefinido que se ejecuta en intervalos de tiempo gracias a TimedBehaviour. Además, los coches pueden comunicarse utilizando mensajes para dar a conocer al agente ControlAgent sus estados y posiciones. Luego, ControlAgent determina si las posiciones dadas indican la ocurrencia de una colisión.

### Movimiento y Colisión:

Cada coche tiene su propio conjunto de propiedades, como status, x, y, size, y colisionado, que se utilizan para calcular su movimiento en la pista y determinar si ha ocurrido una colisión. Las colisiones cambian el estado del coche afectado y provocan la desaparición del carro de la interfaz gráfica.

### Comportamiento Temporizado:
Los comportamientos temporizados de MyTimedBehaviour y ComportTemporal actualizan el estado y la posición de los coches a intervalos regulares. Esto significa que los coches son capaces de desplazarse en la interfaz gráfica a lo largo del tiempo.

### Ejecución de la aplicación:

![image](https://github.com/Rdcornejov/TF_Topicos/assets/66271146/717d17ed-73f8-4aa7-a43b-ee4a37e1539d)

## 6. Conclusiones

* Los MAS pueden ser más eficientes, escalables y adaptables que los sistemas centralizados. Además, pueden ser utilizados para resolver problemas que son difíciles de resolver con sistemas tradicionales.
* PADE nos permitió crear y gestionar agentes autónomos que pueden comunicarse y actuar de manera coordinada. También proporciona la flexibilidad necesaria para ajustar el comportamiento de los agentes.
* La librería QT nos permitió proporcionar una interfaz gráfica de usuario, así pueda visualizar la simulación del circuito de carreras.

## 7. Anexos
* Repositorio: https://github.com/Rdcornejov/TF_Topicos/tree/main
* Video: https://youtu.be/U_n1k7Qje1M
