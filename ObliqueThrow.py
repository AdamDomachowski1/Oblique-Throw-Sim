# Creating Space for program, basics parameters etc.
from time import sleep
import turtle


# Najpierw zapisujemy tylko Y za X odpowiednie beda inne funckje finalnie wszystko sklejamy w jedno

# Class
class object:
    listY = []
    def __init__(self,velocity,acceleration,timeofengine,corx,cory):
        self.velocity = velocity
        self.acceleration = acceleration
        self.timeofengine = timeofengine
        self.corx = corx
        self.cory = cory

    # Engine Force 
    def thrust(self):
        time = 0
        while time < self.timeofengine:
            time += 0.1
            Y = self.cory + self.velocity*time + 0.5*self.acceleration*time**2
            self.listY.append(Y)

    # Freefall
    def freefall(self):
        time = 0
        cory2 = self.cory + self.velocity*self.timeofengine + 0.5*self.acceleration*self.timeofengine**2
        velocity2 = self.velocity + self.acceleration*self.timeofengine
        Y = cory2
        while Y > self.cory: #while rocket hits the ground
            time += 0.1
            Y = cory2 + velocity2*time + 0.5*(-9.81)*time**2
            self.listY.append(Y)
     
    # Printing Coordinates to Terminal
    def printcoordinates(self):
        i = 0
        while i < len(self.listY):
            print(round(self.listY[i],2))
            i += 1

    # Simulation based on list datas
    def simulate(self):
        # Creating Scene
        wn = turtle.Screen()
        wn.title("Simulation by Adam")
        wn.bgcolor("white")
        wn.setup(width=800, height=800)
        wn.tracer(0)

        # Point
        point = turtle.Turtle()
        point.speed(0)
        point.shape("circle")
        point.color("black")
        point.shapesize(stretch_wid=1, stretch_len=1)
        point.penup()
        point.goto(self.corx,self.cory)

        # Simulation Process
        i = 0
        while i < len(self.listY):
            wn.update()
            point.sety(self.listY[i])
            i += 1
            sleep(0.01)



# Main
rocket = object(0,10,8,0,-300)
rocket.thrust()
rocket.freefall()
#rocket.printcoordinates()
rocket.simulate()


