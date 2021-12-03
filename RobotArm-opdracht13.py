from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
Doorgaan = True
Bewegen = 2

while Doorgaan == True:
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        Doorgaan = False
    for i in range (1, Bewegen):
        robotArm.moveRight()
    robotArm.drop()
    for i in range (1, Bewegen):
        robotArm.moveLeft()
    Bewegen += 1
    


    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
