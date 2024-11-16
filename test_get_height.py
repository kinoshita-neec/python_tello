# test_get_height.py
from djitellopy import Tello

tello = Tello()
tello.connect()

# 高度を取得
current_height = tello.get_height()

# バッテリー残量を表示
print(f"現在の高度: {current_height}")

# ドローンから切断
tello.end()


