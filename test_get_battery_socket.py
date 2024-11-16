import socket

TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
TELLO_ADDRESS = (TELLO_IP, TELLO_PORT)
LOCAL_PORT = 9000

def send_command(command):
    # ソケットを作成
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', LOCAL_PORT))
    sock.settimeout(5.0)  # タイムアウトを設定

    try:
        # コマンドを送信
        print(f"Sending command: {command}")
        sock.sendto(command.encode('utf-8'), TELLO_ADDRESS)
        
        # ドローンからの応答を受信
        response, _ = sock.recvfrom(1024)
        
        # 応答が空でない場合にのみ戻り値として返す
        if response:
            print(f"Received response: {response.decode('utf-8')}")
            return response.decode('utf-8')
    except socket.timeout:
        print(f"コマンド '{command}' に対する応答がありませんでした。")
        return None
    finally:
        # ソケットを閉じる
        sock.close()

# Telloをコマンドモードにする
if send_command('command') is None:
    print("Telloをコマンドモードにすることができませんでした。")
    exit(1)

# バッテリー残量を取得するコマンドを送信
battery_level = send_command('battery?')
if battery_level is None:
    print("バッテリー残量を取得することができませんでした。")
else:
    # バッテリー残量を表示
    print(f"バッテリー残量: {battery_level}%")