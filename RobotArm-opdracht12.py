# Robotarm bibliotheek inladen
from RobotArm import RobotArm
            
# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 12')
            
# Jouw python instructies zet je vanaf hier:
Distance = 8

for i in range (1,10):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for i in range(1, Distance):
            robotArm.moveRight()
        robotArm.drop()
        for i in range (1,Distance):
            robotArm.moveLeft()
    robotArm.drop()
    
    Distance -= 1
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
