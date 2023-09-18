# stream_test_service

Test SSE and websocket services.

## Usage

- Service

```bash
uvicorn main:app
```

- Client

```bash
# websocket
websocat ws://127.0.0.1:8000/websocket/233
# SSE
http :8000/event
```
