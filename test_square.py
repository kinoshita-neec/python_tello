from djitellopy import Tello 
import time 

tello = Tello() 
tello.connect() 

tello.takeoff() 
time.sleep(1) 

for _ in range(4): 
    # 前に10cm進む
    tello.move_forward(100) 
    time.sleep(1) 
    # 時計回りに90度旋回する
    tello.rotate_clockwise(90) 
    time.sleep(1)
     
tello.land()
