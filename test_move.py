from djitellopy import Tello 
import time 

tello = Tello() 
tello.connect() 
tello.takeoff()

# ドローンを20cm上昇させる
tello.move_up(20) 
time.sleep(1) 

# ドローンを20cm前進させる
tello.move_forward(20) 
time.sleep(1) 

# ドローンを20cm後退させる
tello.move_back(20) 
time.sleep(1) 

# 着陸
tello.land()

