import telnetlib3
import asyncio


async def connect():
    host = "192.168.198.131" # PNET Lab IP Address
    port = 30001


    reader, writer = await telnetlib3.open_connection(
        host=host,
        port=port
    )

    response = await asyncio.wait_for(
        reader.read(1024000),
        timeout=5
    )
    print(response)




asyncio.run(connect())