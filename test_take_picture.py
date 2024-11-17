# test_take_picture.py
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
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

# 保存したフレームを表示
captured_frame = cv2.imread('captured_frame.png')
cv2.imshow('Captured Frame', captured_frame)
# 何かキーを押すとウィンドウを閉じる
cv2.waitKey(0)
cv2.destroyAllWindows()
