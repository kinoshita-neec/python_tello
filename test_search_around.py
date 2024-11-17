# test_search_around.py
from djitellopy import Tello
import time

tello = Tello()
tello.connect()

tello.takeoff()

# 120 cmに達するまで上昇
while tello.get_height() < 140:
    tello.send_rc_control(0, 0, 20, 0)
    time.sleep(0.2)

# ホバリング
tello.send_rc_control(0, 0, 0, 0)
time.sleep(1)

# 360度回転
tello.rotate_clockwise(360)

# 着陸
tello.land()

# 接続終了
tello.end()

