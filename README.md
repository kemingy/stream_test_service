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

- Proxy

```bash
cd proxy && go run main.go
# HTTP
http :8080
# SSE
http :8080/event
# websocket
websocat ws://127.0.0.1:8080/websocket/233
```
