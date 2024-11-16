# test_take_picture.py
import cv2

# カメラキャプチャオブジェクトを作成（0：デフォルトカメラ）
cap = cv2.VideoCapture(0)

# 無限ループでフレームを読み取る
while True:
    # フレームをキャプチャ
    ret, frame = cap.read()

    # フレームのキャプチャに失敗した場合、ループを終了
    if not ret:
        break

    # フレームをウィンドウに表示
    cv2.imshow('Camera', frame)

    # キー入力を待つ
    key = cv2.waitKey(1) & 0xFF

    # 'p'キーが押された場合、フレームを保存
    if key == ord('p'):
        cv2.imwrite('captured_frame.png', frame)
        print("フレームを保存しました: captured_frame.png")

    # 'q'キーが押された場合、ループを終了
    elif key == ord('q'):
        break

# キャプチャオブジェクトとウィンドウを解放
cap.release()
cv2.destroyAllWindows()