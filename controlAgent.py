import sys
import threading
import time
from PySide6.QtWidgets import QApplication
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from pade.misc.utility import display_message,start_loop
from carAgent import CarAgent
from pade.core.agent import Agent

from gui import Gui

class car:
    def __init__(self, id, x, y, size, status):
        self.id = id
        self.x = x
        self.y = y
        self.size = size
        self.status = status
        self.colisionado = False
        self.start_colision = 0

class MyTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super(MyTimedBehaviour, self).__init__(agent, time)
        self.agent = agent

    def on_time(self):
        super(MyTimedBehaviour, self).on_time()
        if self.agent.cont >= self.agent.n:
            gui.update()
            self.agent.cont = 0
        else:
            print(self.agent.cont,"  no entra")

class ControlAgent(Agent):
    delay = .2
    cont = 0
    cars = []
    def __init__(self, aid, n):
        super(ControlAgent, self).__init__(aid=aid, debug=False)
        mytimed = MyTimedBehaviour(self, self.delay)
        self.behaviours.append(mytimed)
        self.n = n
        for i in range(n):
            self.cars.append(car(i,0,0,0,2))

    def react(self, message):
        super(ControlAgent, self).react(message)
        palabra = str(message.content)
        mensaje = palabra.split()
        print(mensaje, len(mensaje))
        if len(mensaje) == 6:
            carro_encontrado = next(filter(lambda x: x.id == int(mensaje[0]), self.cars), None)
            carro_encontrado.x =float(mensaje[1])
            carro_encontrado.y = float(mensaje[2])
            carro_encontrado.size = int(mensaje[3])
            carro_encontrado.status= int(mensaje[4])
            carro_encontrado.start_colision = int(mensaje[5])
            display_message(self.aid.localname,f"{message.sender.name}: {palabra} Car:{self.cont} - Cont: {self.cont}")
            self.cont += 1

            for car in self.cars:
                if car != carro_encontrado:
                    distancia = ((car.x - carro_encontrado.x)**2 + (car.y - carro_encontrado.y)**2)**0.5
                    if distancia <= car.size + carro_encontrado.size and car.start_colision == 1 and carro_encontrado.start_colision == 1:
                        car.colisionado = True
                        carro_encontrado.colisionado = True
       
def agentsexec():
    start_loop(agents)

if __name__ == '__main__':
    agents = []
    num_cars = 5
    port = int(sys.argv[1])
    control_agent_name = 'control_agent_{}@localhost:{}'.format(port, port)
    control_agent = ControlAgent(AID(name=control_agent_name),num_cars)
    agents.append(control_agent)
    c = 0
    for i in range(num_cars):
        c += 10
        car_agent_name = 'car_agent_{}@localhost:{}'.format(port + c, port + c)
        car_agent = CarAgent(AID(name=car_agent_name),i, control_agent_name, .2)
        agents.append(car_agent)

    x = threading.Thread(target=agentsexec)
    x.start()
    app = QApplication([])
    gui = Gui(control_agent)
    gui.show()
    app.exec()
    x.join()