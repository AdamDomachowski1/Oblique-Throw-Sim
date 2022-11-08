# Creating Space for program, basics parameters etc.
from cmath import pi
from datetime import time
from telnetlib import SE
from time import sleep
import turtle
import math

TIMESTEP = 0.05 # Necesary to simulation

# Class
class object:

    list_corx = []
    list_cory = []
    list_velx = []
    list_vely = []
    list_accx = []
    list_accy = []


    def __init__(self,velocity,acceleration,timeofengine,startangle,factor_k):
        self.velocity = velocity
        self.list_velx.append(math.cos(startangle)*velocity)
        self.list_vely.append(math.sin(startangle)*velocity)

        self.acceleration = acceleration
        self.list_accx.append(math.cos(startangle)*acceleration)
        self.list_accy.append(math.sin(startangle)*acceleration) 

        self.timeofengine = timeofengine
        self.startangle = startangle
        self.factor_k = factor_k

        self.corx = 0
        self.list_corx.append(self.corx)

        self.cory = 0
        self.list_cory.append(self.cory)


    # Engine Force 
    def thrust(self):
        time = 0
        while time < self.timeofengine:
            time += TIMESTEP
            actual_x = self.list_corx[len(self.list_corx)-1]
            actual_y = self.list_cory[len(self.list_cory)-1]
            actual_vel_x = self.list_velx[len(self.list_velx)-1]
            actual_vel_y = self.list_vely[len(self.list_vely)-1]
            actual_acc_x = self.list_accx[0] - (0.5*actual_vel_x**2*self.factor_k)
            actual_acc_y = self.list_accy[0] - (0.5*actual_vel_y**2*self.factor_k)
            x = actual_x + actual_vel_x*1 + 0.5*actual_acc_x*1**2
            y = actual_y + actual_vel_y*1 + 0.5*actual_acc_y*1**2
            vel_x = actual_vel_x + actual_acc_x
            vel_y = actual_vel_y + actual_acc_y
            self.list_corx.append(x)
            self.list_cory.append(y)
            self.list_velx.append(vel_x)
            self.list_vely.append(vel_y)
            self.list_accx.append(actual_acc_x)
            self.list_accy.append(actual_acc_y)

    # Freefall
    def freefall(self):
        time = 0
        while self.list_cory[len(self.list_cory)-1] > self.corx: # while point hits the ground
            time += TIMESTEP
            actual_x = self.list_corx[len(self.list_corx)-1]
            actual_y = self.list_cory[len(self.list_cory)-1]
            actual_vel_x = self.list_velx[len(self.list_velx)-1]
            actual_vel_y = self.list_vely[len(self.list_vely)-1]
            actual_acc_x = 0 - (0.5*actual_vel_x**2*self.factor_k)
            actual_acc_y = -9.81 + (0.5*actual_vel_x**2*self.factor_k) # here plus because the move is in oposite direction
            x = actual_x + actual_vel_x*1 + 0.5*actual_acc_x*1**2
            y = actual_y + actual_vel_y*1 + 0.5*actual_acc_y*1**2
            vel_x = actual_vel_x + actual_acc_x
            vel_y = actual_vel_y + actual_acc_y
            self.list_corx.append(x)
            self.list_cory.append(y)
            self.list_velx.append(vel_x)
            self.list_vely.append(vel_y)
            self.list_accx.append(actual_acc_x)
            self.list_accy.append(actual_acc_y)


    # Printing Coordinates to file
    def save_datas_to_file(self):
        file = open("datas.txt","w")
        file.write("TIME COR_X COR_Y VEL_X VEL_Y ACC_X ACC_Y\n")
        i = 0
        while i < len(self.list_cory):
            file.write( str(i+1) + " " + str(round(self.list_corx[i],4)) + " " + str(round(self.list_cory[i],4)) + " " + str(round(self.list_velx[i],4)) + " " + str(round(self.list_vely[i],4)) + " " + str(round(self.list_accx[i],4)) + " " + str(round(self.list_accy[i],4)) + "\n")
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
rocket = object(0,20,10,pi/2.33,0.0001)
rocket.thrust()
rocket.freefall()
rocket.save_datas_to_file()
rocket.simulate()
sleep(2)


