# Robotarm bibliotheek inladen
from RobotArm import RobotArm
            
# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 7')
            
# Jouw python instructies zet je vanaf hier:
for i in range (1,6):
    for i in range (1,7):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    robotArm.moveRight()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
