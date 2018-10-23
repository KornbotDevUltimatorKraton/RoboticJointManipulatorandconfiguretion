#Author: Mr.Chanapai Chuadchum 
#Project name : Machine Learning Robotic arm with the smart drive 
#Date: 6/10/2018 
import pybrain # pybrain for neural network and machine learning 
import scipy  # machinelearning 
import math   # Math function 
import matplotlib.pyplot as plt # matplot function # plotting the function of the speed and angle 
import numpy   # math matrix function and more on the 
import cv2   # Computer vision system function  
import serial # serial communication system for the controller
import pyttsx #Speech synthesis for the robotic arm to talking with the user  
import sklearn # machine learning fully option 
import time # The time for the angular velocity  
# Serial communication initialization 
  #Status reporter
try: 
   #Base robotic joint rotation  serial communication 
   Base  = serial.Serial("/dev/ttyUSB0",115200)  
   print('Base smart joint connect ....... [OK]') # in the case of the joint connected 
except: 
   print('Base robotic joint lost connection please reconnect') # Robotic joint display function 
try:
  #Shoulder robotic joint rotation serial communication 
   Shoulder = serial.Serial("/dev/ttyUSB1",115200) 
   print('Shoulder smart joint connect ....... [OK]') # in the case of the joint connected 
except: 
   print('Shoulder robotic joint lost connection please reconnection') # Robotic joint display function 
try:
   #Elbow robotic joint rotation serial communication 
   Elbow = serial.Serial("/dev/ttyUSB2",115200) 
   print('Elbow smart joint connect ....... [OK]') # in the case of the joint connected 
except: 
   print('Elbow robotic joint lost connection please reconnection') # Roboticjoint display function 
try:
  #Wrist robotic joint rotation serial communication 
  Wrist = serial.Serial("/dev/ttyUSB3",115200)
  print('Wrist smart joint connect ....... [OK]') # in the case of the joint connected 
except: 
  print('Wrist robotic joint lost connection please reconnection ')# Robotic joint display function
try:  
        #Wristrotation joint serial communication 
  Wristrotation = serial.Serial("/dev/ttyUSB4",115200)  
  print(' Wrist rotation smart joint connect ....... [OK]') # in the case of the joint connected 
except: 
        print('Wrist rotation joint lost connection please reconnection') # Robotic joint display function 
try: 
   #Hand rotation joint serial communication 
   Handrotation = serial.Serial("/dev/ttyUSB5",115200) 
   print('Hand rotation  smart joint connect ....... [OK]') # in the case of the joint connected 
except: 
   print('Hand rotation joint lost connection please reconnection ')# Robotic joint display function 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
#Smart drive function for the 
def BaseRoboticjoint(BaseAngle): #Base function for the rotation 
    Base.write(BaseAngle)  # input base write angle to the mcu core 
def ShoulderRoboticjoint(ShoulderAngle): #Shoulder angle for the rotation 
    Shoulder.write(ShoulderAngle)
def ElbowRoboticjoint(ElbowAngle): #Elbow angle for rotation 
    Elbow.write(ElbowAngle)
def WristRoboticjoint(WristAngle): #Wrist angle for rotation 
    Wrist.write(WristAngle)
def WristrotationRoboticjoint(WristrotateAngle): #Wristrotate angle for rotation  
     Wristrotation.write(WristrotateAngle) 
def HandrotationRoboticJoint(HandrotationAngle): #Hand rotation  
     Handrotation.write(HandrotationAngle)  
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>         
while True:  # function for the loop control application function control 
     print('<< Robotic arm modular smart joint operating >>.......')
     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     print('Base data communication status') # Base data status 
     try:  # Try to commuicate and connect with the base smart joint 
       basesplit = Base.readline() # Read the data from the serial communication 
       basesplit.split(",") # Base splitter function 
       Basedata = basesplit.split(",") # Base data splitter 
       Theta1   = Basedata[0]  # Base control Angle 
       time1    = Basedata[1]  # Base time micro controller 
       print('Base Angle :'+ Theta1) # Theta1 angle output 
       print('Base timing :'+ time1) # Time1 output  Print out the angle and time to processing 
     except: 
       print('Checking Base serial communication function')
     print('Shoulder data communication status') # Base data status 
     try:  # Try to commuicate and connect with the Shoulder smart joint 
       Shouldersplit = Shoulder.readline() # Read the data from the serial communication 
       Shouldersplit.split(",") # Base splitter function 
       Shoulderdata = Shouldersplit.split(",") # Base data splitter 
       Theta2   = Shoulderdata[0]  # Base control Angle 
       time2    = Shoulderdata[1]  # Base time micro controller 
       print('Shoulder Angle :'+ Theta2) # Theta1 angle output 
       print('Soulder timing :'+ time2) # Time1 output  Print out the angle and time to processing 
     except: 
       print('Checking Shoulder serial communication function')
     print('Elbow data communication status')
     try: # Try to communicate and connect with Elbow joint
       Elbowsplit = Elbow.readline()
       Elbowsplit.split(",")
       Elbowdata = Elbowsplit.split(",") # Base data splitter 
       Theta3   =  Elbowdata[0]  # Base control Angle 
       time3   =   Elbowdata[1]  # Base time micro controller 
       print('Elbow Angle :'+ Theta3) # Theta1 angle output 
       print('Elbow timing :'+ time3) # Time1 output  Print out the angle and time to processing 
     except: 
       print('Checking Elbow serial communication function')
     print('Wrist data communication status')
     try: # Try to communicate and connect with Elbow joint
       Wristsplit = Wrist.readline()
       Wristsplit.split(",")
       Wristdata = Wristsplit.split(",") # Base data splitter 
       Theta4   =  Wristdata[0]  # Base control Angle 
       time4   =   Wristdata[1]  # Base time micro controller 
       print('Wrist Angle :'+ Theta4) # Theta1 angle output 
       print('Wrist timing :'+ time4) # Time1 output  Print out the angle and time to processing 
     except: 
       print('Checking Wrist serial communication function')
     print('Wrist rotate data communication status')
     try: # Try to communicate and connect with Elbow joint
       Wristrotatesplit = Wristrotation.readline()
       Wristrotatesplit.split(",")
       Wristrotatedata = Wristrotatesplit.split(",") # Base data splitter 
       Theta5  =   Wristrotatedata[0]  # Base control Angle 
       time5   =   Wristrotatedata[1]  # Base time micro controller 
       print('Wrist rotate Angle :'+ Theta5) # Theta1 angle output 
       print('Wrist rotate timing :'+ time5) # Time1 output  Print out the angle and time to processing 
     except: 
       print('Checking Wrist rotate serial communication function')
     print('Handrotate  data communication status')
     try: # Try to communicate and connect with Elbow joint
       Handsplit = Handrotation.readline()
       Handsplit.split(",")
       Handdata = Handsplit.split(",") # Base data splitter 
       Theta6   =  Handdata[0]  # Base control Angle 
       time6   =   Handdata[1]  # Base time micro controller 
       print('Hand rotation Angle :'+ Theta6) # Theta1 angle output 
       print('Hand rotation timing :'+ time6) # Time1 output  Print out the angle and time to processing 
     except: 
       print('Checking Hand rotation serial communication function')
     