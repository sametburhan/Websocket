import asyncio
import websockets
 
async def hello():
    uri = "ws://198.211.98.57:7443"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Merhaba Dünya!")
        response = await websocket.recv()
        print(f"Gelen mesaj: {response}")
 
asyncio.get_event_loop().run_until_complete(hello())