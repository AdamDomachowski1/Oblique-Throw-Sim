# Creating Space for program, basics parameters etc.
from cmath import pi
from time import sleep
import turtle
import math


# Najpierw zapisujemy tylko Y za X odpowiednie beda inne funckje finalnie wszystko sklejamy w jedno

# Class
class object:
    listX = []
    listY = []
    def __init__(self,velocity,acceleration,timeofengine,startangle,corx,cory):
        self.velocity = velocity
        self.acceleration = acceleration
        self.timeofengine = timeofengine
        self.startangle = startangle
        self.corx = corx
        self.cory = cory

    # Engine Force 
    def thrust(self):
        time = 0
        while time < self.timeofengine:
            time += 0.1
            X = self.corx + math.cos(self.startangle)*(self.velocity*time + 0.5*self.acceleration*time**2)
            Y = self.cory + math.sin(self.startangle)*(self.velocity*time + 0.5*self.acceleration*time**2)
            self.listX.append(X)
            self.listY.append(Y)
            print(X,Y)
        print("engine off")

    # Freefall
    def freefall(self):
        time = 0
        corx2 = self.corx + math.cos(self.startangle)*(self.velocity*self.timeofengine + 0.5*self.acceleration*self.timeofengine**2)
        cory2 = self.cory + math.sin(self.startangle)*(self.velocity*self.timeofengine + 0.5*self.acceleration*self.timeofengine**2)
        velocity2 = self.velocity + self.acceleration*self.timeofengine
        X = corx2
        Y = cory2
        while Y > self.cory: #while rocket hits the ground
            time += 0.1
            X = corx2 + math.cos(self.startangle)*velocity2*time
            Y = cory2 + math.sin(self.startangle)*velocity2*time + 0.5*(-9.81)*time**2
            self.listX.append(X)
            self.listY.append(Y)
            print(X,Y)
     
    # Printing Coordinates to file
    def savecoordinates(self):
        file = open("coordinates.txt","w")

        i = 0
        while i < len(self.listY):
            file.write(str(round(self.listX[i],4)) + " " + str(round(self.listY[i],4)) + "\n")
            i += 1
        file.close()

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
        while i < len(self.listX):
            wn.update()
            point.setx(self.listX[i])
            point.sety(self.listY[i])
            i += 1
            sleep(0.01)



# Main
rocket = object(200,0,200,pi/4,0,0)
rocket.thrust()
rocket.freefall()
rocket.savecoordinates()
#rocket.simulate()


