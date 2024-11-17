import cv2
import asyncio

# フレームを保存するためのグローバル変数
saved_frame = None
# フレームの読み書きを保護するための非同期ロック
frame_lock = asyncio.Lock()
# フレームが保存されたことを示すフラグ
frame_saved = False

async def capture_frames():
    """
    カメラからフレームをキャプチャし、ウィンドウに表示する。
    キャプチャしたフレームをグローバル変数に保存する。
    """
    global saved_frame, frame_saved
    # デフォルトカメラ（インデックス0）をキャプチャするオブジェクトを作成
    cap = cv2.VideoCapture(0)

    while True:
        # フレームをキャプチャ
        ret, frame = cap.read()
        if not ret:
            # フレームのキャプチャが失敗した場合、ループを終了
            break

        # フレームをウィンドウに表示
        cv2.imshow('Camera', frame)

        # フレームを保存
        async with frame_lock:
            saved_frame = frame.copy()
            frame_saved = True  # フレームが保存されたことを示すフラグをセット

        # 'q'キーが押されたらループを終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # 少し待機して他のタスクに制御を渡す
        await asyncio.sleep(0.01)

    # キャプチャオブジェクトを解放
    cap.release()
    # すべてのOpenCVウィンドウを閉じる
    cv2.destroyAllWindows()

async def display_saved_frame():
    """
    保存されたフレームを別のウィンドウに表示する。
    フレームが保存されたときだけウィンドウを作成して表示する。
    """
    global saved_frame, frame_saved

    while True:
        async with frame_lock:
            if frame_saved:
                # 保存されたフレームを表示
                cv2.imshow('Saved Frame', saved_frame)
                frame_saved = False  # フラグをリセット

        # 'q'キーが押されたらループを終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # 少し待機してCPU使用率を下げる
        await asyncio.sleep(0.1)

    # すべてのOpenCVウィンドウを閉じる
    cv2.destroyAllWindows()

async def main():
    """
    メイン関数。非同期タスクを作成し、実行する。
    """
    # 非同期タスクを作成
    capture_task = asyncio.create_task(capture_frames())
    display_task = asyncio.create_task(display_saved_frame())

    # タスクの終了を待つ
    await capture_task
    await display_task

# メイン関数を実行
asyncio.run(main())