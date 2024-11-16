# test_socket
import socket

# サーバーのIPアドレスとポートを設定
HOST = 'localhost'
PORT = 000000  # ポート番号は相手と合わせる

# IPv4でTCPソケットを作成
test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
test_socket.connect((HOST, PORT))  # サーバーに接続

test_socket.sendall(b'こんにちは、サーバー！')  # メッセージを送信

print(f"メッセージを送信しました: こんにちは、サーバー！")        

test_socket.close()  # ソケットを閉じる

