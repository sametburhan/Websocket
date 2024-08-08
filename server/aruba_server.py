import websockets
import json
import asyncio

async def handle_client(websocket,path):
		print("Connected")
		data = {
		 "grant_type": "password",
		 "username": "samet",
		 "password": "test_password",
		 "client_id": "AUEELLJnUkp3YeLF4imUGZWAsEFEgZpT"
		 "scope": "Aruba_IoT_Framework"
        }
        await websocket.send(json.dumps(data))

async def main():
        async with websockets.serve(handle_client,"198.211.98.57", 7443):
                await asyncio.Future()

if __name__ == "__main__":
        asyncio.run(main())

		