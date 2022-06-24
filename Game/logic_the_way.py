import pygame
import random

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Logic The Way")

gates = []


class Gate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 20
        self.inputs = {}
        self.linked = {}
        self.back_linked = {"a": None, "b": None}
        self.available = {"a", "b"}

    def change(self, changes):
        """change the input data to self.inputs"""
        for inp in self.inputs.keys():
            self.inputs[inp] = changes.get(inp, self.inputs.get(inp))

        self.change_linked()

    def change_linked(self):
        """send message to other links"""
        for link in self.linked.keys():
            link.change({self.linked.get(link): self.output()})

    def connect(self, link):
        port = link.available_input()
        if port and (not self.check_recursion(link)):
            self.linked.update({link: port})

            """setup back linking to prevent recursion"""
            link.back_linked[port] = self

            """make changes"""
            link.change({self.linked.get(link): self.output()})

    def disconnect(self, link):
        port = self.linked.get(link, None)
        self.linked.pop(link)

        """reset back tracing to prevent recursion"""
        link.back_linked[port] = None

        """reset linked data"""
        link.set_available(port)
        link.change({port: False})

    def available_input(self):
        if len(self.available) > 0:
            port = sorted(self.available)[0]
            self.available.remove(port)
            return port

        return False

    def set_available(self, port):
        self.available.add(port)
        self.inputs.update({port: False})

    def check_recursion(self, target):
        before = [self]

        while True:
            if len(before) > 0:
                element = before[0]
                before.pop(0)
                if element != target:
                    for v in element.back_linked.values():
                        if v:
                            before.append(v)
                else:
                    return True
            else:
                return False

    def GetData(self):
        return self.x, self.y, self.width, self.height

    def check_select(self, x, y):
        return self.collide(x, y, 1, 1)

    def collide(self, x, y, width, height):
        top_a = self.y
        bottom_a = self.y + self.height
        left_a = self.x
        right_a = self.x + self.width

        top_b = y
        bottom_b = y + height
        left_b = x
        right_b = x + width

        col_width = False
        col_height = False

        if (top_a <= top_b) and (top_b < bottom_a):
            col_height = True
        elif (top_a < bottom_b) and (bottom_b < bottom_a):
            col_height = True

        elif (top_b <= top_a) and (top_a < bottom_b):
            col_height = True
        elif (top_b < bottom_a) and (bottom_a < bottom_b):
            col_height = True

        elif (top_b <= top_a) and (bottom_a < bottom_b):
            col_height = True

        if (left_a <= left_b) and (left_b < right_a):
            col_width = True
        elif (left_a < right_b) and (right_b < right_a):
            col_width = True

        elif (left_b <= left_a) and (left_a < right_b):
            col_width = True
        elif (left_b < right_a) and (right_a < right_b):
            col_width = True

        elif (left_b <= left_a) and (right_a < right_b):
            col_width = True

        if col_width and col_height:
            return True
        else:
            return False

    def output(self):
        return True

    def draw(self):
        if self.output() is True:
            pygame.draw.rect(win, (0, 255, 0), self.GetData())
        else:
            pygame.draw.rect(win, (255, 255, 0), self.GetData())


class NotGate(Gate):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.inputs = {"a": False}
        self.available = {"a"}

    def output(self):
        return not self.inputs.get("a", False)


class OrGate(Gate):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.inputs = {"a": False,
                       "b": False}

    def output(self):
        return self.inputs.get("a", False) or self.inputs.get("b", False)


class AndGate(Gate):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.inputs = {"a": False,
                       "b": False}

    def output(self):
        return self.inputs.get("a", False) and self.inputs.get("b", False)


class StartGate(Gate):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.available = {}
        self.outputs = [True, False]
        self.index = 0

        self.width = 30
        self.height = 30

    def add_index(self):
        self.index += 1
        while len(self.outputs)-1 < self.index:
            self.index -= len(self.outputs)

    def remove_index(self):
        self.index -= 1
        while self.index < 0:
            self.index += len(self.outputs)

    def set_index(self, index):
        self.index = index

    def output(self):
        return self.outputs[self.index]


s = StartGate(10, 300)
gates.append(s)

ora = OrGate(10, 10)
gates.append(ora)

orb = AndGate(80, 80)
gates.append(orb)

orc = OrGate(190, 80)
gates.append(orc)

ord = OrGate(10, 180)
gates.append(ord)

ora.connect(orb)
orb.connect(orc)
ord.connect(orb)

ora.change({"a": True})

print(ora.linked)
print(ord.linked)

selected = "or"
selected_gate = None

while True:
    pygame.time.delay(50)

    for event in pygame.event.get():
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_n]:
            selected = "not"
        elif keys_pressed[pygame.K_o]:
            selected = "or"
        elif keys_pressed[pygame.K_a]:
            selected = "and"
        elif keys_pressed[pygame.K_LEFT]:
            s.remove_index()
            s.change_linked()
        elif keys_pressed[pygame.K_RIGHT]:
            s.add_index()
            s.change_linked()

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if selected:
                if selected == "not":
                    gates.append(NotGate(x - 25, y - 10))
                    selected = None
                elif selected == "or":
                    gates.append(OrGate(x - 25, y - 10))
                    selected = None
                elif selected == "and":
                    gates.append(AndGate(x - 25, y - 10))
                    selected = None
                elif selected == "gate":
                    end_gate = None

                    for g in gates:
                        if g.check_select(x, y):
                            end_gate = g

                    if end_gate:
                        selected_gate.connect(end_gate)

                        selected = None
                        selected_gate = None

            else:
                for g in gates:
                    if g.check_select(x, y):
                        selected = "gate"
                        selected_gate = g

    """draw all the gates"""
    for g in gates:
        g.draw()

    """draw all the gates"""
    for g in gates:
        for link in g.linked:
            pygame.draw.line(win, (255, 0, 0), (g.x + g.width, g.y + g.height/2), (link.x, link.y + 10), 5)

    pygame.display.update()
