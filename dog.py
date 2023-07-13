from xgolib import XGO
from time import sleep

# dog = XGO(port='/dev/ttyAMA0', version="xgolite")
dog = XGO('xgomini')
fm = dog.read_firmware()
battery = dog.read_battery()
print(f'firmware version: {fm}')
print(f'battery level {battery}%')

dog.reset()
print("Dog reset")
dog.action(2)
dog.move('x',15)

# sleep(10)
# for x in range (0,180):
#     for y in range (40,150):
#         dog.arm(x,y)
#         # sleep(0.1)
#         print(f'x: {x}, y: {y} ')
# dog.claw(1)
# dog.claw(255)