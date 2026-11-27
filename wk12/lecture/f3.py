
import telnetlib3
import asyncio


async def connect():
    host = "192.168.198.131"  # PNETLab IP Address
    port = 30001
    writer = None

    try:
        reader, writer = await telnetlib3.open_connection(
            host=host,
            port=port,
            encoding="ascii"
        )

        # Wait for boot
        await asyncio.sleep(2)

        # Send ENTER key to get prompt
        writer.write("\r\n")
        await writer.drain()

        response = await asyncio.wait_for(
            reader.readuntil("R1>".encode()),
            timeout=10
        )

        print(response.decode())
        print("#" * 20)

        # Enter privileged EXEC mode
        writer.write("enable\r\n")
        await writer.drain()

        response = await asyncio.wait_for(
            reader.readuntil("#".encode()),
            timeout=10
        )

        print(response.decode())

    except asyncio.TimeoutError as e:
        print("Connection Timed out:", e)

    except ConnectionError as e:
        print("ConnectionError:", e)

    except OSError as e:
        print("Network error failure:", e)

    finally:
        if writer is not None:
            writer.close()
            await writer.wait_closed()


asyncio.run(connect())
