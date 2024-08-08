import asyncio
import websockets

async def connect_to_server():
    uri = "wss://198.211.98.57:7443"
    async with websockets.connect(uri) as websocket:
        response = await websocket.recv()
        print(f"Sunucudan gelen mesaj: {response}")

if __name__ == "__main__":
    asyncio.run(connect_to_server())
