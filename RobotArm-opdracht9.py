# Robotarm bibliotheek inladen
from RobotArm import RobotArm
            
# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 9')
            
# Jouw python instructies zet je vanaf hier:
for i in range (1,5):
    for i in range (1,5):
        robotArm.grab()
        for i in range (1,6):
            robotArm.moveRight()
        robotArm.drop()
        for x in range (1,5):
            robotArm.moveLeft()
    for m in range (1,5):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
