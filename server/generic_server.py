import asyncio
import websockets

async def echo(websocket, path):
        async for message in websocket:
                print(f"Mesaj alındı: {message}")
                await websocket.send(f"Geri gönderilen: {message}")
start_server = websockets.serve(echo, "198.211.98.57",8000)

asyncio.get_event_loop().run_until_complete(start_server)
print("Websocket sunucusu başlatıldı..")
asyncio.get_event_loop().run_forever()



