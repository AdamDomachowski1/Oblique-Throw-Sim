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
    def __init__(self,velocity,acceleration,timeofengine,startangle):
        self.velocity = velocity
        self.acceleration = acceleration
        self.timeofengine = timeofengine
        self.startangle = startangle
        self.corx = 0
        self.cory = 0

    # Engine Force 
    def thrust(self):
        time = 0
        while time < self.timeofengine:
            time += 0.1
            X = self.corx + math.cos(self.startangle)*(self.velocity*time + 0.5*self.acceleration*time**2)
            Y = self.cory + math.sin(self.startangle)*(self.velocity*time + 0.5*self.acceleration*time**2)
            self.listX.append(X)
            self.listY.append(Y)
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

        # Depending On X and Y sizes program will adjust visual simulation to fit trajectory in window
        if len(self.listX)>0:
            scale_x = 400/max(self.listX)
        else:
            scale_x = 0

        if len(self.listY)>0:
            scale_y = 400/max(self.listY)
        else:
            scale_y = 0

        # It is important to have one scale for both moves to see how it would look like in reality (1m | = 1m __ )
        if scale_x > scale_y:
            scale = scale_y
        else:
            scale = scale_x

        # Creating Scene
        wn = turtle.Screen()
        wn.title("Simulation by Adam")
        wn.bgcolor("white")
        wn.setup(width=800, height=800)
        wn.tracer(0)

        # Surface (define as X = -300)
        surface_line = turtle.Turtle()
        surface_line.speed(0)
        surface_line.shape("square")
        surface_line.color("black")
        surface_line.shapesize(stretch_wid=5, stretch_len=50)
        surface_line.penup()
        surface_line.goto(0,-350)

        # Point
        point = turtle.Turtle()
        point.speed(0)
        point.shape("circle")
        point.color("red")
        point.shapesize(stretch_wid=0.1, stretch_len=0.1)
        point.penup()
        point.goto(self.corx,self.cory)

        #Pixel - used for draw trajectory


        # Simulation Process
        i = 0
        while i < len(self.listX):
            point.color("red")
            point.shapesize(stretch_wid=0.5, stretch_len=0.5)
            wn.update()
            point.setx((self.listX[i])*scale - 300)
            point.sety((self.listY[i])*scale - 300)
            point.shapesize(stretch_wid=0.1, stretch_len=0.1)
            point.color("blue")
            point.stamp()
            
            #print((str)((self.listX[i])*scale - 300) + " " + (str)((self.listY[i])*scale - 300))
            i += 1
            sleep(0.001)



# Main
rocket = object(0,10,20,pi/4)
rocket.thrust()
rocket.freefall()
rocket.savecoordinates()
rocket.simulate()
sleep(2)


