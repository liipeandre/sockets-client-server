from connection.Socket import Socket


def client():

    socket = Socket('127.0.0.1', 1234)

    if socket.ready('client'):

        request = {
            "action": 'action_name',
            "data": []
        }

        socket.send(request)
        response = socket.receive()

        print(f"Received Message: {response}")


if __name__ == '__main__':
    client()
