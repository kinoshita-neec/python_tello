from djitellopy import Tello 
import time 

#! Telloドローンのインスタンスを作成
tello = Tello() 

#! ドローンに接続
tello.connect() 

#! 離陸
tello.takeoff() 

#! 2秒間待機
time.sleep(2) 

#!pip 後方にフリップ
tello.flip_back() 

# 2秒間待機
time.sleep(2) 

# 着陸
tello.land()

