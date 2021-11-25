from connection.Socket import Socket


def server():

    socket = Socket('127.0.0.1', 1234)

    if socket.ready('server'):

        while True:

            socket.accept()
            request = socket.receive()

            print(f"Received Message: {request}")

            response = request
            socket.send(response)

            socket.close()


if __name__ == '__main__':
    server()
