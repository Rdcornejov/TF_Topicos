import random
from pade.misc.utility import display_message, start_loop
from pade.acl.messages import ACLMessage
from pade.core.agent import Agent
from pade.behaviours.protocols import TimedBehaviour
from pade.acl.aid import AID


class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, other, time):
        super(ComportTemporal, self).__init__(agent, time)
        self.agent = agent
        self.other = other

    def on_time(self):
        super(ComportTemporal, self).on_time()
        self.agent.updateStatus()
        self.agent.move()
        #.......................
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(AID(self.other))
        message.set_content(f"{self.agent.id} {self.agent.x} {self.agent.y} {self.agent.size} {self.agent.status} {self.agent.start_colision}")
        self.agent.send(message)

class CarAgent(Agent):

    def __init__(self, aid, id, receiver, delay):
        super(CarAgent, self).__init__(aid=aid, debug=False)
        comp_temp = ComportTemporal(self,receiver, delay)
        self.id = id
        self.behaviours.append(comp_temp)
        self.status = 2
        self.size = random.randint(10, 20)
        self.x1_limit = random.randint(30, 125 - self.size * 2)
        self.x2_limit = random.randint(514, 609 - self.size * 2)
        self.y1_limit = random.randint(30, 125 - self.size)
        self.y2_limit = random.randint(514, 609 - self.size)
        self.x = random.randint(30, 125 - self.size * 2)
        self.y = random.randint(30, 125 - self.size * 2)
        self.speed = 10 * 15 / self.size
        self.colisionado = False
        self.start_colision = 0

    def updateStatus(self):
        if self.y <= self.y1_limit:
            self.status = 1
            if self.x >= self.x2_limit:
                self.status = 4
        elif self.y >= self.y2_limit:
            self.status = 2
            if self.x <= self.x1_limit:
                self.status = 3
        else:
            if self.x <= self.x1_limit:
                self.status = 3
            elif self.x >= self.x2_limit:
                self.status = 4
                
    def move(self):
        if self.status == 1: self.x += self.speed   #Que se vaya a la derecha
        elif self.status == 2: self.x -= self.speed #Que se vaya  la izquierda
        elif self.status == 3: self.y -= self.speed #Que se vaya para arriba
        elif self.status == 4: 
            self.y += self.speed #Que se vaya para abajo
            self.start_colision = 1