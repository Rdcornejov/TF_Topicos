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

class MyTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super(MyTimedBehaviour, self).__init__(agent, time)
        self.agent = agent

    def on_time(self):
        super(MyTimedBehaviour, self).on_time()
        gui.update()

class ControlAgent(Agent):
    delay = .2
    def __init__(self, aid):
        super(ControlAgent, self).__init__(aid=aid, debug=False)
        mytimed = MyTimedBehaviour(self, self.delay)
        self.behaviours.append(mytimed)

    def react(self, message):
        super(ControlAgent, self).react(message)
        display_message(self.aid.localname,f"{message.sender.name}: {message.content}")

def agentsexec():
    start_loop(agents)

if __name__ == '__main__':
    agents = []
    cars = []
    num_cars = 5
    port = int(sys.argv[1])
    control_agent_name = 'control_agent_{}@localhost:{}'.format(port, port)
    control_agent = ControlAgent(AID(name=control_agent_name))
    c = 0
    for i in range(num_cars):
        c += 10
        car_agent_name = 'car_agent_{}@localhost:{}'.format(port + c, port + c)
        car_agent = CarAgent(AID(name=car_agent_name),control_agent_name, .2)
        cars.append(car_agent)

    agents.append(control_agent)
    agents += cars
    x = threading.Thread(target=agentsexec)
    x.start()
    app = QApplication([])
    gui = Gui(cars)
    gui.show()
    app.exec()
    x.join()