
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPainter, QPixmap
from PySide6.QtWidgets import QFrame

class Gui(QFrame):
    def __init__(self, agent) -> None:
        super(Gui, self).__init__()
        self.agent = agent
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFixedSize(640, 640)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        pista = QImage("./Imagen/pista.png")
        painter.drawImage(0,0,pista)
        for car in self.agent.cars:
            # Cargar la imagen del pez
            if car.status == 1:
                car_image = QImage("./Imagen/car_right.png")
                car_image = car_image.scaled(car.size*2, car.size)
            elif car.status == 2:
                car_image = QImage("./Imagen/car_left.png")
                car_image = car_image.scaled(car.size*2, car.size)
            elif car.status == 3:
                car_image = QImage("./Imagen/car_up.png")
                car_image = car_image.scaled(car.size, car.size*2)
            elif car.status == 4:
                car_image = QImage("./Imagen/car_down.png")
                car_image = car_image.scaled(car.size, car.size*2)
            else:
                car_image = QImage("./Imagen/car_left.png")
                car_image = car_image.scaled(car.size*2, car.size)

            
            # Escalar la imagen al tamaño del pez
            

            # Dibujar la imagen del pez en lugar del rectángulo
            painter.drawImage(car.x, car.y, car_image)