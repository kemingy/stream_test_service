import random

from falcon.asgi import App, Request, Response, WebSocket
from falcon import WebSocketDisconnected


RANDOM_BYTES = f"{random.randrange(2**32):x}"


class Stream:
    async def on_get(self, req: Request, resp: Response, account_id: str):
        resp.content_type = "text/plain"
        resp.text = RANDOM_BYTES
        print(account_id, RANDOM_BYTES)

    async def on_websocket(self, req: Request, ws: WebSocket, account_id: str):
        print(req)
        await ws.accept()
        while True:
            try:
                payload = await ws.receive_text()
                payload = payload.strip()
                print(f"receive '{payload}' from {account_id}")
                await ws.send_text(f"Hello, {payload}!")
            except WebSocketDisconnected:
                print(f"{account_id} disconnected")
                break


app = App()
app.add_route("/{account_id}/message", Stream())
