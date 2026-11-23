import telnetlib3
import asyncio


async def connect():
    host = "192.168.198.131" # PNET Lab IP Address
    port = 30001

    try:
        reader, writer = await telnetlib3.open_connection(
            host=host,
            port=port
        )

        response = await asyncio.wait_for(
            reader.read(4096),
            timeout=5
        )

        if not response:
            raise ConnectionError("Connection did not respond")

        print(response)

        writer.write("enable\n")
        await writer.drain()
        response = await asyncio.wait_for(
            reader.read(1024),
            timeout=5
        )
        print(response)

        writer.close()

    except asyncio.TimeoutError as e:
        print("Connection Timed out:", e)
    except ConnectionError as e:
        print("ConnectionError:", e)
    except OSError as e:
        print("Network error failure:", e)

asyncio.run(connect())