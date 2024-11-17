import cv2 

# カメラキャプチャオブジェクトを作成
# （0：デフォルトカメラ）
cap = cv2.VideoCapture(0) 

# 無限ループでフレームを読み取る
while True: 
    # フレームをキャプチャ
    ret, frame = cap.read() 

    # フレームをウィンドウに表示
    cv2.imshow('Camera', frame) 

    # 'q'キーが押されたらループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

# キャプチャオブジェクトを解放
cap.release() 

# すべてのOpenCVウィンドウを閉じる
cv2.destroyAllWindows()
