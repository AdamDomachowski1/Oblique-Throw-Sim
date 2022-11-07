# Creating Space for program, basics parameters etc.
from cmath import pi
from datetime import time
from time import sleep
import turtle
import math

TIMESTEP = 0.5 # Necesary to simulation

# Class
class object:

    list_corx = []
    list_cory = []
    list_velx = []
    list_vely = []

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
            time += TIMESTEP
            S = (self.velocity*time + 0.5*self.acceleration*time**2)
            V = (self.velocity +self.acceleration*time)
            x = self.corx + math.cos(self.startangle)*S
            y = self.cory + math.sin(self.startangle)*S
            VEL_X = math.cos(self.startangle)*V
            VEL_Y = math.sin(self.startangle)*V
            self.list_corx.append(x)
            self.list_cory.append(y)
            self.list_velx.append(VEL_X)
            self.list_vely.append(VEL_Y)



    # Freefall
    def freefall(self):
        time = 0
        S = self.velocity*self.timeofengine + 0.5*self.acceleration*self.timeofengine**2 # distance so far
        V = self.velocity + self.acceleration*self.timeofengine # velocity reach while engine of
        corx2 = self.corx + math.cos(self.startangle)*S # calculating coordinates where engine off
        cory2 = self.cory + math.sin(self.startangle)*S 
        x = corx2   # set this coordinates as a new start point (from here we uses other formula)
        y = cory2
        while y > self.cory: #while rocket hits the ground
            time += TIMESTEP      
            x = corx2 + (math.cos(self.startangle)*V*time) 
            y = cory2 + (math.sin(self.startangle)*V*time + 0.5*(-9.81)*time**2)
            VEL_X = math.cos(self.startangle)*V
            VEL_Y = math.sin(self.startangle)*V + (-9.81)*time
            self.list_corx.append(x)
            self.list_cory.append(y)
            self.list_velx.append(VEL_X)
            self.list_vely.append(VEL_Y)   

    # Printing Coordinates to file
    def save_datas_to_file(self):
        file = open("datas.txt","w")
        file.write("TIME COR_X COR_Y VEL_X VEL_Y ACCELERATION\n")
        i = 0
        while i < len(self.list_cory):
            file.write( str(i+1) + " " + str(round(self.list_corx[i],4)) + " " + str(round(self.list_cory[i],4)) + " " + str(round(self.list_velx[i],4)) + " " + str(round(self.list_vely[i],4)) + "\n")
            i += 1
        file.close()

    # Simulation based on list datas
    def simulate(self):

        # Depending On X and Y sizes program will adjust visual simulation to fit trajectory in window
        if len(self.list_corx)>0:
            scale_x = 400/max(self.list_corx)
        else:
            scale_x = 0

        if len(self.list_cory)>0:
            scale_y = 400/max(self.list_cory)
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

        # Surface
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


        # Simulation Process
        i = 0
        while i < len(self.list_corx):
            point.color("red")
            point.shapesize(stretch_wid=0.5, stretch_len=0.5)
            wn.update()
            point.setx((self.list_corx[i])*scale - 300)
            point.sety((self.list_cory[i])*scale - 300)
            point.shapesize(stretch_wid=0.1, stretch_len=0.1)
            point.color("blue")
            point.stamp()
            
            #print((str)((self.list_corx[i])*scale - 300) + " " + (str)((self.list_cory[i])*scale - 300))
            i += 1
            sleep(0.001)


# Main
rocket = object(0,9.81,100,pi/2.33)
rocket.thrust()
rocket.freefall()
rocket.save_datas_to_file()
rocket.simulate()
sleep(2)


