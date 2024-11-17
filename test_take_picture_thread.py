import cv2
import threading
import time

# フレームを保存するためのグローバル変数
saved_frame = None
frame_lock = threading.Lock()

def capture_frames():
    global saved_frame
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # フレームをウィンドウに表示
        cv2.imshow('Camera', frame)

        # フレームを保存
        with frame_lock:
            saved_frame = frame.copy()

        # 'q'キーが押されたらループを終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def display_saved_frame():
    global saved_frame

    while True:
        with frame_lock:
            if saved_frame is not None:
                # 保存されたフレームを表示
                cv2.imshow('Saved Frame', saved_frame)

        # 'q'キーが押されたらループを終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)  # 少し待機してCPU使用率を下げる

    cv2.destroyAllWindows()

# スレッドを作成
capture_thread = threading.Thread(target=capture_frames)
display_thread = threading.Thread(target=display_saved_frame)

# スレッドを開始
capture_thread.start()
display_thread.start()

# スレッドの終了を待つ
capture_thread.join()
display_thread.join()