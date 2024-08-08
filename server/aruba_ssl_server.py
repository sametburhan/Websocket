import asyncio
import websockets
import ssl
import json

async def handle_client(websocket, path):
    data = {
        "message": "Merhaba, güvenli istemci!",
        "status": "connected"
    }
    await websocket.send(json.dumps(data))
    print("Connected")

async def main():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    async with websockets.serve(handle_client, "198.211.98.57", 7443, s>        await asyncio.Future()  # sonsuz döngüde çalıştır

if __name__ == "__main__":
    asyncio.run(main())
