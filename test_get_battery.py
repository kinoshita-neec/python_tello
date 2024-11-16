from djitellopy import Tello

tello = Tello()
tello.connect()

# バッテリー残量を取得
battery_level = tello.get_battery()

# バッテリー残量を表示
print(f"バッテリー残量: {battery_level}%")

# ドローンから切断
tello.end()


