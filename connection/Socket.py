from json import loads, dumps
from socket import socket, AF_INET, SOCK_STREAM


class Socket:
    def __init__(self, host, port):

        self.socket = socket(AF_INET, SOCK_STREAM)

        self.server_host = host
        self.port = port

        self.socket_type = None
        self.connection = None
        self.client_host = None


    def ready(self, socket_type ='client'):
        try:
            if socket_type not in ['client', 'server']:
                return False

            self.socket_type = socket_type

            if socket_type == 'client':
                self.socket.connect((self.server_host, self.port))

            else:
                self.socket.bind((self.server_host, self.port))
                self.socket.listen(1)

            return True

        except BaseException:
            return False


    def accept(self):
        self.connection, self.client_host = self.socket.accept()


    def send(self, data: dict):
        channel = self.socket

        if self.socket_type == 'server':
            channel = self.connection

        data = dumps(data).encode('utf-8')
        channel.sendall(data)


    def receive(self):
        channel = self.socket

        if self.socket_type == 'server':
            channel = self.connection

        data = channel.recv(1024).decode('utf-8')
        data = loads(data)

        return data


    def close(self):
        channel = self.socket

        if self.socket_type == 'server':
            channel = self.connection

        channel.close()
