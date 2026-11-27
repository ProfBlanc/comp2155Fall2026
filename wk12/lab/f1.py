
import telnetlib3
import asyncio

async def connect(host, port, prompt):
    writer = None

    reader, writer = await telnetlib3.open_connection(
        host=host,
        port=port
    )

    # Wait for boot
    await asyncio.sleep(2)

    # Send ENTER key to get prompt
    writer.write("\r\n")
    await writer.drain()
    # determine if "username:" exists in responses (text outputted to console)
    # if so, send the username value
    # "username: "
    # 'root\r\n'

    # determine if "password:" exists in responses (text outputted to console)
    # if so, send the password value
    # "password: "
    # 'pnet\r\n'

    if not prompt.endswith(">"):
        prompt += ">"

    response = await asyncio.wait_for(
        reader.readuntil(prompt.encode()),
        timeout=10
    )

    # if no response => timeoutexception occured => text was not found

    return reader, writer, response  # response needs to be decoded

    # # Enter privileged EXEC mode
    # writer.write("enable\r\n")
    # await writer.drain()
    #
    # response = await asyncio.wait_for(
    #     reader.readuntil("#".encode()),
    #     timeout=10
    # )
    #
    # print(response.decode())

    #
    # finally:
async def close_connection(writer):
    if writer is not None:
        writer.close()
        await writer.wait_closed()

async def execute_command(reader, writer, command, prompt="#"):
    if writer is None:
        raise ValueError("Writer is None")

    if not command.endswith("\r\n"):
        command += "\r\n"
    # validate to determine if the command is a string
    # if not, convert to a string
    writer.write(command)
    await writer.drain()

    response = await asyncio.wait_for(
        reader.readuntil(prompt.encode()),
        timeout=10
        )

    return response

async def main():
    host = "192.168.198.131"
    port = 30001
    prompt = "R1>"
    writer = None
    try:
        # connect to a host
        reader, writer, response = await connect(host, port, prompt)
        # execute a command
        command = "enable\r\n"
        prompt = prompt[:-1] + "#"  # convert prompt from R1> to R1#
        response = await execute_command(reader, writer, command, prompt)

        print(response.decode())  # .decode() => convert bytes to string
        # expected response: R1#  => successfuly executed enable command


        # close the connection: called in the finally statement
    except asyncio.TimeoutError as e:
        print("Connection Timed out:", e)
    except ConnectionError as e:
        print("ConnectionError:", e)
    except ValueError as e:
        print("ValueError:", e)
    except OSError as e:
        print("Network error failure:", e)
    finally:
        await close_connection(writer)


if __name__ == '__main__':
    asyncio.run(main())