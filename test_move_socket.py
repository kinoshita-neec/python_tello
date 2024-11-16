import socket
import time

# TelloのIPアドレスとポート番号
TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
TELLO_ADDRESS = (TELLO_IP, TELLO_PORT)

# UDPソケットの作成、ポート9000にバインド
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9000))

# コマンドをバイナリ形式でTelloに送信する関数
def send_command(command):
    sock.sendto(command.encode('utf-8'), TELLO_ADDRESS)
    print(command + ' sent')

# SDKモードを開始
send_command('command')
time.sleep(1)

# 離陸
send_command('takeoff')
time.sleep(5)

# 20cm上昇
send_command('up 20')
time.sleep(4)

# 20cm前進
send_command('forward 20')
time.sleep(4)

# 20cm後退
send_command('back 20')
time.sleep(4)

# 着陸
send_command('land')
time.sleep(2)

# ソケットを閉じる
sock.close()
