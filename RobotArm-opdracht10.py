# Robotarm bibliotheek inladen
from RobotArm import RobotArm
            
# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 10')
            
# Jouw python instructies zet je vanaf hier:
for i in range(1,6):
    robotArm.grab()
    for i in range (10,1,-2):
        robotArm.moveRight()
    robotArm.drop()
    for i in range (9,1,-2):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
