import telnetlib3
import asyncio


async def connect():
    host = "192.168.198.131" # PNET Lab IP Address
    port = 30001

    print("Connecting to Router...")

    await telnetlib3.open_connection(
        host=host,
        port=port
    )

    print("Connection Established")


asyncio.run(connect())