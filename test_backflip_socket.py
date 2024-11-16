import socket 
import time 

# TelloドローンのIPアドレスとポートを定義
TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
TELLO_ADDRESS = (TELLO_IP, TELLO_PORT)

# IPv4でUDPソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ソケットをローカルポートにバインド
sock.bind(('', 9000))

###　↓もっとも原始的なコード ###
# SDKモードに入るコマンド'command'をバイナリに変換して送信
sock.sendto('command'.encode('utf-8'), TELLO_ADDRESS)
time.sleep(1)  

### もっとシンプルにするために関数を作る ###
def send_command(command):
    # コマンドをバイナリ形式に変換して、Telloドローンに送信
    sock.sendto(command.encode('utf-8'), TELLO_ADDRESS)

# 関数を使って'takeoff'コマンドを送信
send_command('takeoff')
time.sleep(4)  # 2秒待機

# 関数を使って'flip b'コマンドを送信
send_command('flip b')
time.sleep(4)  # 3秒待機

# 関数を使って'land'コマンドを送信
send_command('land')
time.sleep(2)  # 2秒待機

# ソケットを閉じる
sock.close()
