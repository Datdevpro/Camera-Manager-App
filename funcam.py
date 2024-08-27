import asyncio, base64, cv2, websockets
import numpy as np

async def receive_frame():
    ws_url = 'ws://khus-welcam:1234/video_feed'
    async with websockets.connect(ws_url) as ws:
        while(1):
            encoded_frame = await ws.recv()
            npimg = np.frombuffer(base64.b64decode(encoded_frame), np.uint8)
            img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
            cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
            cv2.imshow('Camera', img)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q') or cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) == 0:
                break

def turn_cam():
    asyncio.run(receive_frame())