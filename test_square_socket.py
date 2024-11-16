import socket
import time

TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
TELLO_ADDRESS = (TELLO_IP, TELLO_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9000))

def send_command(command):
    sock.sendto(command.encode('utf-8'), TELLO_ADDRESS)
    print(command + ' sent')

# commandを送信
send_command('command')
time.sleep(1)

# 離陸
send_command('takeoff')
time.sleep(4)

# 4回のループで前進と回転を繰り返す
for _ in range(4):
    # ドローンを前方に100cm移動
    send_command('forward 100')
    time.sleep(5)
    # ドローンを時計回りに90度回転
    send_command('cw 90')
    time.sleep(5)

# ドローンを着陸
send_command('land')
time.sleep(2)

# ソケットを閉じる
sock.close()
